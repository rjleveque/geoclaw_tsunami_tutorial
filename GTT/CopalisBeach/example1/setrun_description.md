# Setting up the GeoClaw run

This page describes the setup in `$GTT/CopalisBeach/example1`.

GeoClaw simulations are set up using a Python function called `setrun` that is
often found in a file `setrun.py`.  In this example directory several
different running conditions set up in the files `setrun1a.py`, `setrun1b.py`,
etc.

See [](output1a_annotated) for more discussion of the output that is printed to
the screen when you run the code using the `setrun1a.py` script described here.

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

## The setrun function

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
- See [](../../../coordinates) for discussion of what this spatial resolution is in
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
See [geoclaw#??](issue).
:::

Normally `clawdata.restart == False` and a new simulation is run starting
at time `t0`. But there may be times when you need to restart a previous run,
either to extend it out further in time or because you ran out of time on
a supercomputer and the run aborted, for example.  You can only restart if
you saved *checkpoint files* from the original run and `clawdata.restart_file`
indicates where to find the *checkpoint file* from which to do the restart.
See [??](checkpoint_restart) for more details.

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


specifies the format of the output.  See [??]().

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

### Time stepping paramers

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

:::{admonition} Todo
:class: note
*Add description*
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

:::{admonition} Todo
:class: note
*Add description*
:::
### AMR parameters


    # ---------------
    # AMR parameters:
    # ---------------
    amrdata = rundata.amrdata

    # max number of refinement levels:
    amrdata.amr_levels_max = 3

    # List of refinement ratios at each level (length at least mxnest-1)

    # Set up for 8 levels here, possibly using fewer:
    # dx = dy = 4', 2', 24", 12", 6", 3", 1", 1/3"
    refinement_ratios = [2,5,2,2,2,3,3]
    amrdata.refinement_ratios_x = refinement_ratios
    amrdata.refinement_ratios_y = refinement_ratios
    amrdata.refinement_ratios_t = refinement_ratios

    # Specify type of each aux variable in amrdata.auxtype.
    # This must be a list of length maux, each element of which is one of:
    #   'center',  'capacity', 'xleft', or 'yleft'  (see documentation).

    amrdata.aux_type = ['center','capacity','yleft']

    # Flag using refinement routine flag2refine rather than richardson error
    amrdata.flag_richardson = False    # use Richardson?
    amrdata.flag2refine = True

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

:::{admonition} Todo
:class: note
*Add description*
:::

### `geo_data` parameters


    # ------------------------------
    # Set data specific to GeoClaw:
    # ------------------------------

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

See [Setting a Speed Limit to Avoid Instabilities](https://www.clawpack.org/speed_limit.html)

### Refinement parameters

    # Refinement settings
    refinement_data = rundata.refinement_data
    refinement_data.variable_dt_refinement_ratios = True
    refinement_data.wave_tolerance = 0.1

:::{admonition} Todo
:class: note
*Add description*
:::

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

:::{admonition} Todo
:class: note
*Add description*
:::

### dtopo files


    # ---------------
    # DTOPO:
    # ---------------
    # == setdtopo.data values ==
    dtopo_data = rundata.dtopo_data
    dtopofile = os.path.join(dtopodir, 'ASCE_SIFT_Region2.dtt3')
    dtopo_data.dtopofiles = [[3, dtopofile]]
    dtopo_data.dt_max_dtopo = 0.2  # max timestep (sec) while topo is changing

:::{admonition} Todo
:class: note
*Add description*
:::

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

:::{admonition} Todo
:class: note
*Add description*
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
    gauges.append([101, -124.19, 47.116, 0., 1e9])
    gauges.append([102, -124.18, 47.116, 0., 1e9])
    gauges.append([103, -124.17, 47.116, 0., 1e9])


    rundata.gaugedata.file_format = 'ascii'  # often use 'binary32'
    #rundata.gaugedata.min_time_increment = 5 # minimum seconds between outputs

:::{admonition} Todo
:class: note
*Add description*
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
