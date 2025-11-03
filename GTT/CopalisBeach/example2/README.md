# Copalis Beach example2

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

See [](../README) for more about the Copalis Beach location and a
list of other examples and tutorials based on this location.

## fgout and fgmax grids

The directory `$GTT/CopalisBeach/example2`
contains examples showing how to make `fgout` and `fgmax` files during the
simulation. Here `fg` stands for **fixed grid** and the basic idea is that the
user specifies a fixed Cartesian grid (typically in longitude-latitude) on
which the results are desired, independent of the structure and resolution
of the AMR grids that may be active in the region covering this fixed grid,
which will typically be changing with time.


### Key similarities and differences

The essential difference is that an fgout grid is a grid on which snapshots
of the solution will be written to the output directory at some set of times,
while an fgmax grid is one on which GeoClaw keeps track of the maximum value
of some set of quantities (such as water depth or speed) over the entire
simulation (or some user-specified time-interval) and then only prints these
out once at the end of the simulation.

**fgout grids** are useful for making an animation of simulated results, or for
capturing the depth and velocities in order to do post-processing such as
debris tracking.  For these applications it is very convenient to have the
values on a uniform grid that does not change with time. We may also need to
output the solution very frequently on this grid, more frequently than can be
done for the full AMR time frame solutions (which can be output at most
every coarse grid time step).  Moreover the full AMR output may be huge for
each time frame, whereas the fgout grid might cover a small portion of the
domain and there is only one value needed at each fgout point, not all the
overlapping AMR levels that might cover this point.

**fgmax grids** are useful for making inundation or hazard maps, for example.
They are also useful for viewing the radiation pattern of a tsunami over
the entire ocean. They can also be used to keep track of arrival times of the
tsunami at each point.

