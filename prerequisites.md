
# GeoClaw Prerequisites

GeoClaw is distributed with [Clawpack](https://www.clawpack.org), and
if possible you should have Clawpack installed and working on your own computer
for ease in working through the examples in this tutorial.

The core code is written in Fortran, so you will need a Fortran compiler such
as gfortran.  The user interface (both for setting up a simulation and for
viewing the results) is in Python, and some of the examples in this tutorial
are in the form of Jupyter notebooks.  See [Installation Prerequisites](https://www.clawpack.org/prereqs.html#prereqs) for more details.

See [Options for installing Clawpack Fortran codes](https://www.clawpack.org/installing_fortcodes.html#installing-fortcodes)
for two possible ways to install Clawpack that expose the Fortran code.
For our purposes it is best to use the `git clone` option, since we will
need to clone the separate [apps repository](https://www.clawpack.org/apps.html)
that contains the examples for this tutorial.

Running Clawpack code requires using Makefiles and is generally done from
the command line in a linux or MacOS shell (and on a Mac you must also
install the 
[xcode command line tools](https://developer.apple.com/xcode/resources/).
The use of Windows is not generally supported for Clawpack.

After installing clawpack, you should
[set some environment variables](https://www.clawpack.org/setenv.html).
In particular, set `$CLAW` to point to the top level of
your clawpack installation, e.g. in a bash shell:

    $ export CLAW=/full/path/to/clawpack

You should also make sure this path is on the path that Python uses to find
modules when you do an `import`.  The clawpack path defined above can be appended
to your current $PYTHONPATH (if this environment variable is already set
to include other paths) via::

    $ export PYTHONPATH=$PYTHONPATH:$CLAW
See the clawpack documentation on
[Python path](https://www.clawpack.org/python_path.html).

## Using the DesignSafe Jupyter Hub

An alternative to installing software is to use the
[DesignSafe Jupyter Hub](https://designsafe-ci.org/use-designsafe/tools-applications/analysis/jupyter/).
Researchers who study natural hazards can get an account on the NSF infrastructure center [DesignSafe](https://designsafe-ci.org/) and, if more compute power is needed,
also an account on TACC, the [Texas Advanced Computing Center](https://tacc.utexas.edu/systems/all/).

More details to come...
