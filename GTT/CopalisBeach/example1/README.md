# Copalis Beach example1

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

See [](../README) for more about the Copalis Beach location and a
list of other examples and tutorials based on this location.

This directory `$GTT/CopalisBeach/example1`
contains some initial GeoClaw `setrun` and `setplot` functions to start
exploring tsunami modeling.  See [](../README) for more about the Copalis
Beach location and a list of other examples and tutorials based on this
location.

## Contents (Work in Progress):

- `setrun1a.py`, an first pass to model on coarse grids (up to AMR level 3)
- `setrun1b.py`, a modified version to include up to AMR level 5
- `setrun1c.py`, a modified version to include up to AMR level 7
- `setrun1d.py`, a modified version to include up to AMR level 8
- `setplot.py`, to make plots of time frames and a couple gauges
- `more_plots.ipynb`, a notebook illustrating comparison transect and
  gauge plots (To appear)
- `Makefile1a`, a standard GeoClaw `Makefile` but using `setrun1a.py`
  and redirecting output/plots to `_output1a` / `_plots1a`.
- There are similar `Makefile1b`, `Makefile1c`, `Makefile1d` files
- `fetch_sample_results.ipynb` a notebook to fetch the `sample_results`
  directory (which includes the 4 `_plots` directories) from
  an online data repository (so you can view them without running the code).


## Sample results

See [](results) for some sample results from the 4 runs set up by the
different `setrun.py` scripts in this directory, with some discussion of
what is seen.

To obtain the full `_plots` directory created by each run, you could
run all the simulations following the instructions below.
Alternatively, you can quickly fetch archived versions of the plots that result
from all 4 examples via:

    $ python fetch_sample_results.py

or run the notebook `fetch_sample_results.ipynb`, [](fetch_sample_results),
which explains what is happening when sample results are fetched,
and why this notebook is required for building the Jupyter book version
of this page (for those interested).


## Running the code

:::{note}
- If you want to run the code in this directory, you should copy it
  elsewhere first (see [](workflow:copy)).

- If you make any changes in the code and modify the results, then rerunning
  the notebooks may result in images that no longer match the descriptions
  given on these pages.  These examples are not intended to be modified.

- See [](../exercise1/README) for a version that you are encouraged to
  modify and experiment with (after copying elsewhere).
:::

If you want to run the simulations included in this example, you will need
to either create or download the topo and dtopo files that are used as input.
See [](copalis:input) for instructions.

Once  you have the required input files, the
shell scripts `make_example1a.sh` and `make_all.sh`
can be used to run the code and make plots for all these examples.
Run these via e.g.

    $ source make_example1a.sh


:::{tip}
The path to the topo and dtopo files is specified in the `setrun` function,
in terms of the environment variable `$GTT`.  After doing

    $ make data -f Makefile1a

the full paths will be visible in the `topo.data` and `dtopo.data` files.
If `make data` fails because it does not find one of these files while trying
to create kml files, check the path of the file it says is missing.
If you ran the notebooks above, check to see where it is putting the files.
If you ran the `fetch_input_data.py`, that should also have told you where it
put the files.
:::
