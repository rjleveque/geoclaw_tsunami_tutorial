# Suggested Workflow

To run the examples in this tutorial, you will need to clone the Clawpack
[apps repository](https://www.clawpack.org/apps.html) and also
a submodule `tsunami-example` (another repository within `apps`).

After cloning the main repository and setting `$CLAW` to point to the
top level of the Clawpack directory, do the following:

```
    cd $CLAW
    git clone https://github.com/clawpack/apps
    git submodule update --init tsunami-examples
```

Since these tutorials will be evolving, in the future you may need to update the
version on your computer, via::
```
    cd $CLAW/apps
    git submodule update tsunami-examples
```

## Make your own copy before running examples or notebooks

If you make changes to any of the examples, or run a notebook (as you will
be doing), then you may have "merge conflicts" when you try to update the
examples using the command above, since the version in your clone may now differ
from the version on Github that was modified in the latest version.

For this reason we suggest that you do not run examples directly in
`$CLAW/apps`.  Instead, copy any example directories or notebooks to another
location and work on it there.  You might want to put all your examples,
and new ones you create, in a directory that you turn into a git repository of
your own so that you can more easily keep track of your own changes and
developments.
