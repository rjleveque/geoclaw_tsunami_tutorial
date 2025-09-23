# Testing GeoClaw -- chile2010

The GeoClaw distribution includes a few examples.  A good place to start, both
to make sure things are installed properly and to get a feel for the typical
GeoClaw workflow, is with the example in `$CLAW/examples/tsunami/chile2010`.
(Recall that `$CLAW` points to the top level of your `clawpack` installation).

This example appears in the [GeoClaw Gallery](https://www.clawpack.org/gallery/gallery/gallery_geoclaw.html#chile-2010-tsunami) and the
[README](https://www.clawpack.org/gallery/_static/geoclaw/examples/tsunami/chile2010/README.html) file linked there gives some more information about this example.
Running this example as explained below and then plotting the results should
give plots similar to what is seen in the
[gallery _plots directory](https://www.clawpack.org/gallery/_static/geoclaw/examples/tsunami/chile2010/_plots/_PlotIndex.html)


## Running the code

See also the Clawpack documentation under
[Using the Fortran codes](https://www.clawpack.org/contents.html#using-the-fortran-codes)
for more information about some of the steps below.

You could do this test in the directory listed above, or following the
[](workflow), you might want to [](workflow:copy).  For example,
if you have created an environment variable `$MYCLAW` that points to your
own version of things:

    $ cp -r $CLAW/examples/tsunami/chile2010 $MYCLAW/

will recursively copy the entire directory to `$MYCLAW/chile2010`.

### Make topo and dtopo files

Navigate to the directory where you want to run the test, and then issue
the commands given below.  First:

    $ make topo

This simply executes the Python script `maketopo.py`, which downloads
a topography DEM (topofile) and also creates a dtopofile that specifies the
deformation based on a very simple (single subfault) model of the 2010
earthquake near Maule Chile.

### Compile the Fortran code

Next:

    $ make

compiles the Fortran code into an executable `xgeoclaw`.  The first time
you do this you will see a long list of subroutines and Fortran modules being
compiled.  Unless you make changes to the Fortran code, this does not have
to be recompiled in the future.  Note that if you do

    $ make

again you get the message

    make: `xgeoclaw' is up to date.

### Make .data files

Next:

    $ make data

This runs the Python script `setrun.py`, creating a set of input data files in
the precise format required by the Fortran code. For example:

- `claw.data` contains basic information about the computational domain,
  time stepping, desired output times, etc.
- `amr.data` contains information about the adaptive mesh refinement (AMR)
  strategy to be used.
- `topo.data` contains information about the topofiles to be used.

There are several other `.data` files that you can take a look at.  However,
if you want to change any of the data in these files, do not modify them
directly.  Instead modify `setrun.py`, which is much more user-friendly,
and is always used to create the `.data` files.

See [](intro_setrun) for more information on modifying `setrun.py`, and
[](GTT/CopalisBeach/example1/setrun_description) for an annotated `setrun.py`
for [](GTT/CopalisBeach/example1/README).

### View kml files

Running `make data` also created a set of `.kml` files (due to the last 
line in [this `setrun.py`](https://www.clawpack.org/gallery/_static/geoclaw/examples/tsunami/chile2010/setrun.py.html)
where `kmltools.make_input_data_kmls(rundata)` is invoked).

An optional step at this point is to open all of these files in Google Earth
or other GIS tool, which allows you to view the computational domain,
extent of topo and dtopo files, flagregions specified for refinement, and
the location of a gauge.  This is a valuable tool in helping to set up a new
problem properly.

### Run the GeoClaw Fortran code

Next:

    $ make output

runs the Fortran executable `xgeoclaw`, using the `.data` files as input.
As it runs,  it creates files in the output directory `_output`.

## Making plots

After the code has run,

    $ make plots

creates plots from the output directory, using information from the Python
script `setplot.py` to control what sorts of plots are produced.  If that
runs successfully, it should create a directory `_plots` with a main index
file `_plots/_PlotIndex.html`.  Opening this file in a browser will show
the plots created.

There are other ways to make plots that will be discussed later, e.g.
[interactive plotting with Iplotclaw](https://www.clawpack.org/plotting_python.html#interactive-plotting-with-iplotclaw),
which produces the
same plots as specified by `setplot.py`, but in a way that makes it easier
to explore the data (e.g. by zooming in on the plots).

You might also want to write custom scripts to read in data from `_output`
and make plots (in Python or any other graphics package you are comfortable
with).

See [](intro_postproc) for more information.

## Dependency checking

If you type

    $ make output

a second time, it will again run the existing `xgeoclaw` with the existing
`.data` files.  Even if you have changed `setrun.py` in the meantime, it will
not use the new values unless you do `make data` again before `make output`.

Another option is to do

    $ make .output

with a leading dot.  This checks dependencies, and if `setrun.py` has
recently been changed it remakes the `.data` files. (And if any of the Fortran
files have been changed, it also recompiles).  You can also do `make .plots`
which will rerun the code if necessary before making new plots.

See the Clawpack [makefiles](https://www.clawpack.org/makefiles.html)
documentation for more information on this.  Also note that the `Makefile`
contains several variables such as `OUTDIR` that can be modified if you want
to send the output someplace other than `_output`.

## chile2010 notebooks

The procedure given above is the normal procedure used for running GeoClaw.
However, you might also want to look at these notebooks, which were developed
to help explain how changing parameters in `setrun.py` affects the computed
results.

- [chile2010a](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/chile2010a/chile2010a.html) -- Examples of grid refinement.
- [chile2010b](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/chile2010b/chile2010b.html) -- Examples of gauges.
- [Video of a webinar going through these
  examples](https://csdms.colorado.edu/wiki/Presenters-0439), from CSDMS in 2019.

These notebooks use the [`clawpack.clawutil.nbtools`](https://github.com/clawpack/clawutil/blob/master/src/python/clawutil/nbtools.py)
module to facilitate
compiling and running the code and making plots from within a notebook,
which is mostly useful for creating tutorials.


## Next steps

The [](GTT/CopalisBeach/README) step you through setting  up and
running GeoClaw in more detail, in particular these pages refer to the code in
`GTT/CopalisBeach/example1`: 

- [](GTT/CopalisBeach/example1/README)
- [Copalis Beach setrun description](GTT/CopalisBeach/example1/setrun_description)
- [](GTT/CopalisBeach/example1/output1a_annotated)


:::{seealso}
This [Tutorial on flooding in the Quillayute River](https://github.com/clawpack/geoclaw_tutorial_csdms2024)
at La Push, WA also goes through some
of the basics of setting up and running GeoClaw.
(Presented at the [CSDMS](https://csdms.colorado.edu/wiki/Main_Page) Annual
Meeting in 2024.)
:::
