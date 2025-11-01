# Setting up the GeoClaw run

This page describes the setup in `$GTT/CopalisBeach/example1`.

GeoClaw simulations are set up using a Python function called `setrun` that is
often found in a file `setrun.py`.  In this example directory several
different running conditions set up in the files `setrun1a.py`, `setrun1b.py`,
etc.

See [](output1a_annotated) for more discussion of the output that is printed to
the screen when you run the code using the `setrun1a.py` script described here.

:::{warning}
If you want to run the code in this directory, you should copy it
elsewhere first; see [](workflow:copy).
:::

## Makefiles

There are corresponding Makefiles labeled `Makefile1a`, `Makefile1b`, etc.
each of which has `SETRUN_FILE` set to a different setrun file.  The Makefiles
also set `OUTDIR` and `PLOTDIR` differently so that the output and plots
are directed to separate directories for each run.  (This is not usually
done, often the same `setrun.py` is used repeatedly and the output directory
`_output` is overwritten for each run, or might be moved to a give it a
different name such as `_output_run1` before doing the next run. But the
workflow you choose might depend on what you are trying to accomplish.)

To run the code as specified in `Makefile1a` you can specify that this
Makefile should be used in a command such as

    make .output -f Makefile1a

The bash script `make_example1a.sh` in this directory gives the sequence of
commands used to create both `_output1a` and `_plots1a`.  The script
`make_all.sh` puts these commands in a loop to create 4 sets of results and
plots.

## The setrun function, annotated

