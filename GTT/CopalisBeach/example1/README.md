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

## Contents (Work in Progress):

- `setrun1.py`, an first pass to model on coarse grids, which runs quickly.
- `setrun2.py`, a modified version to include finer level grids
- `setplot.py`, to make plots of time frames and a couple gauges
- `example1a.ipynb`, a notebook illustrating timeframe results
- `example1b.ipynb`, a notebook illustrating comparison transect plots
- `Makefile`, a standard GeoClaw `Makefile` but with a new target added so
  `make examples` runs both versions and makes output directories
  `_output1` and `_output2`. 
- `fetch_output.py` a script to fetch `_output1` and `_output2` from an
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
