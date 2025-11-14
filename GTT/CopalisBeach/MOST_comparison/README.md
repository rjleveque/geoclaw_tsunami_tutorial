(copalis:most_comparison)=
# Comparison using the MOST model setup

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

See [](../README) for more about the Copalis Beach location and a
list of other examples and tutorials based on this location.

This directory `$GTT/CopalisBeach/MOST_comparison`
contains code to perform a GeoClaw simulation that mimics the setup of
the MOST model used by the NOAA Center for Tsunami Research (NCTR),
which uses fixed nested grids at 3 resolutions, called the A, B, and C grids.

The Copalis Beach example used in this tutorial has also been explored by
the NCTR group using the MOST model, and they provided the grid data
that is in the subdirectory `MOST_data`.  Note that these grids are used
both as the topography DEMs and as the computational grids in MOST.
(Use the `fetch_MOST_data.py` script to fetch this data.)

The script `convert_most_to_asc.py` converts these into a standard GeoClaw
topofile format for use as topofiles in this example.   The `setrun.py`
file specifies 3 levels of fixed refinement with no regridding, and covering
the same regions as the A, B, and C grids.

:::{note}
For GeoClaw, it is necessary to add a 4th coarser
level on a larger domain covering more of the ocean in order to capture 
the outgoing portion of the initial waves without artifacts coming
from the domain boundaries.  MOST handles this by using a precomputed
tsunami from the NOAA propagation database to provide boundary conditions
at the edge of the A grid.
:::

:::{warning}
This example still Work in Progress, and the `setrun.py` is for an
old 3-level run that didn't work so well.
:::

## Changes to `setrun.py`

The file `$GTT/CopalisBeach/exercise1/setrun.py`
was modified to create the `setrun.py` file in this directory.

Below are the changes needed to force fixed resolution on the A, B, and C
grids.

First we set the domain extent and resolution to match the A grid:

    clawdata.lower[0] = -126.       # west longitude
    clawdata.upper[0] = -123.75     # east longitude

    clawdata.lower[1] = 45.         # south latitude
    clawdata.upper[1] = 48.5        # north latitude

    # Number of grid cells: Coarsest grid is 15 arcsec (1/240 degree)
    clawdata.num_cells[0] =  540
    clawdata.num_cells[1] =  840


Next we specify three levels of AMR with the resolutions of the
A, B, and C grids:


    # max number of refinement levels:
    amrdata.amr_levels_max = 3

    # List of refinement ratios at each level (length at least mxnest-1)

    # Set up for 8 levels here, possibly using fewer:
    # dx = dy = 15", 3", 1/3"
    refinement_ratios = [5,9]
    amrdata.refinement_ratios_x = refinement_ratios
    amrdata.refinement_ratios_y = refinement_ratios
    amrdata.refinement_ratios_t = refinement_ratios

We also specify that the initial grid refinement determined at time `t0`
should never be modified (no regridding is done).  We also specify that
the points flagged for refinement by the flagregions specified below
should not be buffered by additional points, so the refinement patches
at Levels 2 and 3 should identically agree with the B and C grids at all
times:

    # steps to take on each level L between regriddings of level L+1:
    amrdata.regrid_interval = 100000000  # NEVER REGRID

    # width of buffer zone around flagged points:
    # (typically the same as regrid_interval so waves don't escape):
    amrdata.regrid_buffer_width  = 0   # NO BUFFER around Bgrid, Cgrid

    # clustering alg. cutoff for (# flagged pts) / (total # of cells refined)
    # (closer to 1.0 => more small grids may be needed to cover flagged cells)
    amrdata.clustering_cutoff = 0.7 # SHOULDN'T MATTER (only flag in rectangles)

Finally, the flagregions below specify three regions with each
`spatial_region` specified based on the extent of the A, B and C grids:

    # ---------------
    # REGIONS:
    # ---------------

    flagregions = rundata.flagregiondata.flagregions  # empty list initially

    # MOST A grid: (full computational domain)
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_Agrid'
    flagregion.minlevel = 1
    flagregion.maxlevel = 1
    flagregion.t1 = 0.
    flagregion.t2 = 1e9
    flagregion.spatial_region_type = 1  # Rectangle
    x1,y1 = clawdata.lower
    x2,y2 = clawdata.upper
    flagregion.spatial_region = [x1,x2,y1,y2]
    flagregions.append(flagregion)


    # MOST B grid
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_Bgrid'
    flagregion.minlevel = 2
    flagregion.maxlevel = 2
    flagregion.t1 = 0.
    flagregion.t2 = 1e9
    flagregion.spatial_region_type = 1  # Rectangle
    flagregion.spatial_region = [-126.5, -124.1, 47.0, 47.4]
    flagregions.append(flagregion)

    # MOST C grid
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_Cgrid'
    flagregion.minlevel = 3
    flagregion.maxlevel = 3
    flagregion.t1 = 0.
    flagregion.t2 = 1e9
    flagregion.spatial_region_type = 1  # Rectangle
    flagregion.spatial_region = [-124.25, -124.14, 47.1, 47.18]
    flagregions.append(flagregion)

