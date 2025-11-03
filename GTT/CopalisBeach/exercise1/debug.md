(copalis_debug)=
# Running/debugging the Copalis exercise1 code

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

The directory `$GTT/CopalisBeach/exercise1`
contains GeoClaw `setrun` and `setplot` functions for one example run.
See [](README) for some ideas of how you might try to modify these in this
exercise.

Getting the original code running is the first step in this exercise.

:::{warning}
If you want to run the code in this directory, you should copy it
elsewhere first (see [](workflow:copy)).

But if you follow this advice and are working in a different
directory than the `$GTT` directory, then you may discover that
files are not always where expected in these tutorials
(still debugging this workflow!).  So some
adjustments in paths may be necessary and perhaps the rest of this page will
help with getting things running.
:::

(copalis:debug:fetch_input_data)=
## Acquiring the input data

The example in this directory requires two topo files and one dtopo file,
and in `setrun.py` the location of these files is set by these lines:

    topodir = '../../topo/topofiles'  # path to topofiles used below
    dtopodir = '../../dtopo/dtopofiles'  # path to dtopofile used below

You should be able to fetch these files from an online data repository
using the script `../fetch_input_data.py`, e.g. via:

    $ cd ..
    $ python fetch_input_data.py

Alternatively, you should be able to create them by running the Jupyter notebooks
in the directories `../../topo` and `../../dtopo`, see
[](topodir) and [](dtopodir).

If you fail to have these files in the expected location, you will get an
error when you try to `make data`, see [](copalis:debug:missing_topo).
If you have the files in a different location,
you could fix this by modifying the paths set in `setrun.py`.


(copalis:debug:make_exe)=
## Making the Fortran executable

:::{seealso}
- [](makefile_description)
:::

Before running the code in this directory, you should make sure the following
environment variables are set:

- `CLAW` should point to the top level of the `clawpack` repository code.
- `PYTHONPATH` should include `$CLAW` (maybe other paths too, separated by `:`)
- `FC`, `FFLAGS`, `OMP_NUM_THREADS` could be set, or else values in the Makefile
  are used (see [](makefile_description)).

Then try doing this at the command line:

    $ make check

This prints out the values of several environment/Makefile variables.

You should see something like:

    ===================
    CLAW = /Users/rjl/clawpack_src/clawpack-v5.13.1
    OMP_NUM_THREADS = 6
    RUNEXE =
    EXE = xgeoclaw
    FC = gfortran
    FFLAGS = -O2 -fopenmp
    LFLAGS = -O2 -fopenmp
    OUTDIR = _output
    PLOTDIR = _plots
    ===================

:::{tip}
The variable `RUNEXE` isn't needed in general, but can be set to a command
that should be prepended to `EXE` to actually run the executable.
E.g. if you are running the dispersive version of geoclaw, which also uses
MPI, then `RUNEXE` must be something like `mpiexec`.
:::


### Compile and link the Fortran code

You need to make the Fortran executable file specified by `EXE` in the
`make check` output above.

In general you can do:

    $ make .exe