:::{seealso}
- [Fixed grid output documentation](https://www.clawpack.org/fgout.html)
- [Fixed grid monitoring documentation](https://www.clawpack.org/fgmax.html)
:::

In both cases the fg points may be at either finer or coarser resolution than
the AMR grids on which the calculation is being done, and some sort of
interpolation is need to evaluate quantities at each fg point. Two different
types of interpolation are supported:

- Zero-order interpolation: View the finite volume solution as piecewise
constant in each computational cell, and simply take the value from the finest
resolution AMR grid cell that covers the fg point at each time.
- Bilinear interpolation: Find the 4 computational cell centers that surround
the fg point (on the finest-resolution grid patch available) and compute a
bilinear function of the form $f(x,y) = a_1 + a_2x + a_3y + a_4xy$
that interpolates
these four values, and then evaluate this function at the fg point.

There are some subtleties in deciding which of these is better in different
contexts, discussed later and in
[Nearshore interpolation](https://www.clawpack.org/nearshore_interp.html).

There are some differences in the way fgout and fgmax grids are specified
in `setrun.py`, partly due to their different applications and partly for
historical reasons since fgmax grids were introduced around 2012 and fgout
grids a decade later.  For details see

- [Fixed grid output documentation](https://www.clawpack.org/fgout.html)
- [Fixed grid monitoring documentation](https://www.clawpack.org/fgmax.html)

One key difference is that for fgout grids the edges of an fgout domain are
specified and the actual fgout points are then the cell centers of equally
spaced grid cells covering this domain. This is similar to how the full
computational domain is specified in `setrun.py`.  The fgout grid is always
a two-dimensional uniform grid in the current implementation. This is typically
what is desired for making an animation or doing postprocessing such as
debris tracking.

By contrast, for fgmax grids there is more flexibility in how the actual
fgmax points are specified, with five different point style's supported
(see the documentation linked above for details). If `point_style == 2`
then a uniform two-dimensional grid is used, but the grid is specified
by giving the locations of the first and last *points* in each dimension,
rather than *cell edges* of surrounding cells as in the case of fgout grids.
This aligns better with how points are specified for the other point styles.

## Specification of fgmax and fgout for this example

The `setrun.py` file in this directory is very similar to the one in
[](../exercise1/README), with the addition of some lines shown below.
Near the top of the file we import two Python modules that are needed
to specify the fg grids:

    from clawpack.geoclaw import fgmax_tools, fgout_tools

These same two modules also have some tools for reading in and processing
the resulting output, as illustrated in [To Appear](fgmax_plots) and [To Appear](fgout_plots).

### Annotated fgmax grid section

Toward the bottom of the `setrun.py` file, the specification of the fgmax
grid appears.  Here's an annotated version of those lines:


        # -----------------------------
        # FGMAX GRIDS:
        # ------------------------------
        # set num_fgmax_val = 1 to save only max depth,
        #                     2 to also save max speed,
        #                     5 to also save max hs,hss,hmin
        rundata.fgmax_data.num_fgmax_val = 2

Setting `num_fgmax_val = 2` means that two values will be monitored at each
fgmax point, the water depth
$h$ and speed $s$, which is computed from the fluid velocity $(u,v)$ at each
time as $s = \sqrt{u^2 + v^2}$.  Since we are only keeping track of the
maximum over time, this is more useful than monitoring the maximum of $u$
and $v$ separately, since the velocities in the two directions might occur
at different times and knowing their maxima would not allow computing the
maximum speed.

If `num_fgmax_val = 1` were specified, only the water depth would be monitored,
while if `num_fgmax_val = 5` then additional quantities are monitored.
(Ideally we would allow more flexibility for the user to specify precisely
what to monitor, but that's not yet available).

        fgmax_grids = rundata.fgmax_data.fgmax_grids  # empty list initially

        # Now append to this list objects of class fgmax_tools.FGmaxGrid
        # specifying any fgmax grids.

        # Points on a uniform 2d grid:
        # grid resolution at 1" level
        dx_fine = 1/3600.

        fgmax = fgmax_tools.FGmaxGrid()  # define a new object to add to list
        fgmax.fgno = 1                   # id number for this fgmax grid
        fgmax.point_style = 2            # uniform rectangular x-y grid

        # fgmax_extent gives first and last grid points, which we choose
        # to be cell centers on a grid with dx = 1/3600.:
        fgmax_extent = [-124.19486111, -124.15597222, 47.10791667, 47.14597222]

        fgmax.x1 = fgmax_extent[0]
        fgmax.x2 = fgmax_extent[1]
        fgmax.y1 = fgmax_extent[2]
        fgmax.y2 = fgmax_extent[3]
        fgmax.dx = dx_fine
        fgmax.dy = dx_fine


We are creating an fgmax grid covering the `fgmax_extent` specified, with
a grid spacing of 1 arc-second.
Note that these values have been chosen so that the points will be centered
in computational grid cells at this resolution based on the edges of the
computational domain specified in `setrun.py`.  *[Add more about why centering
is desirable]*.

        fgmax.tstart_max = 35*60.     # when to start monitoring max values
        fgmax.tend_max = 1.e10        # when to stop monitoring max values

We specify that we monitor and update the maximum observed on this grid starting
only at time 35 minutes (and continuing to the end of the simulation).
From other simulations we know that the tsunami
does not arrive until around this time. Also the finer grid levels around
Copalis Beach are not introduced until time 30 minutes (as specified by the
AMR flagregions used).

        fgmax.dt_check = 10.          # target time (sec) increment between updating

This means that we only require monitoring the fgmax grid
(and possibly updating the maximum values stored) if the time since the last
update was more than 10 seconds.  On very fine grids the time step may be much
smaller than this.  For some problems you might want to set this value to be
smaller, e.g. 5 seconds, since large spikes in speed around the first wave
may happen over very short time scales.

        fgmax.min_level_check = amrdata.amr_levels_max  # monitor on finest level only

This means that only patches at the finest AMR level in this simulation will
be used for updating the fgmax values.  If there is no patch covering the point
at some time, the value will not be updated.  Initially there is a special
`NOT_SET` value stored in these locations, and so during post-processing these
fgmax files one needs to check for points that were never updated.

The reason for specifying `min_level_check` in this way is that early in the
simulation there may only be coarse grids covering a point and the water depth
on a coarse grid could be **much** larger than any value seen once the grid
is refined, since the coarse grid cell the point lies in might cover a lot
of off-shore area and hence have a large negative topography value and hence
large water depth initially, even if the point is really onshore and so has
much smaller `h` values on the finer grid(s).

        fgmax.arrival_tol = 0.2      # tolerance for flagging arrival

This specifies that the "arrival time" for the tsunami at each
fgmax point should be determined based on the first time the fgmax
point is wet and the water surface elevation
`eta` at this point exceeds 0.2 meters.

:::{warning}
There are better ways to monitor the arrival of the first wave (e.g. using
`h` is better than `eta`), and in practical applications one often wants to
keep track of several different times (e.g. when the water depth is first
above or below some list of thresholds).  An improved version of the
arrival time capabilities should be available in a future GeoClaw release.
:::

The next line is:

        fgmax.interp_method = 0      # 0 ==> pw const in cells, recommended

This specifies that zero-order interpolation should be used, as described above.
Set this value to `1` for piecewise linear.

        # add fg to the list of fgmax_grids, which is written to fgmax_grids.data
        fgmax_grids.append(fgmax)

`fgmax_grids` is initially an empty list and so we append the `fgmax` object
just created to this list.

If you want to specify a second fgmax grid, the entire fgmax code block could
be copied below this to set up a second version of `fgmax` and append this
to the list as well.  The bare bones version of this might look like:

        fgmax = fgmax_tools.FGmaxGrid()  # define a new object to add to list
        fgmax.fgno = 2                   # id number for this fgmax grid
        # set parameters for the extent, resolution, etc.
        fgmax_grids.append(fgmax)

You can use the same name `fgmax` in defining this second object, since
a new Python object will be created by `fgmax_tools.FGmaxGrid()` and won't
affect the object already in the `fgmax_grids` list.  But be
sure to give it a new ID `fgno` and to append it to the list already in use.

When you do `make data`, the specification of fgmax grids from `setrun.py`
will be used to create the data file `fgmax_grids.data` that will be read in
by the Fortran code, so you can check this file to make sure the desired
fgmax grid(s) appear.

The kml file `fgmax0001.kml` created by `make data` (since `setrun.py` calls
`kmltools.make_input_data_kmls(rundata)`) shows the footprint of the fgmax
grid with `fgno = 1`.


### Annotated fgout grid section

Toward the bottom of the `setrun.py` file, the specification of the fgout
grid appears.  Here's an annotated version of those lines:

To appear.
