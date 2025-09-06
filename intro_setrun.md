
# Setting up and running GeoClaw

This is a rough outline with some pointers to existing documentation and
examples.  More will be added.

See also the 
[GeoClaw documentation](https://www.clawpack.org/contents.html#geoclaw-geophysical-flows)
and [](intro_resources).

## Things to set/adjust in `setrun.py`

### Computational domain

- How large should it be? (Outflow boundaries)
- Should edges be adjusted so that cells on some fine level are aligned to
  match some desired grid?

### Choosing grid resolutions and refinement factors

- How coarse should the initial (Level 1) grid be?
- How many AMR levels are needed, what refinement factors are best?


### Topography DEMs (topofiles)

See [Topography data](https://www.clawpack.org/topo.html)

- Sources of data
- [Grid registration](https://www.clawpack.org/grid_registration.html)
- [topotools_examples notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/topotools_examples.html)

#### Adjusting background sea level

- [Setting `sea_level`](https://www.clawpack.org/sealevel.html)

### Specifying ground motion (dtopofiles)

See 
- [Moving topography displacement files](https://www.clawpack.org/dtopo.html)
- [dtopotools_examples notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/dtopotools_examples.html)
- [Okada notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/Okada.html)
- [CSZ_example notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/dtopo_triangular/CSZ_example.html)

### Refinement criteria and flagregions

- [Adaptive mesh refinement (AMR) algorithms](https://www.clawpack.org/amr_algorithm.html)
- [AMR refinement criteria](https://www.clawpack.org/refinement.html)
- [Specifying flagregions for adaptive
  refinement](https://www.clawpack.org/flagregions.html)
- Using [Ruled Rectangles](http://www.clawpack.org/ruled_rectangles.html)
  for refinement regions, e.g.
  [MakeFlagregionsCoast](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/MakeFlagregionsCoast.html)

### Duration of simulation and time between outputs

### Synthetic gauges

- [General Gauges documentation](https://www.clawpack.org/gauges.html)
- Centering gauges in grid cells

### fgmax grids to capture maxima

- [Fixed grid monitoring](https://www.clawpack.org/fgmax.html)
- Centering fgmax grid points in computational grid cells

### fgout grids for frequent output on fixed grids

- [Fixed grid output](https://www.clawpack.org/fgout.html)

## Other topics

### Bottom friction and the Manning Coefficient

- [Manning friction term](https://www.clawpack.org/manning.html)

### Initializing some land below sea level as dry

Land that is behind a dike or levee should be forced to be dry initially.
This can be done with a `force_dry` array. See 
the documentation page [Force Cells to be Dry
Initially](http://www.clawpack.org/force_dry.html) and
[this notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/ForceDry.html).


### Initializing some land above sea level as wet

A lake that is near the coast may have an initial surface elevation that is
different from `sea_level`.

### Adding river flow

## Running GeoClaw

- Using OpenMP, how many threads?
- Checkpoint files and restarts
- Sending output to a scratch directory
- Running on cluster / supercomputer with SLURM scripts
- Running dispersive (Boussinesq) code with MPI, PETSc


