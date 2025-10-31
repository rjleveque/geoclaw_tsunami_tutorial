(copalis_makefile_description)=
# Makefile description

From `$GTT/CopalisBeach/exercise1`.  See [](./README) for more description
of the files in this directory.

:::{tip}
See [](./debug) for help debugging problems you encounter running the
code in this directory.

The first thing to try is:

    $ make check

which will tell you how some of your environment variables are set and
might help uncover some problems.
:::

:::{seealso}
- [Clawpack Makefiles](https://www.clawpack.org/makefiles.html)
- [Using the Fortran codes in Clawpack](https://www.clawpack.org/contents.html#using-the-fortran-codes)
:::

:::{warning}
Makefiles are written in a very particular form, a language unto itself.
There are whole books on the subject, e.g. {cite}`GNUmake`, or try Googling
"makefile tutorial fortran".
:::

The `Makefile` in this directory has the form of the typical Makefile for
other projects and can often be copied and used elsewhere with few changes.
Here is an annotated version of it to explain what it does.


    # Makefile for Clawpack code in this directory.
    # This version only sets the local files and frequently changed
    # options, and then includes the standard makefile pointed to by CLAWMAKE.
    CLAWMAKE = $(CLAW)/clawutil/src/Makefile.common

The `$(CLAW)` in the line above refers to the environment variable `CLAW`.
At the command line this used as `$CLAW` but in the Makefile a different form
is required.

The file CLAWMAKE is a much longer and very complicate Makefile that defines
what happens when you type `make data` or `make .output`, for example.
All those rules in included in this Makefile by the `include` statement
at the end of this Makefile.


    # See the above file for details and a list of make options, or type
    #   make .help
    # at the unix prompt.

    # Adjust these variables if desired:
    # ----------------------------------

    CLAW_PKG = geoclaw                  # Clawpack package to use

    EXE ?= xgeoclaw

    SETRUN_FILE = setrun.py               # File containing function to make data
    OUTDIR = _output                      # Directory for output
    SETPLOT_FILE = setplot.py             # File containing setplot function
    PLOTDIR = _plots                      # Directory for plots

The `?=` syntax used for `EXE` above and for other variables
below means to set it to the value given
here only if this is not already set as an environment variable.

The standard names for `setrun.py` and `setplot.py` are used here, but you
might want to change them as was done in the different Makefiles in
`../example1`.  Similarly for the output and plots directories.

:::{tip}
You can also move `_output` elsewhere after running the code, e.g.

        $ mv _output _output_run1

and/or you can specify these variables when running make, e.g.

        $ make plots OUTDIR=_output_run1 PLOTDIR=_plots_run1
:::


The next few lines are things you might want to set as environment variables
for all your runs, rather than in the Makefiles you use, since these
may never change for your computing environment:

    # Environment variable FC should be set to fortran compiler, e.g. gfortran
    FC ?= gfortran

    # Compiler flags can be specified here or set as an environment variable
    FFLAGS ?= -O2 -fopenmp  # for gfortran

    # Number of OpenMP threads to use:
    OMP_NUM_THREADS ?= 6

:::{seealso}
- [Fortran Compilers for Clawpack](https://www.clawpack.org/fortran_compilers.html)
- [Using OpenMP in Clawpack](https://www.clawpack.org/openmp.html)
:::

You don't generally need to change any of the following lines unless you
need to modify one of the Fortran routines for some reason. In that case, see
[Library routines in Makefiles](https://www.clawpack.org/makefiles_library.html).

    # ---------------------------------
    # package sources for this program:
    # ---------------------------------

    GEOLIB = $(CLAW)/geoclaw/src/2d/shallow
    include $(GEOLIB)/Makefile.geoclaw


    # ---------------------------------------
    # package sources specifically to exclude
    # (i.e. if a custom replacement source
    #  under a different name is provided)
    # ---------------------------------------

    EXCLUDE_MODULES = \

    EXCLUDE_SOURCES = \

    # ----------------------------------------
    # List of custom sources for this program:
    # ----------------------------------------


    MODULES = \

    SOURCES = \
      $(CLAW)/riemann/src/rpn2_geoclaw.f \
      $(CLAW)/riemann/src/rpt2_geoclaw.f \
      $(CLAW)/riemann/src/geoclaw_riemann_utils.f \

    #-------------------------------------------------------------------
    # Include Makefile containing standard definitions and make options:
    include $(CLAWMAKE)
