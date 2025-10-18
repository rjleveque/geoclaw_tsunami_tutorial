# GTT_data_repository directory

This directory is used only by developers and can be ignored.

:::{warning}
You should not run the scripts in this directory, they are only used when
developing these tutorials.
:::


## Notes for developers only:

`datarepo_tools.py` contains a list of data files and directories
to be zipped and placed in the `GTT_data` subdirectory of this directory,
organized with the same file structure as the original versions.
Running this function will do so.  

Then the `GTT_data` directory should be rsync'ed to the server hosting the data
repository by:

    $ rsync -avz GTT_data/ \
        clawpack@homer.u.washington.edu:public_html/geoclaw/GTT_data/
