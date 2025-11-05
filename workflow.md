(workflow)=
# Suggested Workflow

## Tutorial repository

The files in this repository can be viewed online at:
https://github.com/rjleveque/geoclaw_tsunami_tutorial.

To run the examples in this tutorial, you will need to clone the git
repository that contains them (along with all the markdown files and Jupyter
notebooks that create these tutorial pages):

    $ git clone https://github.com/rjleveque/geoclaw_tsunami_tutorial.git

This will create a new directory named `geoclaw_tsunami_tutorial`
containing a subdirectory `GTT` (short for GeoClaw Tsunami Tutorial)
that contains the examples that we will be working with.
(The top level directory also contains a lot of markdown and other files
that are used in building the Jupyter Book that you are reading).

You might want to set an
environment variable that contains the full path (on your computer)
to the `GTT` subdirectory. 
In this tutorial this variable will be called `GTT`
which can be set in the bash shell via:

    $ cd geoclaw_tsunami_tutorial/GTT
    $ export GTT=`pwd`

The export command creates a new environment variable named `GTT` that now
points to this directory, since `pwd` prints the working directory (you
could alternatively type in the full path name in defining `GTT`).  

You can use this variable in any bash command by using `$GTT`, which gets
replaced by its definition, so for example:

    $ echo $GTT

should print out the expected full path.  Files within this directory
will often be referred to in this tutorial as e.g.
`$GTT/topo/CopalisTopo.ipynb`, which is the Jupyter notebook that
we will use to create a topofile for one of the examples.

Since these tutorials will be evolving, in the future you may need to update the
version on your computer, via::

    $ cd $GTT
    $ git pull

## Clawpack apps respository

You should also clone the Clawpack
[apps repository](https://www.clawpack.org/apps.html),
since this contains a few other examples and several Jupyter notebooks
illustrating GeoClaw concepts.

After cloning the main Clawpack repository, (using the `git clone` option from
[Options for installing Clawpack Fortran
codes](https://www.clawpack.org/installing_fortcodes.html#installing-fortcodes), 
as suggested in [](prerequisites)), 
and setting `$CLAW` to point to the
top level of the Clawpack directory, do the following:

```
    $ cd $CLAW
    $ git clone https://github.com/clawpack/apps
```

(workflow:copy)=
## Make your own copy before running examples or notebooks

If you make changes to any of the examples, or run a notebook (as you will
be doing), then you may have "merge conflicts" when you try to update the
examples using `git pull`, since the version in your clone may now differ
from the version on Github that was modified in the latest version.

For this reason **we strongly suggest that you do not run examples directly in
`$GTT`**.  Instead, copy any example directories or notebooks to another
location and work on it there.  You might want to put all your examples,
and new ones you create, in a directory that you turn into a git repository of
your own so that you can more easily keep track of your own changes and
developments.

For example, you could create a new directory with any name and location you
want (but not within the `$GTT` or `$CLAW` directories) and then set an
environment variable to point to this directory, and call it e.g. `$MYGTT`.
Then before running the Jupyter notebook `$GTT/topo/CopalisTopo.ipynb`,
for example (which is rendered in this tutorial as
[](GTT/topo/CopalisTopo)),
you could first do:

    $ cp -r $GTT/topo $MYGTT/

which would recursively copy the entire `$GTT/topo` into `$MYGTT/topo`. Then
run the notebook in that directory, so that the one in `$GTT/topo` is
unchanged.

To start with, you could do:

    $ cp -r $GTT/* $MYGTT/*

to recursively copy all files and subdirectories in `$GTT` to `$MYGTT`, but
later if you want to move something new over you might not want to overwrite
your own versions of earlier tests that are already in `$MYGTT`, so you
might have to be more selective in what you copy.

Similarly, to run the notebooks in `$CLAW/apps/notebooks/geoclaw/chile2010a`
you might first copy this entire directory to `$MYGTT`, and then running the
notebooks should give you output similar to this
[rendered version](https://www.clawpack.org/gallery/_static/apps/notebooks/geoclaw/chile2010a/chile2010a.html)
from the
[gallery of tsunami application notebooks](https://www.clawpack.org/gallery/notebooks.html#tsunami-modeling-examples).

Of course you can organize `$MYGTT` however you want, e.g. you might want an
`apps` subdirectory within it for things you copied from `$CLAW/apps` and a
`mygeo` subdirectory for new GeoClaw experiments that you are setting up on
your own.

You might also want to turn your `$MYGTT` directory into your own git
repository. Using version control regularly is a good idea when developing
code, for many reasons, whether you are sharing code with others or think
you are working entirely on your own (in which case you still need to
collaborate with your past and future self, and using version control makes
this far easier!)  There are many excellent git tutorials online.

(workflow:sample_results)=
### Sample results

Some example directories have a script `fetch_sample_results.py` to fetch
sample results (e.g. the `_plots` directory containing plots generated after
running the code).  Executing this allows you to explore the results without
having to run the code. This script is also run to fetch the sample results
that are shown on the pages built by Jupyter Book such as 
[](GTT/CopalisBeach/example1/results).
(See [](datasets) for more information about how this works.)

(workflow:run)=
## Workflow for running GeoClaw and processing results

The typical workflow for running GeoClaw and making plots from the output is
explained in [](testing_chile2010).

For more details on setting up a run via `setrun.py`, see
[](GTT/CopalisBeach/example1/README) and the annotated `setrun.py` in
[](GTT/CopalisBeach/example1/setrun_description).

To run/modify an example yourself, you might want to start with
[](GTT/CopalisBeach/exercise1/README) and 
[](GTT/CopalisBeach/exercise1/debug).

The use of fgmax and fgout grids is covered in 
[](GTT/CopalisBeach/example2/README).

Other GeoClaw features will be
covered in additional examples still under development.

:::{seealso}
The following pages list many topics, with links to more information on how to
do specific things:
- [](intro_setrun)
- [](intro_postproc)
:::

