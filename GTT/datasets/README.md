
(datasets)=
# Fetching data and results

The `geoclaw_tsunami_tutorial/GTT/datasets` directory contains this
description of how large datasets (both input data and sample results)
are handled in the tutorials, as well as a few simple examples,
used mostly for testing purposes at the moment.

Using GeoClaw on a realistic problem often requires large data files as input,
e.g. topo files with the topography DEMs and dtopo files prescribing earthquake
motion.  These data files are not included in the Github repository but must be
downloaded separately in order to run the codes.  Often these can be downloaded
directly from the NCEI server or other existing code repositories, but in some
cases may be stored on the geoclaw server.  There are some notebooks included
in the tutorial that will download and save these files (or even cropped and
coarsened versions, as in the notebook [](../topo/CopalisTopo)).  In some cases
a script `fetch_input_data.py` is included in examples to fetch the required
input data.

Some of the examples also have a script `fetch_sample_results.py` that fetches
a subdirectory `sample_results` with examples of what should be produced by
running the GeoClaw code, often the plots that result from also doing `make
plots` or running other postprocessing scripts.  There are two reasons for
providing sample results:

- Some examples take hours to run and you may want to be able to explore the
  results without having to run the code.

- Building the Jupyter Book (i.e. converting a markdown file like
  `$CLAW/datasets/README.md` into the html version that you are now reading)
  is done on Github every time a change to these tutorials is pushed.
  If the resulting webpage should have figures that illustrate the results
  being discussed (such as [](../CopalisBeach/example1/results)), then those plots
  need to be available on the computer building the html. Downloading the
  `sample_results` directory is done directly from a code cell at the top
  of the file `$GTT/CopalisBeach/example1/results.md` that executes
  `$GTT/CopalisBeach/example1/fetch_sample_results.py`.


## The data repository and cache

The top level of this repository `geoclaw_tsunami_tutorial` contains a
subdirectory `GTT` (which is where `$GTT` points, if you followed the
[](workflow).  It also contains subdirectories `$GTT_data_repository` and
`GTT_cache`.  The directory `$GTT_data_repository` is nearly empty and just
contains some tools for building the remote repository, which you can ignore.
It also contains a file `$GTT_data_repository/registry.txt` that
contains a list of data files or directories that can be fetched
from the remote repository, along with a hash of the zip file of each, used to
check if you have the most recent version.

This repository `geoclaw_tsunami_tutorial` also contains a 
subdirectory `GTT_cache` that is populated by zip files of the large data sets
as they are fetched from the remote repository.  You should not need to directly
work with files in the directory and if you are trying to clean up the space
being used, you could remove its contents with no adverse effects.

A script like `$GTT/CopalisBeach/example1/fetch_sample_results.py` gives a
list of files or directories to download (in this case only `sample_results`)
and then uses tools in the module `$GTT/common_code/GTT_tools.py`
to fetch the zip file from the online repository and store it in `GTT_cache`
(with the same subdirectory structure as in `GTT`).
It also unzips the file and puts the resulting `sample_results` directory
in the proper location in `GTT`.

:::{admonition} Todo
:class: note
- Describe hash codes and updating in more detail.
- Use of [pooch](https://www.fatiando.org/pooch/dev/index.html).
- Problem: The hash of a zip file can change even when the data in it that
  we care about does not (since the zip file also contains some metadata
  such as when it was created?)  This is annoying.
- It would be nice to just use rsync, which would manage updating,
  compressing, keeping track of hashes, etc.  But users can't use without
  login or ssh keys.   Or put the data
  repository on a server with an rsync daemon running??
- Could alternatively use a git submodule to store all the data? But the
  it gets versioned and grows in size if changes are made,  large files are
  always downloaded even for examples not run, etc.
- Are there better ways? E.g. some version of ["Git for
  data"](https://www.dolthub.com/blog/2020-03-06-so-you-want-git-for-data/)?
- Some other possibilities:
  - [cloudpathlib](https://cloudpathlib.drivendata.org/stable/caching/)
  - xarray uses a separate github data repository
    [xarray-data](https://github.com/pydata/xarray-data)
    with a [load_dataset function](https://docs.xarray.dev/en/latest/generated/xarray.tutorial.load_dataset.html)
:::

