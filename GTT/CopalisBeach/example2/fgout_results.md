---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(copalis:example2:fgout_results)=
# Sample fgout results

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

The directory `$GTT/CopalisBeach/example2`
contains a GeoClaw example that produces results on fgout and fgmax grids.

:::{seealso}
- [](README) for more about this example,
- [](plot_fgout) is a Jupyter notebook that plots the fgout results.
- [chile2010_fgmax-fgout]() shows results from the example included with
  GeoClaw in `$CLAW/geoclaw/examples/tsunami/chile2010_fgmax-fgout`, which
  also illustrates how to make fgout animations, similar to what is
  described here, using the Chile 2010 event in the offshore region.
:::

The script `fetch_sample_results.py` can be used to fetch some sample
results if you want to run the post-processing script or notebook in
this directory without running the GeoClaw code.

```{code-cell}
:tags: [remove-input, remove-output]
run fetch_sample_results.py
```

## Plotting fgout results using `setplot.py`

One approach to plotting fgout grid results is to specify a setplot
function (in this example, there is one in `setplot_fgout.py`) that has the
same form as a setplot function for plotting standard GeoClaw/Clawpack
output frames, but we set:

    plotdata.file_prefix = 'fgout0001'  # for fgout grid fgno==1

to indicate that instead of the usual output files with names like
`fort.t*` and `fort.q*` (and also `fort.b*` in the case of binary output),
as described at 
[Clawpack output styles](https://www.clawpack.org/output_styles.html),
the data is in files named `fgout0001.t*`, etc.
The fgout results are written with the same format as AMR frame data,
the only difference is that each frame has only one grid (the fgout grid)
at a single AMR level (which is denoted by AMR level 0 in the `fgout0001.t*`
files, to remind us that this is not one of the computational grids and is
based on data at all levels).

Executing:

    $ make plots SETPLOT_FILE=setplot_fgout.py PLOTDIR=_plots_fgout

will use this `setplot_fgout.py` file to create a set of plots in
`_plots_fgout` that includes all of the fgout snapshots at the fgout times
that were specified in `setrun.py`.

## Loading and plotting one or more fgout snapshots directly

Alternatively, since every fgout frame consists of only a single
uniform grid of data, it is much easier to manipulate or plot
directly than general AMR data. The `clawpack.geoclaw.fgout_tools`
module described at 
[fgout tools](https://www.clawpack.org/fgout_tools_module.html)
provides tools for reading frames and producing
arrays that can then be worked with directly.

One example of how this might be done is provided in the Jupyter
notebook [](plot_fgout).
This shows how a single frame of fgout results can be loaded, and then you
can do any sort of plotting or other manipulations you please on this data,
which is stored as a single numpy array.


## Making an animation

The sample code in `make_fgout_animation.py` reads in all the frames
of fgout data and produces an animation as stand-alone mp4 and/or
html files.  To run this code, do::

    python make_fgout_animation.py

The use of fgout grids provides a way to produce frequent outputs
on a fixed grid resolution, as often desired for making smooth
animations of a portion of the computational domain.

The code produces this animation:

(Right click and select "Show all controls" to find the Play button.)

![](./sample_results/fgout_animation.mp4)


