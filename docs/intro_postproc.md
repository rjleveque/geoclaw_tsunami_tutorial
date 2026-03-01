# Postprocessing and plotting GeoClaw output

## Plotting time frame output

- [Plotting with Visclaw
  documentation](https://www.clawpack.org/plotting.html) 
  is outdated and needs a lot of work!
- [Using `setplot.py`](https://www.clawpack.org/setplot.html)
- plotting on maps or satellite imagery
- Extracting transects

## Specialized gauge plots

- Better titles with quantities like max value, lat,lon, etc.
- Gotchas: discontinuities in output when AMR level changes
- Phase plane plots of flow direction

## Plotting fgmax output

- plan view
- transects
- determining initial shoreline from `B0` topography
  - may require separate GeoClaw run with no dtopo
- plotting on maps or satellite imagery

## Plotting fgout output

- Similar tools as for time frames and/or fgmax
- Making animations

## Plotting topo in 3D with PyVista

- [Some examples](https://depts.washington.edu/clawpack/dev_pyvista/)
  to accompany
  [visclaw issue #311](https://github.com/clawpack/visclaw/issues/311)

- [Some examples](https://depts.washington.edu/ptha/CopesHubTsunamis/vis3d/)
  developed for [Cascadia CoPes Hub](https://cascadiacopeshub.org/)
  research.

## Debris tracking

- As postprocessing, using velocity field from `fgout` output.

