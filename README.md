# GeoClaw Tsunami Tutorial

Tutorial on using GeoClaw for tsunami modeling

[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](<https://rjleveque.github.io/geoclaw_tsunami_tutorial>)

Under development, more to come! 

The rendered version of this [Jupyter Book](https://jupyterbook.org/)
can be viewed at
https://rjleveque.github.io/geoclaw_tsunami_tutorial

The tutorial examples are all within the `GTT` subdirectory. Files in the
top level are primarily used for building the Jupyter Book.

## Usage

Clone this repository to obtain all of the GeoClaw examples and
Jupyter notebooks discussed in the tutorial, which will be in the `GTT`
subdirectory.

See [Suggested Workflow](https://rjleveque.github.io/geoclaw_tsunami_tutorial/markdown/workflow.html)
for more information on how to run the examples.

### Building the book

If you'd like to develop and/or build the GeoClaw Tsunami Tutorial book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a
   virtual environment)
3. (Optional) Edit the books source files (which include `.md` files in this
   directory and also some `.md` and `.ipynb` files within `GTT`).
4. Run `jupyter-book clean ./` to remove any existing builds
5. Run `jupyter-book build ./`

A fully-rendered HTML version of the book will be built in `./_build/html/`.


## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).

This book is rebuilt on Github on every push, using Github actions as
specified in the file `.github/workflows/deploy.yml` which was
set up using [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) 
Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) for other options
for deploying a book online.
