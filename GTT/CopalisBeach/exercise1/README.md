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
- [](setplot_description)

### To compare to the sample results

You can compare your results with the archived sample results if you first
fetch those using:

    $ python fetch_sample_results.py

Compare the plots you made in `_plots` to those in `sample_results/_plots`.


## Exercises


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

Here are some tings you might try modifying in this example:

- After copying this example elsewhere and running it, also run "make plots"
  to create a webpage of results in the new directory and check that the
  plots look the same as those in
  `$GTT/CopalisBeach/exercise1/sample_results/_plots`.
  
  Then also use the script `compare_gauges.py` to compare the gauge
  results in more detail by plotting the results from your run on top
  of the sample results.

- Try modifying the example to use a different set of AMR levels and
  refinement regions to get down to the same resolution and see how this
  affects the results and running time.  In particular, the example is set
  up to use the first 6 levels from an AMR structure with resolutions

      # dx = dy = 4', 2', 24", 12", 6", 3", 1", 1/3"

  Try modifying `refinement_ratios` so that it uses fewer levels with:

      # dx = dy = 4', 1', 12", 3", 1", 1/3"

  Modify `compare_gauges.py` to see how much this affects the solution
  at the gauges

:::{hint}
If you run compare_gauges interactively in
[IPython](https://ipython.readthedocs.io/en/stable/) via:

    $ ipython --pylab
    In [1]: run compare_gauges

then you can zoom in on the plots to see any differences more clearly.
:::

- Do more comparisons of different resolutions, refinement ratios, 
  and/or refinement flagregions.

- Add one or more new gauges in the computational domain.

- The domain used in this example does not cover very much of the ocean, not
  even the entire region of seafloor deformation defined by the
  dtopo file.  Try enlarging the computational domain to see if that changes
  the results.  (What happens if you enlarge it beyond the region covered by
  the topo files being used?
  Remember that the kml files produced by "make data" can
  help you see how the domain relates to the topo and dtopo files.)

- Try shifting this example to a different coastal region.  You may need to
  download different topo files if you move very far.

