# GTT_data_repository directory

This directory is used only by developers and can be ignored.

The `registry.txt` file in this directory is needed when sample data files are
downloaded using `$GTT/common_code/GTT_tools.fetch`.  Do not remove this
directory.

:::{warning}
You should not run the scripts in this directory, they are only used when
developing these tutorials.
:::


## Notes for developers only:

`datarepo_tools.make_all()` contains a list of data files and directories
to be zipped and placed in the `GTT_data` subdirectory of this directory,
organized with the same file structure as the original versions.

Running this function will do so, and will also create a new `registry.txt`
file with the hash for each zip file.

Then the `GTT_data` directory should be rsync'ed to the server hosting the data
repository by:

    $ rsync -avz GTT_data/ \
        clawpack@homer.u.washington.edu:public_html/geoclaw/GTT_data/

and the new `registry.txt` file committed and pushed to Github.

