# Copalis Beach example1

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

See [](../README) for more about the Copalis Beach location and a
list of other examples and tutorials based on this location.

The directory `$GTT/CopalisBeach/example1`
contains some initial GeoClaw `setrun` and `setplot` functions to start
exploring tsunami modeling.  See [](../README) for more about the Copalis
Beach location and a list of other examples and tutorials based on this
location.

## Sample results

:::{warning}
Work in Progress

Todo: Add `fetch_output` script to download all `_output` and `_plots`
directories?
:::

See [](results).  The shell scripts `make_example1a.sh` and `make_all.sh`
can be used to run the code and create the files needed in `sample_results`
for [rendering results.md](results).

## Contents (Work in Progress):

- `setrun1a.py`, an first pass to model on coarse grids (up to AMR level 3)
- `setrun1b.py`, a modified version to include up to AMR level 5
- `setrun1c.py`, a modified version to include up to AMR level 7
- `setrun1d.py`, a modified version to include up to AMR level 8
- `setplot.py`, to make plots of time frames and a couple gauges
- `example1a.ipynb`, a notebook illustrating timeframe results (To appear)
- `example1b.ipynb`, a notebook illustrating comparison transect plots (To
  appear)
- `Makefile1a`, a standard GeoClaw `Makefile` but using `setrun1a.py`
  and redirecting output/plots to `_output1a` / `_plots1a`.
- `Makefile1b`, `Makefile1c`, `Makefile1d`.
- `fetch_output.py` a script to fetch `_output1a` and `_output1b` from an
  online archive (rather than running the code).

## Note:

- If you want to run the code in this directory, you should copy it
  elsewhere first (see [](../../../workflow)).

- If you make any changes in the code and modify the results, then rerunning
  the notebooks may result in images that no longer match the descriptions.
  These examples are not intended to be modified.

- See [](../exercise1/README) for a version that you are encouraged to
  modify and experiment with (after copying elsewhere).

- The notebooks check if the output directories exist, and if not they
  are fetched using the `fetch_output.py` script.  This makes it possible
  to execute the notebooks without first running GeoClaw.

  This is necessary in part so that the Jupyter Book is properly built on
  Github for the version that appears on the web. (Github Actions
  are used to start up a new virtual machine, install necessary software,
  and run all the notebooks on every new push.  Clawpack is `pip installed`
  as part of this, which allows all the Python code in Clawpack to work, but
  not the Fortran code, nor is the computer time allocated in this virtual
  machine sufficient to rerun the simulations every time.)
