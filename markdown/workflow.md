# Suggested Workflow

## Tutorial repository

To run the examples in this tutorial, you will need to clone the git
repository that contains them (along with all the markdown files and Jupyter
notebooks that create these tutorial pages):

    $ git clone https://github.com/rjleveque/geoclaw_tsunami_tutorial.git

This will create a new directory named `geoclaw_tsunami_tutorial`
which also contains a subdirectory of the same name, which is really the top
level in relation to these notes and the examples.  You might want to set an
environment variable to point to this directly. 
In this tutorial this will be called `$GTT` (for GeoClaw Tsunami Tutorial)
which can be set in the bash shell via:

    $ cd geoclaw_tsunami_tutorial/geoclaw_tsunami_tutorial
    $ export GTT=`pwd`

The export command creates a new environment variable named `GTT` that now
points to this directory, since `pwd` prints the working directory (you
could alternatively type in the full path name in defining `GTT`.  

You can use this variable in any bash command by using `$GTT` which gets
replaced by its definition, so for example:

    $ echo $GTT

should print out the expected full path.  Files within this directory
will often be referred to in these notes as e.g. `$GTT/workflow.md`, which
is the markdown file that creates the page you are now reading.

Since these tutorials will be evolving, in the future you may need to update the
version on your computer, via::

    $ cd $GTT
    $ git pull

## Clawpack apps respository

You should also clone the Clawpack
[apps repository](https://www.clawpack.org/apps.html),
since this contains a few other examples and several Jupyter notebooks
illustrating GeoClaw concepts.

After cloning the main repository and setting `$CLAW` to point to the
top level of the Clawpack directory, do the following:

```
    $ cd $CLAW
    $ git clone https://github.com/clawpack/apps
```


## Make your own copy before running examples or notebooks

If you make changes to any of the examples, or run a notebook (as you will
be doing), then you may have "merge conflicts" when you try to update the
examples using `git pull`, since the version in your clone may now differ
from the version on Github that was modified in the latest version.

For this reason we suggest that you do not run examples directly in
`$GTT`.  Instead, copy any example directories or notebooks to another
location and work on it there.  You might want to put all your examples,
and new ones you create, in a directory that you turn into a git repository of
your own so that you can more easily keep track of your own changes and
developments.

For example, you could create a new directory with any name and location you
want (but not within the `$GTT` or `$CLAW` directories) and then set an
environment variable to point to this directory, and call it e.g. `$MYGTT`.
Then before running the Jupyter notebook `$GTT/topo/CopalisTopo.ipynb`,
for example (which is rendered in this tutorial as
[CopalisTopo](topo/CopalisTopo),
you could first do:

    $ cp -r $GTT/topo $MYGTT/

which would recursively copy the entire `$GTT/topo` into `$MYGTT/topo`. Then
run the notebook in that directory, so that the one in `$GTT/topo` is
unchanged.

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

