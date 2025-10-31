# Copalis Beach exercise1

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

See [](../README) for more about the Copalis Beach location and a
list of other examples and tutorials based on this location.

The directory `$GTT/CopalisBeach/exercise1`
contains bare bones GeoClaw `setrun` and `setplot` functions
similar to those used for example 1b in [](../example1/README).

:::{warning}
If you want to run the code in this directory, you should copy it
elsewhere first (see [](workflow:copy)).
:::

## To run this code

You should first try running this code as-is.  


## Exercises (Work in Progress):

A list of things to try doing, which will require adapting some code from
[](../example2/README).

:::{warning}
Do not run the code in this directory.
You should copy this directory to your own working directory `$MYGTT`,
as explained in [](workflow:copy), and then make modifications.
Otherwise you may run into merge conflicts when you try to update the
tutorial repository with a `git pull`!

You may want to make several copies of this directory to experiment with
different modifications.
:::

Some ideas (WIP)...
- Add gauges at the following locations: ...
- Add an fgmax grid over some different region than in `example2`.
  Create plots on suitable backgroud images.
- Create transect plots of time frame and/or fgmax results.
- Add an fgout grid and make animations.
- Compare different resolutions and/or refinement regions.
- Leave out some topofile(s) and see how this affects the results.
- Replace the `ASCE_SIFT_Region2` dtopo with a different CSZ earthquake
  source. E.g. L1, CoPes Hub groundmotions, fakequakes, etc.
- Make comparison plots for different resolutions or sources.
- Etc.
