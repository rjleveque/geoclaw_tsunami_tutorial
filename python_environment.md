(python_environment)=
# Python environment with useful tools

Some Python tools are required for using GeoClaw, such as `numpy` and
`matplotlib`.  There are many other Python tools that are useful for dealing
with geophysical data and/or more advanced plotting.  The file
`requirements_geo.txt` in this directory contains a list of things you might
want to pip install.  (Feel free to edit it to add or delete things
based on your needs.)

You are strongly encouraged to create a new Python environment before pip
installing a lot of software, and some operating systems now require this.
The instructions below might be useful.

### Building a Python virtual environment

This procedure should work on a laptop (linux or MacOS) using the standard
Python module [venv](https://docs.python.org/3/library/venv.html).

    mkdir ~/venv   # directory for virtual environments
    python -m venv ~/venv/geo
    source ~/venv/geo/bin/activate
    python -m pip install --upgrade -r /path/to/requirements_geo.txt

### Using the virtual environment

When open a new shell or terminal window, the command
    
    source ~/venv/geo/bin/activate

should activate the environment.  You might want to put this in your
`.bashrc` file, for example.  Then if you start python, ipython, or a 
Jupyter lab in this environment, the packates listed in requirements_geo.txt
(and their dependencies) should be available to import.

### Building a conda environment on DesignSafe

:::{seealso}
https://designsafe-ci.org/user-guide/tools/jupyterhub/#installing
:::

The following should work, but doesn't seem to at the moment....  

First launch JupyterHub from
https://designsafe-ci.org/use-designsafe/tools-applications/analysis/jupyter/

Then start a terminal, and in this terminal:

    conda config --add envs_dirs ~/MyData/Python_Envs  # directory for env
    conda create --name geo  -y -c conda-forge pip python
    conda activate geo 
    python -m pip install --upgrade -r /path/to/requirements_geo.txt

    pip install --src=$HOME/MyData/clawpack_src --user --no-build-isolation -e \
        git+https://github.com/clawpack/clawpack.git@v5.13.1#egg=clawpack