to create the executable. If all the GeoClaw library routines are already
compiled (because you've already run other problems), then this should be quick
since it only requires linking them together into the `xgeoclaw` executable.

If you see:

    make: Nothing to be done for `.exe'.

then the executable is already up to date, because you have already run the
code in this directory and the Fortran code hasn't been changed since then.

If this is your first time compiling GeoClaw you will see output from all the
individual codes being compiled.

:::{tip}
You can force all the Fortran codes to be recompiled by doing:

    $ make new

This is usually not necessary, but may be worth trying if you seem to be
getting some strange Fortran error.

**This is necessary** if you want to change compilers, e.g. if you compiled
everything with `gfortran` but now want to set `FC` to `ifx` to use the intel
compiler instead (which may make an executable that runs faster,
but is not free). Then you have to do `make new` to recompile everything.
:::



## Make data files based on `setrun.py`

Next try:

    $ make data

This should produce something like:

    rm -f .data
    python setrun.py                geoclaw                  
    Domain:   -128.500000  -123.500000   45.000000   49.000000
    Level 1 resolution:  dy = 0 deg, 4 min, 0 sec = 7400 meters

    Level 2 resolution:  dy = 0 deg, 2 min, 0 sec = 3700 meters  (refined by 2)

    Level 3 resolution:  dy = 0 deg, 0 min, 24 sec = 740 meters  (refined by 5)

    Level 4 resolution:  dy = 0 deg, 0 min, 12 sec = 370 meters  (refined by 2)

    Level 5 resolution:  dy = 0 deg, 0 min, 6 sec = 185 meters  (refined by 2)

    Level 6 resolution:  dy = 0 deg, 0 min, 3 sec = 92.5 meters  (refined by 2)

    Level 7 resolution:  dy = 0 deg, 0 min, 1 sec = 30.8333 meters  (refined by 3)

    Level 8 resolution:  dy = 0 deg, 0 min, 0.333333 sec = 10.2778 meters  (refined by 3)

    Allowing maximum of 5 levels
    Created  Domain.kml
    No regions found in setrun.py
    Region  Region_domain
    Created  Region_domain.kml
    Region  Region_dtopo
    Created  Region_dtopo.kml
    Region  Region_12sec
    Created  Region_12sec.kml
    Region  Region_3sec
    Created  Region_3sec.kml
    Region  Region_1sec
    Created  Region_1sec.kml
    Region  Region_onethird
    Created  Region_onethird.kml
    Gauge 101: x = -124.189583, y = 47.11625  
      t1 = 0.,  t2 = 1000000000.
    Gauge 102: x = -124.180417, y = 47.11625  
      t1 = 0.,  t2 = 1000000000.
    Gauge 103: x = -124.170417, y = 47.11625  
      t1 = 0.,  t2 = 1000000000.
    Created  gauges.kml
    *** Note: since grid registration is llcorner,
        will shift x,y values by (dx/2, dy/2) to cell centers
    *** Note: since grid registration is llcorner,
        will shift x,y values by (dx/2, dy/2) to cell centers
    Box:   -129.995833  -122.004167   40.004167   49.995833
    Created  etopo22_30s_-130_-122_40_50_30sec.kml
    *** Note: since grid registration is llcorner,
        will shift x,y values by (dx/2, dy/2) to cell centers
    *** Note: since grid registration is llcorner,
        will shift x,y values by (dx/2, dy/2) to cell centers
    Box:   -124.249985  -124.100077   47.050015   47.219923
    Created  Copalis_13s.kml
    Box:   -127.569034  -122.569034   44.032340   50.032340
    Created  ASCE_SIFT_Region2.kml
    touch .data

Much of this output is produced by these lines at the bottom of `setrun.py`:

    # To create kml files of inputs:
    from clawpack.geoclaw import kmltools
    kmltools.make_input_data_kmls(rundata)

which produces kml files that can be opened in Google Earth to see the
footprints of various geographical things specified in setrun, including
the computational domain, the extent of topofiles and the dtopofile, and
AMR flagregions, along with the locations of gauges.

(copalis:debug:missing_topo)=
## Missing topo or dtopo files

Make sure you acquired the topo and dtopo data needed for this example, see
[](copalis:debug:fetch_input_data).

If running `make data` gives you errors like the following:

    ### Normal stuff up until...

    Created  gauges.kml
    Traceback (most recent call last):
      File "/Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/exercise1/setrun.py", line 538, in <module>
        kmltools.make_input_data_kmls(rundata)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^

      ### many lines deleted...

      File "/Users/rjl/clawpack_src/clawpack-v5.13.1/geoclaw/src/python/geoclaw/topotools.py", line 838, in read_header
        with open(self.path, 'r') as topo_file:
             ~~~~^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: './etopo22_30s_-130_-122_40_50_30sec.asc'
    make: *** [data] Error 1

This is an indication that when trying to make the kml file corresponding to
the topo file `etopo22_30s_-130_-122_40_50_30sec.asc`, it could not find
the file (from which it needs to read the header information in order to
know the extent of its footprint).

This failed because I changed the line in `setrun.py` that specifies where
to look for topo data to:

    topodir = '.'

so it was looking in this directory instead of in `../../topo/topofiles`,
where the file is stored.

Note that it did successfully make all the `*.data` files in this directory
before trying to make the kml files, and if we look at `topo.data` we would
see:

    ### lines deleted

    '/Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/exercise1/etopo22_30s_-130_-122_40_50_30sec.asc'
       3   # topo_type

    '/Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/exercise1/Copalis_13s.asc'
       3   # topo_type

which shows the full path of the files it is looking for.  Neither one is
correct, but it throws an error and stops after trying to read the first one.

If you try to run geoclaw with `make output` before fixing this problem,
the Fortran code will run, but will simply print out an error message and then
quit without taking any time steps:

    ### lines deleted

    Reading data file: topo.data
             first 5 lines are comments and will be skipped
     Missing topography file:
        /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/exercise1/etopo22_30s_-130_-122_40_50_30sec.asc                                              
    ==> runclaw: Done executing /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/exercise1/xgeoclaw via clawutil.runclaw.py
    ==> runclaw: Output is in  /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/exercise1/_output

If you do fix the problem in `setrun.py`, you should run

    $ make data

again with the correct `setrun.py` file before running the code.

## Run the code

Once you have created the executable and the data files, you can run the
executable via:

    $ make output

This should create a directory named `_output`
(as specified in the Makefile),
copy all the `*.data` files into that directory, and then run the code from
within that directory, where all of the output files will be written.

This should produce an `_output` directory that contains all the `*.data` files
used for this run and also the files

    fort.t0000, ..., fort.t0009
    fort.q0000, ..., fort.q0009
    fort.b0000, ..., fort.b0009
    gauge00101.txt, ..., gauge00103.txt
    timing.txt, timing.csv

:::{seealso}
For information on the format of these files, see:
- [Output data styles and formats](https://www.clawpack.org/output_styles.html)
- [Gauges](https://www.clawpack.org/gauges.html)
- [Timing Statistics](https://www.clawpack.org/timing.html)
:::

:::{admonition} Todo
:class: note
Are there any problems that can arise at this stage to discuss?
:::

## Plotting the results

This directory contains a python script `setplot.py` that determines how the
output produced at each output time is plotted.

To produce a directory `_plots`
(the name is specified by `PLOTDIR` in the Makefile)
that contains png files of a set of plots, along with html files to navigate
them and also javascript animations of the plots over time, run this command:

    make plots

If this throws some sort of Python error, it may be that you do not have the
Python packages installed that are being used. For the basic plots made here,
`matplotlib` should be sufficient.

If it runs properly, it should give a lot of output as it goes along and then
end with something like:

    Point your browser to:
        file:///full/path/to/_plots/_PlotIndex.html

Open this file in your browser to view the plots.

See [](setplot_description) for an annotated version of the `setplot.py`
file in this directory that explains how these plots have been specified.

:::{seealso}
- [Using `setplot.py` to specify the desired
  plots](https://www.clawpack.org/setplot.html)
  from the general Clawpack documentation.
- [Interactive plotting with Iplotclaw](https://www.clawpack.org/plotting_python.html#interactive-plotting-with-iplotclaw)
:::

## Changing `setrun.py` and re-running the code

Now try making a change to `setrun.py`, for example to make the code run
much faster you could do a coarse-grid run by changing

    amrdata.amr_levels_max = 6

to

    amrdata.amr_levels_max = 3

If you want to save the output and/or plots from the original run before
re-running this, you could move these directories, e.g.

    $ mv _output _output_orig
    $ mv _plots _plots_orig

After changing `setrun.py`, to re-run the code you need to do:

    $ make data  # to recreate the .data files from setrun.py
    $ make output # to run the code
    $ make plots # to make the plots

Alternatively, you could simply do:

    $ make .plots

which checks dependencies and would see that it needs to re-make the `.data`
files and then run the code before making the plots.

:::{seealso}
- [Clawpack Makefiles](https://www.clawpack.org/makefiles.html) documentation
:::
