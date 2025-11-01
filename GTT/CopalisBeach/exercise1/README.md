# Copalis Beach exercise1

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

See [](../README) for more about the Copalis Beach location and a
list of other examples and tutorials based on this location.

The directory `$GTT/CopalisBeach/exercise1`
contains GeoClaw `setrun` and `setplot` functions
similar to those used for example 1b in [](../example1/README), with the
following changes:

- There is only one `Makefile` that specifies `OUTDIR = _output` and
  `PLOTDIR = _plots`.
- There is only one `setrun.py` that specifies

        clawdata.num_output_times = 6
        clawdata.tfinal = 1.0*3600.

        amrdata.amr_levels_max = 6

  So it is only refining to Level 6 (3 arcsecond) and only running out to
  one hour of simulated time.


## To run this code

You should first try running this code as-is.  If you have problems with
this, please see the following pages:

- [](debug)
- [](makefile_description)


## Exercises (Work in Progress):

A list of things to try doing, which will require adapting some code from
[](../example2/README).

:::{warning}
Do not modify the code in this directory.
You should copy this directory to your own working directory `$MYGTT`,
as explained in [](workflow:copy), and then make modifications.
Otherwise you may run into merge conflicts when you try to update the
tutorial repository with a `git pull`!

You may want to make several copies of this directory to experiment with
different modifications.

If you run into problems running the code after moving it, see the suggestions
in [](debug).
:::

Some ideas (WIP)...
- Add gauges at the following locations: ...
- Compare different resolutions and/or refinement regions.
- Leave out some topofile(s) and see how this affects the results.
- Replace the `ASCE_SIFT_Region2` dtopo with a different CSZ earthquake
  source. E.g. L1, CoPes Hub groundmotions, fakequakes, etc.
- Make comparison plots for different resolutions or sources.
- Etc.
