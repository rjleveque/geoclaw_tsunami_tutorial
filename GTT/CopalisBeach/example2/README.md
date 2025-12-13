(copalis_example2)=
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

First read [](fg_intro) for a general introduction to fgout and fgmax grids,
and an annotated version of the additions to `setrun.py` needed to specify
these grids.

:::{seealso}

**To plot fgmax results:**

- [](fgmax_results): Discussion of ways to plot fgmax results,
- [](plot_fgmax): notebook to plot fgmax results,
- `make_fgmax_kmz.py`: script to make a kmz file showing fgmax results,
- [](plot_fgmax_folium): notebook to plot fgmax results on an interactive
  map,

**To plot fgout results:**

- [](fgout_results): Discussion of ways to plot fgout results,
- [](plot_fgout): notebook to plot fgout results,
- `make_fgout_animation.py`: script to make an animation of fgout results.
- `fetch_sample_results.py`: fetch `_outdir` containing results needed
  for running the above. (Or `make .output` should run GeoClaw to create
  these results.)


The `fetch_sample_results.py` scripts also fetches these sample results:

- `sample_results/CopalisBeach_ASCE_SIFT_fgmax1.kmz`: kmz file created by
  `make_fgmax_kmz.py` (open in Google Earth or other GIS platform)
- `sample_results/folium_map_with_max_depth.html`: html file created
  by [](plot_fgmax_folium).
- `sample_results/fgout_animation.mp4`: Animation created by
  `make_fgout_animation.py`

:::


