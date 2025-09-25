# Annotated screen output

To run the example set up in `setrun1a.py` (which is described in detail in
[](setrun_description) and make the plots, you can execute the commands found
in `make_example1a.sh` or type the shell command

    $ source make_example1a.sh

Here's the contents of that file, the shell commands that are executed by
running the script:

    #!/bin/bash

    # clean up any old results:
    rm -rf _output1a _plots1a

    # make sure the code is compiled:
    make .exe -f Makefile1a | tee geoclaw_output1a.txt

    # create .data files (appending screen output):
    make data -f Makefile1a | tee -a geoclaw_output1a.txt

    # run GeoClaw:
    echo ==========> Running GeoClaw...
    make output -f Makefile1a | tee -a geoclaw_output1a.txt

    # plot the results:
    echo ==========> Plotting results...
    make plots -f Makefile1a | tee -a geoclaw_output1a.txt

Note that the unix `tee` command is used to both print the usual output to the
screen and capture it to a file, appending to it for each command.
A copy of this output is in the file `sample_results/geoclaw_output1a.txt`.

An annotated version of this output follows, to explain what is going on...

#### Compiling the code: `make .exe`

The code

    # make sure the code is compiled:
    make .exe -f Makefile1a | tee geoclaw_output1a.txt

produces:


    make: Nothing to be done for `.exe'.

:::{note}
Nothing is done by `make .exe` since the code was previously compiled when I
ran this.
:::

#### Creating the data files: `make .data`

The code

    # create .data files (appending screen output):
    make data -f Makefile1a | tee -a geoclaw_output1a.txt

forces recreation of the `.data` files based on `setrun1a.py` (as specified
in `Makefile1a`, and produces:

    rm -f .data
    python setrun1a.py              geoclaw                  
    Domain:   -128.500000  -123.500000   45.000000   49.000000
    Level 1 resolution:  dy = 0 deg, 4 min, 0 sec = 7400 meters

    Level 2 resolution:  dy = 0 deg, 2 min, 0 sec = 3700 meters  (refined by 2)

    Level 3 resolution:  dy = 0 deg, 0 min, 24 sec = 740 meters  (refined by 5)

    Level 4 resolution:  dy = 0 deg, 0 min, 12 sec = 370 meters  (refined by 2)

    Level 5 resolution:  dy = 0 deg, 0 min, 6 sec = 185 meters  (refined by 2)

    Level 6 resolution:  dy = 0 deg, 0 min, 3 sec = 92.5 meters  (refined by 2)

    Level 7 resolution:  dy = 0 deg, 0 min, 1 sec = 30.8333 meters  (refined by 3)

    Level 8 resolution:  dy = 0 deg, 0 min, 0.333333 sec = 10.2778 meters  (refined by 3)

    Allowing maximum of 3 levels
    Created  Domain.kml
    No regions found in setrun.py
    Region  Region_domain
    Created  Region_domain.kml
    Region  Region_12sec
    Created  Region_12sec.kml
    Gauge 101: x = -124.19, y = 47.116  
      t1 = 0.,  t2 = 1000000000.
    Gauge 102: x = -124.18, y = 47.116  
      t1 = 0.,  t2 = 1000000000.
    Gauge 103: x = -124.17, y = 47.116  
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

:::{note}
Some things were printed out above from the `make data` command.
:::

#### Running the GeoClaw executable: `make output`

Next it starts running the compiled GeoClaw Fortran code...

The code

    make output -f Makefile1a | tee -a geoclaw_output1a.txt

produces:

    rm -f .output
    python /Users/rjl/git/clawpack/clawutil/src/python/clawutil/runclaw.py xgeoclaw _output1a                     \
        True None . False False None
    Reading data file: claw.data
             first 5 lines are comments and will be skipped
    Reading data file: amr.data
             first 5 lines are comments and will be skipped

     Running amrclaw ...  

    Reading data file: geoclaw.data
             first 5 lines are comments and will be skipped
    Reading data file: refinement.data
             first 5 lines are comments and will be skipped
    Reading data file: dtopo.data
             first 5 lines are comments and will be skipped
    Reading data file: topo.data
             first 5 lines are comments and will be skipped
     *** in file: /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc
         Shifting xllcorner by 0.5*dx to cell center
     *** in file: /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc
         Shifting yllcorner by 0.5*dy to cell center
     *** in file: /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/topo/topofiles/Copalis_13s.asc
         Shifting xllcorner by 0.5*dx to cell center
     *** in file: /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/topo/topofiles/Copalis_13s.asc
         Shifting yllcorner by 0.5*dy to cell center

     Reading topography file  /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc                                                      

     Reading topography file  /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/topo/topofiles/Copalis_13s.asc                                                                            
    Reading data file: qinit.data
             first 5 lines are comments and will be skipped
       qinit_type = 0, no perturbation
    Reading data file: fgout_grids.data
             first 5 lines are comments and will be skipped
    Reading data file: friction.data
             first 5 lines are comments and will be skipped
    Reading data file: multilayer.data
             first 5 lines are comments and will be skipped
    Reading data file: surge.data
             first 5 lines are comments and will be skipped
    Reading data file: regions.data
             first 5 lines are comments and will be skipped
    Reading data file: flagregions.data
             first 5 lines are comments and will be skipped
     +++ rregion bounding box:
      -128.69999999999999       -123.30000000000000        44.799999999999997        49.200000000000003     
     +++ i, rr%s(1), rr%ds:            1  -128.69999999999999        5.3999999999999915     
     +++ rregion bounding box:
      -126.59999999999999       -124.00000000000000        46.270000000000003        47.680000000000000     
     +++ i, rr%s(1), rr%ds:            2  -126.59999999999999        2.5999999999999943     
    Reading data file: gauges.data
             first 5 lines are comments and will be skipped
    Reading data file: fgmax_grids.data
             first 5 lines are comments and will be skipped
    Reading data file: adjoint.data
             first 5 lines are comments and will be skipped
     rnode allocated...
     node allocated...
     listOfGrids allocated...
     Storage allocated...
     bndList allocated...
    Gridding level   1 at t =  0.000000E+00:     4 grids with        4500 cells
    Gridding level   2 at t =  0.000000E+00:     2 grids with        4576 cells
    Gridding level   3 at t =  0.000000E+00:    56 grids with       96350 cells
       Setting initial dt to   0.20000000000000001     
      max threads set to            6

     Done reading data, starting computation ...  

     Total mass at initial time:    265457917005868.75     


:::{note}
It's done reading in all the topo and dtopo files.
For historical reasons the code prints out the total mass of water in the
domain, which is a bit silly for ocean-scale tsunami modeling
(it's in cubic meters).

Next it runs the code. There is a line printed every time a frame of output
data (the full AMR solution) is written to the output directory. For this run a
line is also printed for every time step on every grid level (because we set
`verbosity = 3`,  and also every time regridding
happens at every level, because `verbosity_regrid = 3`.
See [](setrun_description) for discussion of these parameters and others
mentioned below.

:::

    GEOCLAW: Frame    0 output files done at time t =  0.000000D+00

     AMRCLAW: level  1  CFL = .653E-02  dt = 0.2000E+00  final t = 0.200000E+00
     AMRCLAW: level  2  CFL = .129E-01  dt = 0.2000E+00  final t = 0.200000E+00
     AMRCLAW: level  3  CFL = .653E-01  dt = 0.2000E+00  final t = 0.200000E+00
     AMRCLAW: level  1  CFL = .653E-02  dt = 0.2000E+00  final t = 0.400000E+00
     AMRCLAW: level  2  CFL = .129E-01  dt = 0.2000E+00  final t = 0.400000E+00
     AMRCLAW: level  3  CFL = .653E-01  dt = 0.2000E+00  final t = 0.400000E+00
     AMRCLAW: level  1  CFL = .653E-02  dt = 0.2000E+00  final t = 0.600000E+00
     AMRCLAW: level  2  CFL = .129E-01  dt = 0.2000E+00  final t = 0.600000E+00
     AMRCLAW: level  3  CFL = .653E-01  dt = 0.2000E+00  final t = 0.600000E+00
    Regridding level   2 at t =  0.600000E+00:     8 grids with       12960 cells
    Regridding level   3 at t =  0.600000E+00:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .653E-02  dt = 0.2000E+00  final t = 0.800000E+00
     AMRCLAW: level  2  CFL = .130E-01  dt = 0.2000E+00  final t = 0.800000E+00
     AMRCLAW: level  3  CFL = .653E-01  dt = 0.2000E+00  final t = 0.800000E+00
     AMRCLAW: level  1  CFL = .653E-02  dt = 0.2000E+00  final t = 0.100000E+01
     AMRCLAW: level  2  CFL = .130E-01  dt = 0.2000E+00  final t = 0.100000E+01
     AMRCLAW: level  3  CFL = .653E-01  dt = 0.2000E+00  final t = 0.100000E+01
     AMRCLAW: level  1  CFL = .653E-02  dt = 0.2000E+00  final t = 0.120000E+01
     AMRCLAW: level  2  CFL = .130E-01  dt = 0.2000E+00  final t = 0.120000E+01
     AMRCLAW: level  3  CFL = .653E-01  dt = 0.2000E+00  final t = 0.120000E+01
    Regridding level   2 at t =  0.120000E+01:    16 grids with       15120 cells
    Regridding level   3 at t =  0.120000E+01:    56 grids with       96350 cells


:::{note}
Note that initially it took time steps of 0.2 seconds up to time 1.2 seconds.
This is because the dtopo file specifies an instanteous uplift event at time 1
second.  Because the time step was forced to be so small on level 1, the same
time step also works on levels 2 and 3 (the CFL condition is satisfied for
stability), and so each level 1 step is followed by a single Level 2 step and a
single Level 3 step.

After time 1.2, it is allowed to increase the time step on Level 1, based on
the specified `cfl_desired`.  The time step chosen is about 26 seconds.

When refining to level 2, you might expect the time step to be cut down by
a factor 2 since that is the refinement ratio in `x,y,t` specified in
`setrun1a.py`.  However, since

    refinement_data.variable_dt_refinement_ratios = True

it is allowed to choose the time step based on CFL and it chooses to refine
by 3, and so every Level 1 time step is followed by 3 Level 2 timesteps before
the next Level 1 step.

In refining to Level 3, the specified refinement factor is 5 but note that it
only has to refine in time by a factor of 4 due to the fact that the Level 2
time step was smaller than necessary.  So there are 4 Level 3 steps between
each Level 2 step in the output below.

Note that the total refinement in
time from Level 1 to 3 is `3*4 = 12`, whereas we might have expected
`2*5 = 10`.  This is still stable, but means it is taking 12 Level 3 steps
for each Level 1 step rather than only 10.
(*Something we need to investigate in Geoclaw!*)
:::

     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.272148E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.987161E+01
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.336790E+01
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.553581E+01
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.770371E+01
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.987161E+01
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.185432E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.120395E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.142074E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.163753E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.185432E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.272148E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.207111E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.228790E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.250469E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.272148E+02
    Regridding level   3 at t =  0.272148E+02:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.532297E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.358865E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.293827E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.315507E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.337186E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.358865E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.445581E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.380544E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.402223E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.423902E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.445581E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.532297E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.467260E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.488939E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.510618E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.532297E+02
    Regridding level   3 at t =  0.532297E+02:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.792443E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.619012E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.553976E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.575655E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.597333E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.619012E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.705728E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.640691E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.662370E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.684049E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.705728E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.792443E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.727407E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.749085E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.770764E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.792443E+02
    Regridding level   2 at t =  0.792443E+02:    16 grids with       14640 cells
    Regridding level   3 at t =  0.792443E+02:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.105259E+03
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.879158E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.814122E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.835801E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.857479E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.879158E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.965873E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.900837E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.922516E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.944195E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.965873E+02
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.105259E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.987552E+02
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.100923E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.103091E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.105259E+03
    Regridding level   3 at t =  0.105259E+03:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.131273E+03
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.113930E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.107427E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.109595E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.111762E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.113930E+03
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.122602E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.116098E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.118266E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.120434E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.122602E+03
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.131273E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.124770E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.126938E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.129106E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.131273E+03
    Regridding level   3 at t =  0.131273E+03:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.157288E+03
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.139945E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.133441E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.135609E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.137777E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.139945E+03
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.148616E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.142113E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.144281E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.146449E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.148616E+03
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8672E+01  final t = 0.157288E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.150784E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.152952E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.155120E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.157288E+03
    Regridding level   2 at t =  0.157288E+03:    16 grids with       14400 cells
    Regridding level   3 at t =  0.157288E+03:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.183302E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8672E+01  final t = 0.165959E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.159456E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.161624E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.163792E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.165959E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8672E+01  final t = 0.174631E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.168127E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.170295E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.172463E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.174631E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8672E+01  final t = 0.183302E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.176799E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.178967E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.181135E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.183302E+03
    Regridding level   3 at t =  0.183302E+03:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.209317E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8671E+01  final t = 0.191974E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.185470E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.187638E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.189806E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.191974E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8671E+01  final t = 0.200645E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.194142E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.196310E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.198478E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.200645E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8671E+01  final t = 0.209317E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.202813E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.204981E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.207149E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.209317E+03
    Regridding level   3 at t =  0.209317E+03:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.235331E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8671E+01  final t = 0.217988E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.211485E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.213653E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.215821E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.217988E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8671E+01  final t = 0.226660E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.220156E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.222324E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.224492E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.226660E+03
     AMRCLAW: level  2  CFL = .568E+00  dt = 0.8671E+01  final t = 0.235331E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.228828E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.230996E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.233163E+03
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2168E+01  final t = 0.235331E+03
    Regridding level   2 at t =  0.235331E+03:    16 grids with       14880 cells
    Regridding level   3 at t =  0.235331E+03:    56 grids with       96350 cells


:::{note}
Note above how often the regridding is done on each level.
:::

:::{warning}
The calculation continues in the same manner and prints lots more output.
Roughly 3500 lines of output have been deleted here.
:::

:::{note}
Here are the last few time steps....

Note that in order to hit an output time exactly (in this case the final time
of 90 minutes), the time steps on all levels must typically be
decreased a bit in the final step.
:::

     AMRCLAW: level  1  CFL = .850E+00  dt = 0.2601E+02  final t = 0.539824E+04
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8670E+01  final t = 0.538090E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.537439E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.537656E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.537873E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.538090E+04
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8670E+01  final t = 0.538957E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.538306E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.538523E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.538740E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.538957E+04
     AMRCLAW: level  2  CFL = .573E+00  dt = 0.8670E+01  final t = 0.539824E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.539173E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.539390E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.539607E+04
     AMRCLAW: level  3  CFL = .708E+00  dt = 0.2167E+01  final t = 0.539824E+04
    Regridding level   3 at t =  0.539824E+04:    56 grids with       96350 cells
     AMRCLAW: level  1  CFL = .577E-01  dt = 0.1765E+01  final t = 0.540000E+04
     AMRCLAW: level  2  CFL = .389E-01  dt = 0.5882E+00  final t = 0.539882E+04
     AMRCLAW: level  3  CFL = .192E+00  dt = 0.5882E+00  final t = 0.539882E+04
     AMRCLAW: level  2  CFL = .389E-01  dt = 0.5882E+00  final t = 0.539941E+04
     AMRCLAW: level  3  CFL = .192E+00  dt = 0.5882E+00  final t = 0.539941E+04
     AMRCLAW: level  2  CFL = .389E-01  dt = 0.5882E+00  final t = 0.540000E+04
     AMRCLAW: level  3  CFL = .192E+00  dt = 0.5882E+00  final t = 0.540000E+04
    GEOCLAW: Frame    9 output files done at time t =  0.540000D+04

     Done integrating to time    5400.0000000000000     
    See fort.amr for more info on this run and memory usage

:::{note}
After it finishes, it prints out some timing information that is also
always written to a file `timing.txt` in the output directory.
There is also a file `timing.csv` that gives cumulative timings up to each
output time.
:::

    ============================== Timing Data ==============================

    Integration Time (stepgrid + BC + overhead)
    Level           Wall Time (seconds)    CPU Time (seconds)   Total Cell Updates
      1                     1.241                  2.421            0.999E+06
      2                     2.448                  9.375            0.115E+08
      3                    29.638                166.353            0.243E+09
    total                  33.328                178.149            0.255E+09

    All levels:
    stepgrid               32.586                176.159    
    BC/ghost cells          0.400                  1.638
    Regridding              1.049                  2.409  
    Output (valout)         0.050                  0.048  

    Total time:            34.591                180.979  
    Using  6 thread(s)

    Note: The CPU times are summed over all threads.
          Total time includes more than the subroutines listed above
    Note: timings are also recorded for each output step
          in the file timing.csv.

    =========================================================================


#### Making plots:  `make .plots`


Next the plots are made.  All of the Makefiles in this directory reference the
same `setplot.py`, so each of the four examples produces the same set of plots
(but with different simulation output).

The code

    make plots -f Makefile1a | tee -a geoclaw_output1a.txt

produces:

    rm -f .plots
    python /Users/rjl/git/clawpack/visclaw/src/python/visclaw/plotclaw.py _output1a                     _plots1a                     setplot.py             
    Importing setplot.setplot from /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1.
    Executed setplot successfully
        Reading  Frame 4 at t = 2400  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 4
    Importing setplot.setplot from /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1.
    Executed setplot successfully
        Reading  Frame 5 at t = 3000  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 5
    Importing setplot.setplot from /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1.
    Executed setplot successfully
        Reading  Frame 0 at t = 0  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 0
        Reading  Frame 6 at t = 3600  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 6
    Importing setplot.setplot from /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1.
    Executed setplot successfully
        Reading  Frame 1 at t = 600  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 1
        Reading  Frame 7 at t = 4200  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 7
    Importing setplot.setplot from /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1.
    Executed setplot successfully
        Reading  Frame 2 at t = 1200  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 2
        Reading  Frame 8 at t = 4800  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 8
    Importing setplot.setplot from /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1.
    Executed setplot successfully
        Reading  Frame 3 at t = 1800  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 3
        Reading  Frame 9 at t = 5400  from outdir = /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Creating png for Frame 9
    Importing setplot.setplot from /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1.
    Executed setplot successfully
    *** Warning: No fort.q or claw.pkl files found in directory  /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_output1a
    Will plot 10 frames numbered: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Will make 2 figure(s) for each frame, numbered:  [0, 1]

    -----------------------------------


    Creating html pages for figures...

    Directory '/Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a'
        already exists, files may be overwritten
    Created /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/timing_figures/timing_CumCellUpdates.png
    Created /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/timing_figures/timing_CumCPUTime.png
    Created /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/timing_figures/timing_CumWallTime.png
    Created /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/timing_figures/timing_ByFrameCellUpdates.png
    Created /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/timing_figures/timing_ByFrameCPUTime.png
    Created /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/timing_figures/timing_ByFrameWallTime.png
    Created /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/timing_figures/timing_ByFrameCellUpdatesPerCPU.png
    Created /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/timing_figures/timing.html
    Now making png files for all figures...
    Read in gauge 101.
    Found data for Gauge 101
    Read in gauge 102.
    Found data for Gauge 102
    Read in gauge 103.
    Found data for Gauge 103

    -----------------------------------

    Creating latex file...
    Directory '/Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a'
        already exists, files may be overwritten

    Latex file created:  
      /Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/plots.tex

    Use pdflatex to create pdf file
    2025-09-14 15:34:27,032 INFO CLAW: Animation.save using <class 'matplotlib.animation.FFMpegWriter'>
    2025-09-14 15:34:27,032 INFO CLAW: MovieWriter._run: running command: ffmpeg -f rawvideo -vcodec rawvideo -s 700x700 -pix_fmt rgba -framerate 5 -loglevel error -i pipe: -vcodec h264 -pix_fmt yuv420p -y movie_fig0.mp4
    Created movie_fig0.mp4
    2025-09-14 15:34:27,452 INFO CLAW: Animation.save using <class 'matplotlib.animation.HTMLWriter'>
    Created movie_fig0.html
    2025-09-14 15:34:27,945 INFO CLAW: Animation.save using <class 'matplotlib.animation.FFMpegWriter'>
    2025-09-14 15:34:27,945 INFO CLAW: MovieWriter._run: running command: ffmpeg -f rawvideo -vcodec rawvideo -s 800x600 -pix_fmt rgba -framerate 5 -loglevel error -i pipe: -vcodec h264 -pix_fmt yuv420p -y movie_fig1.mp4
    Created movie_fig1.mp4
    2025-09-14 15:34:28,386 INFO CLAW: Animation.save using <class 'matplotlib.animation.HTMLWriter'>
    Created movie_fig1.html

    --------------------------------------------------------

    Point your browser to:
        file:///Users/rjl/git/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/_plots1a/_PlotIndex.html
