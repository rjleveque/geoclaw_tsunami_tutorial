
(coordinates)=
# Coordinates and grid resolution

## meters vs longitude-latitude

The partial differential equations (PDEs) solved in GeoClaw are naturally written
in units of meters.  In GeoClaw you can specify that your computational domain is
expressed in meters by setting

    rundata.geo_data.coordinate_system = 1

in `setrun.py`, in which case the upper and lower limits of the domain should
be in meters, along with the corners of refinement `flagregions`, edges of
`fgmax` or `fgout` grids, locations of gauges, etc.

For many tsunami modeling problems, we instead use longitude-latitude
coordinates, normally with the World Geodetic System 1984 (WGS84) coordinate
system, specified by ESPG:4326 in some GIS systems.  In this case, set

    rundata.geo_data.coordinate_system = 2

and limits of the domain and all other location specifiers in `setrun.py`
should be in longitude-latitude.  

:::{tip}
Note that our convention is to specify
longitude first in tuples `(x,y)` and this is the order used to specify gauge
locations, for example.  In many GIS systems the opposite order is used, but
as mathematicians we specify the horizontal coordinate first in describing
points on a map.
:::

(coordinates:resolution)=
## Choice of grid resolution

When written in meter coordinates, the PDEs used in GeoClaw are isotropic (on a
uniform flat bottom) and waves propagate at the same speed in all directions.
This suggests that it is most efficient to use the same grid resolution in $x$
and $y$, with $\Delta x = \Delta y$. The time step that can be used is related
to $\Delta x$ and $\Delta y$ based on the maximum wave speed on the grid
and the [CFL condition](CFL).

When solving a problem set up in meters it is thus natural to take $\Delta x =
\Delta y$ for most problems.  But if the problem is set up so that $x$ and $y$
are longitude and latitude (`coordinate_system = 2`), it may be less clear
how to choose the relation between $\Delta x$ and $\Delta y$. Often we choose
$\Delta x = \Delta y$ (e.g. talking about "1 arcsecond resolution" usually
means the two are equal).  This is partly because the topography DEMs used as
input are often in WGS84 coordinates on equally spaced grids with
$\Delta x = \Delta y$ and it seems natural to use the same resolution for the
simulation output. (Sometimes we might even want exactly the same grid points
for the output as the input DEM, see [??](DEMresolution).)

Here are some things to consider in choosing the resolution:

- One degree in latitude is about 111 km, so 1 arcminute (1') is about
1.85 km.  (Note also that 1' of latitude is exactly 1 nautical mile,
by definition).  One arcsecond (1") in latitude
is 1/60 arcminute, so about 31 m.

- One degree in longitude is smaller than $1\deg$ of latitude
by a factor of $\cos(y)$ at latitude $y$.
So for example at 47 degrees (off the WA coast), this is a factor of 0.68,
about 2/3 the length of 1 degree latitude.

- You do not need to use $\Delta x = \Delta y$ in GeoClaw, and for the WA
coast, for example, it might make more sense to choose
$\Delta x = 1.5\Delta y$ so that the distances these lengths are more nearly
equal when converted to meters.  This suggests that if $\Delta y = 2"$
then perhaps it would be best to use $\Delta x = 3"$ since the simulation
would run faster than with $\Delta x = 2"$ and would have roughly the same
resolution of about $(2/3600)*111e3) \approx 62$ meters in both directions.

## Resolution of adaptively refined grid patches

Also remember that in GeoClaw we specify the spatial resolution of the coarsest
Level 1 grid when setting `clawdata.num_cells` in `setrun.py`, and then the
resolution of refined patches is determined by the refinement ratios specified
by the lists `amrdata.refinement_ratios_x` and
`amrdata.refinement_ratios_y` (see [??](AMR) and
[](GTT/CopalisBeach/example1/setrun_description)).  These ratios in `x` and `y`
are usually the same so that if $\Delta x = \Delta y$ on Level 1 then the
same will be true on every finer level, for example.