:::{seealso}
- [Specifying GeoClaw parameters in setrun.py](https://www.clawpack.org/setrun_geoclaw.html)
- [Specifying AMRClaw run-time parameters in setrun.py](https://www.clawpack.org/setrun_amrclaw.html)

However, this documentation is out of date and does not include all options.
:::

Let's take a closer look at the file `setrun1a.py`.  Much of what is in this
file is standard boilerplate that rarely changes between GeoClaw runs, and
typically a new problem is set up by copying some `setrun.py` as a template
and modifying a few things.  Here we focus on the things that were modified
for this particular case, [](README).  You should open `setrun1a.py` in an
editor to see where these things are in the file and note all the things
in between that often do not change.  In particular, everything above the
`Spatial domain` section is standard for GeoClaw.

### Setting the spatial domain

    # ---------------
    # Spatial domain:
    # ---------------

    # Number of space dimensions:
    clawdata.num_dim = num_dim      # should always be 2 in GeoClaw

    # Lower and upper edge of computational domain:

    clawdata.lower[0] = -128.5      # west longitude
    clawdata.upper[0] = -123.5      # east longitude

    clawdata.lower[1] = 45.         # south latitude
    clawdata.upper[1] = 49.         # north latitude

    # Number of grid cells: Coarsest grid is 4 arcminutes (1/15 degree)
    clawdata.num_cells[0] =  5*15
    clawdata.num_cells[1] =  4*15

This specifies the longitude and latitude extent of the computational domain
and the number of finite volume grid cells used to discretize it at the
coarsest level, which is Level 1 in the AMR terminology, see
[Adaptive mesh refinement (AMR) algorithms
documentation](https://www.clawpack.org/amr_algorithm.html).

Note several things about the number of cells chosen:
- The domain is 5 degrees by 4 degrees and we are specifying 15 cells per
  degree, so the spatial resolution will be $\Delta x = \Delta y = 60/15 = 4$
  arcminutes.
- See [](coordinates) for discussion of what this spatial resolution is in
  meters, and why you might not want to choose $\Delta x = \Delta y$ in when
  working in longitude-latitude coordinates.

### Initial time and restart?

    # -------------
    # Initial time:
    # -------------

    clawdata.t0 = 0.  # Start time in seconds

    # Restart from checkpoint file of a previous run?
    # If restarting, t0 above should be from original run, and the
    # restart_file 'fort.chkNNNNN' specified below should be in
    # the OUTDIR indicated in Makefile.

    clawdata.restart = False     # True to restart from prior results
    clawdata.restart_file = ''   # File to use for restart data

Often `t0 = 0`, but you could start the simulation at some other time.

:::{warning}
If you are providing a `dtopo` file for moving topography then you should
normally make sure that the first time in that file is later than `t0`.
See [geoclaw issue #679](https://github.com/clawpack/geoclaw/issues/679).
:::

Normally `clawdata.restart == False` and a new simulation is run starting
at time `t0`. But there may be times when you need to restart a previous run,
either to extend it out further in time or because you ran out of time on
a supercomputer and the run aborted, for example.  You can only restart if
you saved *checkpoint files* from the original run and `clawdata.restart_file`
indicates where to find the *checkpoint file* from which to do the restart.
See [](checkpoint_restart) for more details.

### Output times and style

    # -------------
    # Output times:
    #--------------

    # Specify at what times the results should be written to fort.q files.
    # Note that the time integration stops after the final output time.

    clawdata.output_style = 1

    if clawdata.output_style==1:
        # Output nout frames at equally spaced times up to tfinal:
        clawdata.num_output_times = 9
        clawdata.tfinal = 1.5*3600.
        clawdata.output_t0 = True  # output at initial (or restart) time?

    elif clawdata.output_style == 2:
        # Specify a list of output times.
        # e.g. at 0 and 60 seconds and then less frequently:
        clawdata.output_times = [0.,60., 1800., 3600., 5400.]

    elif clawdata.output_style == 3:
        # Output every iout timesteps with a total of ntot time steps:
        clawdata.output_step_interval = 1
        clawdata.total_steps = 3
        clawdata.output_t0 = True

There are three different values of `output_style` that are recognized:
- `output_style == 1:` specify the final time `tfinal` and how many equally
  spaced output times to use up to this time (so every 10 minutes in the
  example above).
- `output_style == 2:` Specify a list of times `output_times`,
  which need not be equally
  spaced.  You can also use python code in doing this, e.g.

      clawdata.output_times = [0, 60.] + list(np.arange(600,5401,600))

  would specify output at times 0 and 60 seconds and then every 10 minutes up to
  90 minutes.
- `output_style == 3:` Output every `output_step_interval` timesteps on the
  coarsest level for a total of `total_steps` coarsest-level timesteps.
  This is mostly used for debugging, but there may be times when you want the
  code to always take the maximum size time step it can and output at after
  some number of coarse steps.  (With the other output styles, the time steps
  will generally be shortened just before a specified output time in order
  to hit that time exactly.)

Note that for `output_style` 1 and 3 there is also a parameter
`clawdata.output_t0`.  The default True is if you don't set it, in which case
an output frame at time `t0` is produced (the initial conditions, often a
flat ocean in tsunami simulations).


:::{tip}
If you set

    clawdata.output_style = 1
    clawdata.num_output_times = 0
    clawdata.tfinal = 1.5*3600.
    clawdata.output_t0 = False

then the simulation will run out to 1.5 hours but no output frames will be
produced.  You might want to do this if you are only interested in the gauge
or fgmax output, for example.  This might be useful if doing a probabilistic
study with hundreds of runs, for example, since the output frames with all the
AMR grid levels can be very large.
:::

The next block of code:

    clawdata.output_format = 'binary32'      # 'ascii', 'binary', or 'binary32'
    clawdata.output_q_components = 'all'     # output all 3 components h,hu,hv


specifies the format of the output.  


:::{seealso}
[Output data styles and formats](https://www.clawpack.org/output_styles.html)
in the Clawpack documentation.
:::

### Verbosity

    # ---------------------------------------------------
    # Verbosity of messages to screen during integration:
    # ---------------------------------------------------

    # The current t, dt, and cfl will be printed every time step
    # at AMR levels <= verbosity.  Set verbosity = 0 for no printing.
    #   (E.g. verbosity == 2 means print only on levels 1 and 2.)
    clawdata.verbosity = 3

In this `setrun1a.py` we are using 3 levels of AMR and we set `verbosity = 3`
so that when we run GeoClaw it prints a line to the screen every time step
on each of the 3 levels.   If you examine the [sample output](??) you will
see that after each step on Level 1 there are two steps taken on Level 2 before
the next Level 1 step.  Moreover after each Level 2 step there are five Level 3
steps before the next Level 2 step.  This is because the refinement ratios
discussed below specify refinement by a factor of 2 from Level 1 to 2 and by a
factor of 5 from Level 2 to 3.

Note that the other `setrun` functions in this example directory have
`verbosity = 1` so that a line is printed only after the coarsest Level 1 step.
Setting `verbosity` too high can lead to a huge amount of output if you have
many levels of refinement (e.g. in `setrun1d.py` we use 8 levels with
`refinement_ratios = [2,5,2,2,2,3,3]`, so for
every time step on Level 1 there are roughly $2*5*2*2*2*3*3 = 720$ time steps
taken on Level 8).

:::{tip}
You can set `verbosity = 0` so that no time step information is printed,
and a line will be printed to the screen only at each output time.
:::

:::{tip}
You can redirect the output to a file rather than having it appear on the
screen using, e.g.

    make .output > geoclaw_output.txt

If you end this command with `&` it will also run the job in the background
so you get the shell prompt back and can do other things in the window.
(Use `fg` to bring the job back to the foreground, e.g. if you need to kill it.)

Another possibility is to pipe the output through the unix `tee` command:

    make .output | tee geoclaw_output.txt

which prints the output to the screen *and* also sends it to the file.
:::

Note that later in the `setrun` function there is another verbosity parameter:

    # print info about each regridding up to this level:
    amrdata.verbosity_regrid = 3

This causes the code to print out information every time it regrids at each
level up to the level specified, as discussed further below.
We normally set `verbosity_regrid = 0` to suppress printing regridding info,
but this can be useful and is turned on here so you can see the pattern of
regridding that is performed.

### Time stepping parameters

    # --------------
    # Time stepping:
    # --------------

    # if dt_variable==1: variable time steps used based on cfl_desired,
    # if dt_variable==0: fixed time steps dt = dt_initial will always be used.
    clawdata.dt_variable = True

    # Initial time step for variable dt.
    # If dt_variable==0 then dt=dt_initial for all steps:
    clawdata.dt_initial = 0.2

    # Max time step to be allowed if variable dt used:
    clawdata.dt_max = 1e+99

    # Desired Courant number if variable dt used
    clawdata.cfl_desired = 0.85
    # max Courant number to allow without retaking step with a smaller dt:
    clawdata.cfl_max = 1.0

    # Maximum number of time steps to allow between output times:
    clawdata.steps_max = 5000

See [Specifying classic run-time parameters in setrun.py](https://www.clawpack.org/setrun.html) for a description of these parameters.

:::{admonition} Todo
:class: note
*Add more description*
:::

### checkpoint files

    # --------------
    # Checkpointing:
    # --------------

    # Specify when checkpoint files should be created that can be
    # used to restart a computation.

    # negative checkpoint_style means alternate between aaaaa and bbbbb files
    # so that at most 2 checkpoint files exist at any time, useful when
    # doing frequent checkpoints of large problems.

    clawdata.checkpt_style = 0

    if clawdata.checkpt_style == 0:
        # Do not checkpoint at all
        pass

    elif clawdata.checkpt_style == 1:
        # Checkpoint only at tfinal.
        pass

    elif abs(clawdata.checkpt_style) == 2:
        # Specify a list of checkpoint times.
        clawdata.checkpt_times = 1800.*np.arange(1,6,1)

    elif abs(clawdata.checkpt_style) == 3:
        # Checkpoint every checkpt_interval timesteps (on Level 1)
        # and at the final time.
        clawdata.checkpt_interval = 5

Setting `clawdata.checkpt_style = 0` means that no checkpoint files will
be generated for this quick run.

See [](checkpoint_restart) for more discussion of these parameters.

### AMR parameters


    # ---------------
    # AMR parameters:
    # ---------------
    amrdata = rundata.amrdata

    # maximum size of each grid patch (in each direction):
    amrdata.max1d = 60    # default is 60

    # initial size of work array for AMR patches:
    amrdata.memsize = 10000000    # default is 1000000

The `amrdata.max1d` parameter controls how large individual grid patches
can be in each dimension, so in this example the 2D patches are
at most 60x60 grid cells.  This is the default value if you do not
specify this parameter in `setrun.py` and is usually a good choice.

The `amrdata.memsize` determines how much memory is allocated for a work
array used for keeping the solution on all the grid patches at all levels
of the AMR solution.  The default value in GeoClaw is currently 1e6, which
is generally too small, so here it is set to 1e7.  (If this work array size
is exceeded, the code automatically extends the array so the code does
not die, but it takes some time to do this re-allocation and copying of
data, so nice to avoid.)

    # max number of refinement levels:
    amrdata.amr_levels_max = 3

    # List of refinement ratios at each level (length at least mxnest-1)

    # Set up for 8 levels here, possibly using fewer:
    # dx = dy = 4', 2', 24", 12", 6", 3", 1", 1/3"
    refinement_ratios = [2,5,2,2,2,3,3]
    amrdata.refinement_ratios_x = refinement_ratios
    amrdata.refinement_ratios_y = refinement_ratios
    amrdata.refinement_ratios_t = refinement_ratios

:::{note}
These are the AMR parameters you will most frequently need to change for a
new problem or to increase the resolution of the problem you are solving.
:::

In this `setrun1a.py`, we specify that only 3 levels of refinement are allowed.
(The other examples in this directory have larger values of
`amrdata.amr_levels_max`.)  The `refinement_ratios` array consists of integers
telling how much to refine the grid from one level to the next.  This is
done here in a way that refinement ratios are the same in `x, y` and `t`,
but they need not be.

From Level 1 to 2, the grid is refined by a factor of 2 and from Level 2 to 3
by a factor of 5.  The array `refinement_ratios` can be longer than necessary,
and here it includes the refinement ratios that will be used for levels 4--8
in the other examples in this directory.

:::{note}
The refinement in time is also controlled by the Courant number
specified, described below...
:::

    # Specify type of each aux variable in amrdata.auxtype.
    # This must be a list of length maux, each element of which is one of:
    #   'center',  'capacity', 'xleft', or 'yleft'  (see documentation).

    amrdata.aux_type = ['center','capacity','yleft']

    # Flag using refinement routine flag2refine rather than richardson error
    amrdata.flag_richardson = False    # use Richardson?
    amrdata.flag2refine = True

For GeoClaw run, the parameters above typically never change.

    # steps to take on each level L between regriddings of level L+1:
    amrdata.regrid_interval = 3

    # width of buffer zone around flagged points:
    # (typically the same as regrid_interval so waves don't escape):
    amrdata.regrid_buffer_width  = 2

    # clustering alg. cutoff for (# flagged pts) / (total # of cells refined)
    # (closer to 1.0 => more small grids may be needed to cover flagged cells)
    amrdata.clustering_cutoff = 0.7

    # print info about each regridding up to this level:
    amrdata.verbosity_regrid = 3

The parameters above specify that every 3 time steps on each AMR level the
finer grids should be regridded, which means that cells on the current level
are tested against various criteria and some are flagged as needed refinement
(see below).  The flagged cells are then clustered into rectangular patches,
but before doing so a buffer of 2 cells around each flagged cell is also
flagged.  This helps insure that propagating waves do not escape from the
refined region before the next regridding happens.  The `clustering_cutoff`
determines how many unflagged points are allowed in the rectangular
patches, and 0.7 is generally fine.

(wave_tolerance)=
### Additional refinement settings for GeoClaw

    # ------------------------------
    # Set data specific to GeoClaw:
    # ------------------------------

    # Refinement settings
    refinement_data = rundata.refinement_data
    refinement_data.variable_dt_refinement_ratios = True
    refinement_data.wave_tolerance = 0.1

For GeoClaw some additional AMR parameters are set (all the parameters
so far also exist in the more general AMRClaw code, if AMR is applied
to other problems such as advection, acoustics, gas dynamics, etc.)

You normally want to set `variable_dt_refinement_ratios = True`, which
allows GeoClaw to adjust the refinement ratio in time to be something
different than specified earlier. (**explain**).

`wave_tolerance = 0.1` means that cells might be flagged for refinement if
the magnitude of the surface elevation `abs(eta)` is greater than 0.1 meter.
This is only used, however, for cells that are allowed to be flagged to
a higher level but not required to be flagged, as explained further below
in [](setrun_flagregions).

### `geo_data` parameters

    geo_data = rundata.geo_data

    # == Physics ==
    geo_data.gravity = 9.81            # m/s**2
    geo_data.coordinate_system = 2     # 1=meters, 2=long-lat
    geo_data.earth_radius = 6367.5e3   # mean radius in meters

    # == Forcing Options
    geo_data.coriolis_forcing = False  # apply Coriolis terms?

    # == Algorithm and Initial Conditions ==
    geo_data.sea_level = 0.0          # level to fill water up to initially
    geo_data.dry_tolerance = 1.e-3    # smaller depths are set to 0 each step
    geo_data.friction_forcing = True  # using a Manning friction term?
    geo_data.manning_coefficient =.025
    geo_data.friction_depth = 200     # how deep to apply friction term
    geo_data.speed_limit = 20.        # limit on speed sqrt(u**2 + v**2)

Some of these parameters are described below...

#### Physics

You won't be changing `gravity` unless you are modeling tsunamis on Mars,
for example, as has been done (e.g. [??]), in which case the poorly named
`earth_radius` should be changed as well.

#### Coriolis terms

For global tsunami modeling, the conventional wisdom is that it is not
necessary to apply [Coriolis terms](??) due to the very small fluid velocities
in the tsunami wave  (**Note:** the wave speeds $\sqrt{gh}$ may be very large
in the deep ocean, but the depth-averaged fluid velocity is generally tiny.)
So we always set `coriolis_forcing = False`, but the terms have been
implemented.

#### sea_level

The initial data for GeoClaw often consists of an ocean at rest with the
initial water surface at some level relative to the vertical datum of the
topography files being used. See [](SeaLevel) and

- [Set eta init documentation](https://www.clawpack.org/set_eta_init.html)

for more details, but here's a
summary of some things to consider:

- If the coastal topography is referenced to MHW, for example, then setting
  `sea_level = 0` will initialize the water to MHW.  If you want to do a
  simulation at MLW instead, you need to determine the difference `MLW - MHW`
  at the coastal location of interest (a negative number, in meters) and set
  `sea_level` to this value.
- If the topography is referenced to NAVD88 you need to determine the proper
  offset for whatever tide stage you want to model.
- There is a Fortran subroutine `set_eta_init` that can be used to specify
  different values of the initial `eta` (water surface level) as a function
  of the spatial coordinates `(x,y)`.  This can be used to initialize an
  onshore lake to a higher surface level than the ocean, for example.
- The default `set_eta_init` subroutine adjusts the initial sea level to
  incorporate coastal uplift or subsidence if fine grids are first introduced
  in a region where there is coseismic deformation at some time after the
  earthquake specified by the dtopo file has occurred.  The need for this
  is discussed in [??]().

#### dry tolerance

The value `dry_tolerance = 1.e-3` (1 mm) works fine in general.  Each time
step, any value of water depth `h` less than this is reset to 0.  This is done
in particular to avoid negative `h < 0`, which would cause the simulation to
die.  This is non-physical but the numerical method sometimes has tiny
undershoots that need to be eliminated.

#### Bottom friction

    geo_data.friction_forcing = True
    geo_data.manning_coefficient =.025
    geo_data.friction_depth = 200

See [Manning friction term documentation](https://www.clawpack.org/manning.html).

#### Speed limit

    geo_data.speed_limit = 20.  # limit on speed sqrt(u**2 + v**2)

Very large speeds sometimes arise in cells that have a small amount of
water and a large jump in topography to a neighboring lower cell with a lower
surface elevation eta.  This parameter specifies that any cell where the
fluid speed is greater than 20 m/s should be scaled back to this level, which
reduces the chances of the code blowing up and aborting.
See [Setting a Speed Limit to Avoid Instabilities](https://www.clawpack.org/speed_limit.html)


### topo files

    # ---------------
    # TOPO:
    # ---------------
    # == topo.data values ==
    topo_data = rundata.topo_data

    topofiles = topo_data.topofiles   # empty list initially
    # for topography, append tuples/lists of the form:
    #    [topotype, fname]

    # 30-sec topo:
    topo_file = os.path.join(topodir, 'etopo22_30s_-130_-122_40_50_30sec.asc')
    topofiles.append([3, topo_file])

    # 1/3 arcsec topo
    topo_file = os.path.join(topodir, 'Copalis_13s.asc')
    topofiles.append([3, topo_file])

The two topo files specified here are created by the Jupyter notebooks
[](../../topo/fetch_etopo22) and [](../../topo/CopalisTopo), respectively.
They both have `topotype = 3` as described in the
[Topography data documentation](https://www.clawpack.org/topo.html).

:::{warning}
Normally additional topography files with intermediate resolution would be used,
e.g. 2-arcsec topography around a larger coastal region than where the 1/3"
is provided.  To keep this example simple, additional topography has been
omitted here.
:::

### dtopo files


    # ---------------
    # DTOPO:
    # ---------------
    # == setdtopo.data values ==
    # for moving topography, append lists of the form  [dtopo_type, fname]
    # to the initially empty list rundata.dtopo_data.dtopofiles:
    dtopo_data = rundata.dtopo_data
    dtopofile = os.path.join(dtopodir, 'ASCE_SIFT_Region2.dtt3')
    dtopo_data.dtopofiles.append([3, dtopofile])
    dtopo_data.dt_max_dtopo = 0.2  # max timestep (sec) while topo is changing

The dtopo file `ASCE_SIFT_Region2.dtt3` is created by the Jupyter notebook
[](../../dtopo/ASCE_SIFT_fRegion2), with `dtopo_type == 3`, see the
[dtopo file documentation](https://www.clawpack.org/dtopo.html).


(setrun_flagregions)=
### flagregions to guide AMR

    # ---------------
    # REGIONS:
    # ---------------

    flagregions = rundata.flagregiondata.flagregions  # empty list initially

    # Computational domain Variable Region:
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_domain'
    flagregion.minlevel = 1
    flagregion.maxlevel = 2
    flagregion.t1 = 0.
    flagregion.t2 = 1e9
    flagregion.spatial_region_type = 1  # Rectangle
    x1,y1 = clawdata.lower
    x2,y2 = clawdata.upper
    # Domain is [x1,x2,y1,y2], and add a buffer around it (not really needed):
    flagregion.spatial_region = [x1-0.2, x2+0.2, y1-0.2, y2+0.2]
    flagregions.append(flagregion)

See [Specifying flagregions for adaptive
refinement](https://www.clawpack.org/flagregions.html) for
general discussion of using flagregions to guide adaptive refinement.

For this initial coarse grid simulation, we only specify three flagregions
to guide the adaptive mesh refinement.  The first flagregion `Region_domain`
defined above specifies that the entire computational domain can be refined to
2 levels for all time
(but refinement beyond Level 1 is not forced anywhere by this region).

    # dtopo region - force refinement even before there is any deformation
    # to the resolution needed to resolve the initial waves well.
    # This region forces a certain level of refinement over a short time.
    # Normally this would cover all of dtopo, but for this simplified
    # test problem the domain is truncated and we are only going out to
    # a short time so we don't need to refine even all of the dtopo within
    # the domain.
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_dtopo'
    flagregion.minlevel = 4
    flagregion.maxlevel = 4
    flagregion.t1 = 0.
    flagregion.t2 = 10.
    flagregion.spatial_region_type = 1  # Rectangle
    flagregion.spatial_region = [-126.6,-124.,45.5,48.5]
    flagregions.append(flagregion)

The second region `Region_dtopo` specifies a `spatial_region` around the
earthquake source should be refined to Level 4 starting at time 0.
Since the initial conditions are an ocean at rest, this is necessary to
insure that ample refinement is present in the region where the deformation
takes place.

This forced refinement ends at time
time 10 seconds.  By this time the surface elevation is far from zero in the
source region and so the next flagregion together with the
`wave_tolerance` specified below insures that the
region with large waves near the coast of interest remains refined to
Level 4.

    # Region12sec - 24 to  12 sec:
    # Level 4 is 12 sec
    # (other regions below will force/allow more refinement)
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_12sec'
    flagregion.minlevel = 3
    flagregion.maxlevel = 4
    flagregion.t1 = 0.
    flagregion.t2 = 1e9
    flagregion.spatial_region_type = 1  # Rectangle
    flagregion.spatial_region = [-126.6,-124.,46.27,47.68]
    flagregions.append(flagregion)


This flagregion specifies a rectangle where at least 3 levels and possibly 4
levels are used, and covers the coastal region of interest and a significant
distance offshore.

For this `setrun1a.py`, recall that `amr_max_levels = 3`, so in fact 4 levels
will never be used and this flagregion would have the same effect if we set
`maxlevel = 3`. But for the other examples in this directory, at least
4 levels are allowed, and so `maxlevel = 4` allows finer grids in this
region.


:::{note}
When flagging cells at level L for possible refinement to Level L+1, GeoClaw
finds all flagregions that contain the cell center, and then uses the
maximum of all the `flagregion.minlevel` values for such flagregions and
marks the cell for refinement if this maximum is larger than L.  It also
uses the maximum of all the `flagregion.maxlevel` values and insures that the
cell will not be flagged for refinement if this value is less then L+1.
If the cell is allowed to be flagged but not required to be, then the default
criterion is to flag the cell if `abs(eta) > wave_tolerance`, the value set
earlier in [](wave_tolerance).
:::

:::{seealso}
See [AMR refinement criteria](https://www.clawpack.org/refinement.html) for
more details about refinement criteria.
:::

### Gauges

    # ---------------
    # GAUGES:
    # ---------------

    gauges = rundata.gaugedata.gauges   # empty list initially
    # for gauges append tuples/lists of the form
    #   [gaugeno, x, y, t1, t2]

    # Note: it is best to center gauges in cells at finest resolution
    # (not done here)
    gauges.append([101, -124.1895833, 47.1162500, 0, 1e9]) # slightly offshore
    gauges.append([102, -124.1804167, 47.1162500, 0, 1e9]) # onshore
    gauges.append([103, -124.1704167, 47.1162500, 0, 1e9]) # in river

Each gauge is specified by a list `[gaugeno, x, y, t1, t2]`
where `t1` and `t2` set the time interval over which the gauge will be
recording data, here from time 0 to "forever".

The three gauges specified here have longitudes `x` and latitudes `y` that
were chosen so that each gauge is in the center of a grid cell for any grid
patch that is on a grid with resolution 3", which means it is also centered
on grids with resolution 1" or 1/3" (so on AMR levels 6, 7, and 8)
See [](centering_gauges) and
[Nearshore interpolation](https://www.clawpack.org/nearshore_interp.html)
for a discussion of why this is desirable in general.

This centering is performed by the Python script `center_gauges.py`
in this directory.

:::{note}
For the coarse simulation set up in this `setrun1a.py`, these gauges are
not centered on the finest grid resolution we are using near shore, which is 24"
on Level 3. But this raises no issues for this particular problem.
See [](copalis_example1_gauges) for some discussion of other issues that can arise
when interpreting the gauge results in and AMR simulation in regions where the
maximum refinement level changes with time.
:::


    rundata.gaugedata.file_format = 'ascii'  # often use 'binary32'

Setting `file_format = 'ascii'` produces files in the `_output` directory
with names like `gauge00101.txt` that contains a header followed by
all the gauge time series output,
with columns `level, t, h, hu, hv, eta`.  The integer `level` is the finest AMR
refinement level that covered the gauge location at each time and the values
`h, hu, hv, eta` were obtained from a patch at that level (either by
interpolation or as the value in the containing grid cell, as described
in [Nearshore interpolation](https://www.clawpack.org/nearshore_interp.html).)

For problems with many gauges or lots of time points it may be better to
use a binary format, setting `file_format` to `binary` or `binary32`, in
which case `gauge00101.txt` contains only the header information and the
arrays of time series are in `gauge00101.bin`, stored either as full
"double precision" 64-bit floating point numbers or as 32-bit "single precision"
values, which is generally plenty of significant figures for gauge output
and gives files that are half as large.

    #rundata.gaugedata.min_time_increment = 5 # minimum seconds between outputs

Since this line is commented out, a new line of gauge output is printed for
every time step on the finest level that covers the gauge, giving the best
possible resolution in time. If `min_time_increment` is set to some value
greater than 0, then a new line is printed only if at least this much time
(in seconds) has passed since the last time a value was printed.  Larger
values of this parameter lead to smaller file sizes and may still give adequate
temporal resolution.

:::{seealso}
See the [Gauges documentation](https://www.clawpack.org/gauges.html) for
general information about specifying gauge locations and related parameters.
:::



### create kml files

    # To create kml files of inputs:
    from clawpack.geoclaw import kmltools
    kmltools.make_input_data_kmls(rundata)

These lines appear in the `__main__` program at the end of the function
definition. Once all the input data is specified in the `rundata` object,
this function creates a set of `kml` files that can be opened in Google Earth
or other GIS tools to show a variety of useful things, in particular:

- Rectangles showing the computational domain, the extents of any topo and
  dtopo files, and the flagregions specified.

- Any gauges specified as thumbtack points.

This can be very useful in determining if you have set things up properly
in `setrun` before running the code.

:::{tip}
If you open all the kml files, then clicking on one of the objects in the
view will generally pop up some information about it, e.g. the long-lat extents
of rectangles, the `minlevel` and `maxlevel` for flagregions, coordinates of
gauges, etc.  You may have to deselect some items in the menu to click on ones
that are show up underneath them.
:::
