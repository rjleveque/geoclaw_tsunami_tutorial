# GeoClaw Tsunami Tutorial

Tutorial on using GeoClaw for tsunami modeling

Under development, more to come! 

The rendered version of this Jupyter Book can be viewed at
https://rjleveque.github.io/geoclaw_tsunami_tutorial

## Usage

Clone this repository to obtain all of the GeoClaw examples and Jupyter notebooks discussed in the tutorial.

### Building the book

If you'd like to develop and/or build the GeoClaw Tsunami Tutorial book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. (Optional) Edit the books source files located in the `geoclaw_tsunami_tutorial/` directory
4. Run `jupyter-book clean geoclaw_tsunami_tutorial/` to remove any existing builds
5. Run `jupyter-book build geoclaw_tsunami_tutorial/`

A fully-rendered HTML version of the book will be built in `geoclaw_tsunami_tutorial/_build/html/`.


## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).

This book is rebuilt on Github on every push, using Github actions as
specified in the file `.github/workflows/deploy.yml` which was
set up using [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) 
Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) for other options
for deploying a book online.
