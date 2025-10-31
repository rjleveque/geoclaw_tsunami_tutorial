(copalis_debug)=
# Debugging the Copalis example code

:::{warning}
If you want to run the code in this directory, you should copy it
elsewhere first (see [](workflow:copy)).
:::

Before running the code in this directory, you should make sure the following
environment variables are set:

- `CLAW` should point to the top level of the `clawpack` repository code.
- `PYTHONPATH` should include `$CLAW` (maybe other paths too, separated by `:`)
- `FC, FFLAGS, OMP_NUM_THREADS` could be set, or else values in the Makefile
  are used (see [](makefile_description)).

Then try doing this at the command line:

    $ make check

This prints out the values of several variables.  You should see something like:

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

## make data

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
    
