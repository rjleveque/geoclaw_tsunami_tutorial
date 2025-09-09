
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

- [Topography data documentation](https://www.clawpack.org/topo.html)
- [Sources of data](https://www.clawpack.org/tsunamidata.html) (needs
  updating)
- [Grid registration documentation](https://www.clawpack.org/grid_registration.html)
- [topotools_examples notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/topotools_examples.html)
- [Topography file ordering
  documentation](https://www.clawpack.org/topo_order.html)

#### Adjusting background sea level

- Relation to vertical datum of the topography files.
- Choice of tide level for simulation(s), e.g. MHW is often used for
  modeling onshore inundation, MLW for modeling drawdown in marinas.
- Incorporating future sea level projections.
- [Setting `sea_level` documentation](https://www.clawpack.org/sealevel.html)
- How `sea_level` is adjusted by ground deformation for initializing water level
  on fine grids, see 
  [Set Eta Init documentation](https://www.clawpack.org/set_eta_init.html)

### Specifying ground motion (dtopofiles)

- Coastal subsidence / uplift
- Choice of `dtopo_data.dt_max_dtopo` for static vs. kinematic sources
- [dtopo file documentation](https://www.clawpack.org/dtopo.html)
- [dtopotools_examples notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/dtopotools_examples.html)
- [Okada notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/Okada.html)
- [CSZ_example notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/dtopo_triangular/CSZ_example.html)

### Refinement criteria and flagregions

- Finite volume methods, cell-averaged values, and consistency between levels
- [Adaptive mesh refinement (AMR) algorithms documentation](https://www.clawpack.org/amr_algorithm.html)
- [AMR refinement criteria documentation](https://www.clawpack.org/refinement.html)
- [Specifying flagregions for adaptive
  refinement documentation](https://www.clawpack.org/flagregions.html)
- Using [Ruled Rectangles](http://www.clawpack.org/ruled_rectangles.html)
  for refinement regions, e.g.
  [MakeFlagregionsCoast notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/MakeFlagregionsCoast.html)

### Duration of simulation and time between outputs

- Size of output files, `ascii` vs `binary` output
- Time frame output (full AMR solution) vs. `fgout` output (on fixed grids)
- Choice of Courant number, `cfl_desired`

### Synthetic gauges

- Centering gauges in grid cells
- Capturing pre-seismic and/or final topography at gauge points
- When to turn gauges on
- [General Gauges documentation](https://www.clawpack.org/gauges.html)

### fgmax grids to capture maxima

- Centering fgmax grid points in computational grid cells
- What levels to monitor, when to turn on
- Capturing pre-seismic and/or final topography at grid points
- [Fixed grid monitoring documentation](https://www.clawpack.org/fgmax.html)

### fgout grids for frequent output on fixed grids

- [Fixed grid output documentation](https://www.clawpack.org/fgout.html)

### Bottom friction and the Manning Coefficient

- [Manning friction term documentation](https://www.clawpack.org/manning.html)


## Other topics

### Initializing some land below sea level as dry

Land that is behind a dike or levee should be forced to be dry initially.
This can be done with a `force_dry` array.

- [Force Cells to be Dry Initially documentation](http://www.clawpack.org/force_dry.html)
- [Force Cells to be Dry Initially notebook](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/ForceDry.html).


### Initializing some land above sea level as wet

A lake that is near the coast may have an initial surface elevation that is
different from `sea_level`.

- Modifying `set_eta_init.f90` to change `sea_level` over specified region.
- [Set Eta Init documentation](https://www.clawpack.org/set_eta_init.html)
- See the sample code commented out in the 
  [default set_eta_init.f90](https://github.com/clawpack/geoclaw/blob/master/src/2d/shallow/set_eta_init.f90)
- Modifying `Makefile` to used your version of this Fortran code, see
  [Makefile documentation](https://www.clawpack.org/makefiles_library.html#replacing-files-with-the-same-name-as-library-files)

### Adding river flow, precipitation, overland flooding

- [Sample results for Quillayute River flooding
  notebook](https://depts.washington.edu/clawpack/geoclaw/geoclaw_tutorial_csdms2024/quillayute/ViewPlotsQuillayute.html) 
  from
  [Tutorial from CSDMS 2024](https://github.com/clawpack/geoclaw_tutorial_csdms2024)

### Landslide generated tsunamis

- [Landslides documentation](https://www.clawpack.org/landslides.html)
- Need for dispersive modeling, see
  [Boussinesq solver documentation](https://www.clawpack.org/bouss2d.html)

## Running GeoClaw

### Using OpenMP, how many threads?

- See [Using OpenMP documentation](https://www.clawpack.org/openmp.html)

### Checkpoint files and restarts

- See [Checkpointing and restarting
  documentation](https://www.clawpack.org/restart.html)

### Running on cluster / supercomputer 

- Sending output to a scratch directory
- SLURM scripts
- Running [dispersive (Boussinesq)
  code](https://www.clawpack.org/bouss2d.html) with MPI, PETSc on TACC


