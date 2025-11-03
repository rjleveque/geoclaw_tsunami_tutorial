(copalis:setplot_description)=
# Setting up the time frame plots

"Time frame" output refers to the full solution that is produced at each of
the "output times" specified in `setrun.py`.  This full output generally
consists of the solution values at every point on each of the grid patches
that exist at this output time.  When AMR is being used with many levels of
refinement this may consist of dozens or even hundreds of grid patches.
(Even with only a few levels, the size of each grid patch is restricted by
the `max1d` parameter that can be set in `setrun.py`, 60 by default, and so
there may be dozens of patches at each level.)

Hence to produce a plot of a single time frame of the solution requires knitting
together all the different patches of data.  To make this easier for the user,
tools were created in the VisClaw package to handle AMR data in Clawpack more
easily, and this is commonly used for GeoClaw.

:::{seealso}
For general information on using `setplot.py` for plotting time frames with
AMR data, see
- [Using `setplot.py` to specify the desired
  plots](https://www.clawpack.org/setplot.html)
  from the general Clawpack documentation.
- [Interactive plotting with Iplotclaw](https://www.clawpack.org/plotting_python.html#interactive-plotting-with-iplotclaw)
:::

## Annotated `setplot.py`

Here is the `setplot.py from this directory, with a few additional comments...



    #--------------------------
    def setplot(plotdata):
    #--------------------------

        """
        Specify what is to be plotted at each frame.
        Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
        Output: a modified version of plotdata.

        """

        from clawpack.visclaw import colormaps, geoplot
        from numpy import linspace

        plotdata.clearfigures()
        plotdata.format = 'binary'

The output files in this directory are in binary format because that was
specified in `setrun.py`.  If the format there was set to `'ascii'`, then
`plotdata.format` should also be set to `'ascii'`.

        from clawpack.visclaw import gaugetools
        setgauges = gaugetools.read_setgauges(plotdata.outdir)
        gaugenos = setgauges.gauge_numbers

        def addgauges(current_data):
            from clawpack.visclaw import gaugetools
            gaugetools.plot_gauge_locations(current_data.plotdata,
                 gaugenos=gaugenos, format_string='ko', add_labels=True,
                 fontsize=8, markersize=3)

The `addegauges` function is used later to specify that gauge locations
should be added to some of the plots.
Here `gaugenos` is set by reading in all gauge numbers from
`_output/gauges.data`.  Alternatively you could set
`gaugenos=[101,102]`, for example, in the call to
`gaugetools.plot_gauge_locations` if you only want to plot the locations of
those two gauges.


        #-----------------------------------------
        # Figure for surface in ocean
        #-----------------------------------------

        plotfigure = plotdata.new_plotfigure(name='Ocean Surface', figno=0)
        #plotfigure.show = False
        plotfigure.figsize = (7,7)
        plotfigure.facecolor = 'w'

        # Set up for axes in this figure:
        plotaxes = plotfigure.new_plotaxes('pcolor')

        # note: including h:m:s in title converts to hours:minutes:seconds
        plotaxes.title = 'Surface at time h:m:s after quake'

        plotaxes.aspect_latitude = -20.  # set aspect ratio based on this latitude
        plotaxes.title_fontsize = 15
        plotaxes.xticks_kwargs = {'rotation':20, 'fontsize':12}
        plotaxes.yticks_fontsize = 12
        plotaxes.xlabel = 'Longitude'
        plotaxes.xlabel_fontsize = 12
        plotaxes.ylabel = 'Latitude'
        plotaxes.ylabel_fontsize = 12

        plotaxes.xlimits = [-128.5,-123.5]
        plotaxes.ylimits = [45,49]

        # Water
        plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
        plotitem.plot_var = geoplot.surface_or_depth
        plotitem.pcolor_cmap = geoplot.tsunami_colormap
        plotitem.pcolor_cmin = -5
        plotitem.pcolor_cmax = 5
        plotitem.add_colorbar = True
        plotitem.colorbar_extend = 'both'
        plotitem.colorbar_shrink = 0.7
        plotitem.colorbar_label = 'meters'
        plotitem.amr_celledges_show = [0,0,0]
        plotitem.patchedges_show = 0

        # Land
        plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
        plotitem.plot_var = geoplot.land
        plotitem.pcolor_cmap = geoplot.land_colors
        plotitem.pcolor_cmin = 0.0
        plotitem.pcolor_cmax = 500.0
        plotitem.add_colorbar = False

This is a typical description for a plot figure that shows a pcolor image
of the water surface using one colormap (`geoplot.tsunami_colormap`)
on top of the land topography that is shown with a different colormap
(`geoplot.tsunami_colormap`).  These colormaps are defined in the VisClaw
module `clawpack.visclaw.geoplot` that is imported earlier in `setplot.py`.
The actual code can be found in the Clawpack source code in the file
`$CLAW/visclaw/src/python/visclaw/geoplot.py`.

See [Using `setplot.py` to specify the desired
plots](https://www.clawpack.org/setplot.html)
from the general Clawpack documentation
for more information on the process of setting up one or more axes within
a plot figure and then specifying one or more plotitems within each axis.
Here we have a single axis that contains two plotitems, one for the water
surface and one for the land.  Note that the first plotitem specifies

    plotitem.plot_var = geoplot.surface_or_depth

and the second specifies

    plotitem.plot_var = geoplot.land

The `geoplot` module defines these two functions. The `geoplot.surface_or_depth`
function returns the water surface `eta` at points that are off-shore (defined
by where the topography `B < 0`), but returns the water depth `h` where
`B >= 0`.  This shows what we often most want to see in the plots, since
in the ocean we don't want to see the huge variations of the water depth,
only the wave on the surface, while onshore we care less about the elevation
of the surface and more about the depth of the inundation.

But for some applications you may want to plot something different and you
can define your own function in `setplot.py` or elsewhere and set
`plotitem.plot_var` to this function.  (See the ones in
`$CLAW/visclaw/src/python/visclaw/geoplot.py` for the format of function
required).  You can also simply specify `plotitem.plot_var = 0`, for example,
to plot the `q[0,:,:]` variable over each patch, i.e. the first element of the
set of variables in `q`, which for GeoClaw is simply the water depth `h`.
The other variables saved in each time frame output are `hu`, 'hv`, and `eta`.

The `geoplot.land` function simply
returns the topography `B` but this has to be computed from the `eta` and `h`
values that are actually stored as part of the AMR output (using `B = eta - h`)

Most of the other parameters set in the code aboveshould be self-explanatory.
You might want to
experiment with changing some of these and see how the plots change.

A second plotfigure is specified for showing a zoomed in view around
Copalis Beach, which is very similar, and much of that code is omitted here.

One difference is that for the plotaxis specified in the Copalis Beach zoom,
the line

        plotaxes.afteraxes = addgauges  # show the gauge locations

says that after plotting everything else on these axes, the function
`addgauges` should be called to plot the gauge locations.

Another addition for the Copalis Beach zoom is that one
additional plotitem is specified in addition to the land and water surface:

        # add contour lines of bathy if desired:
        plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
        plotitem.show = False
        plotitem.plot_var = geoplot.topo
        plotitem.contour_levels = [-1]
        plotitem.amr_contour_colors = ['yellow']  # color on each level
        plotitem.kwargs = {'linestyles':'solid','linewidths':0.7}
        plotitem.amr_contour_show = [0,0,0,0,0,1,0,0] # show only on level 6
        plotitem.celledges_show = 0
        plotitem.patchedges_show = 0

This specified that contours of topography should also be drawn.  Note that
we generally do not want to plot the contours for all of the AMR grid patches,
or there would be 6 sets of contour lines in the region covered by Level 6 AMR
patches, since they would be plotted for each patch.  They would not line up
well since the ones on the coarser patches are would be based on the coarser
data.  So  `plotitem.amr_contour_show`  is a list of 0/1 or False/True values
to indicate which level(s) of patches to draw contour lines on.

:::{tip}
Since `celledges_show = 0` the edges of grid cells are not shown on any level,
and similarly for the edges of grid patches since `patchedges_show = 0`.
Setting `patchedges_show = 1` would cause patch edges to be shown on all
levels. If we only wanted to see the patch edges on Level 6 we could instead
set

        plotitem.amr_patchedges_show = [0,0,0,0,0,1,0,0]

Some other `plotitem` attributes also have this AMR feature.
:::

At each synthetic gauge a time series is recorded in the output
directory.  The next part of the `setplot.py` file shows how to specify
two plotsfigures for each gauge, displaying the time series of water
depth `h` and surface elevation `eta` at the gauge.

(copalis:gauge_plots)=
## Specifying gauge plots

        #-----------------------------------------
        # Figures for gauges
        #-----------------------------------------


        time_scale = 1./60.
        time_label = 'minutes'

        plotfigure = plotdata.new_plotfigure(name='Gauge depth',
                                             figno=300,type='each_gauge')
        plotfigure.figsize = (10,5)
        plotfigure.clf_each_gauge = True

        # Set up for axes in this figure:
        plotaxes = plotfigure.new_plotaxes()
        plotaxes.time_scale = time_scale
        plotaxes.time_label = time_label  # note the x-axis is time in this case
        plotaxes.ylabel = 'meters'
        plotaxes.xlabel_fontsize = 15
        plotaxes.ylabel_fontsize = 15
        plotaxes.title_fontsize = 20
        plotaxes.xlimits = 'auto'    
        plotaxes.ylimits = 'auto'
        plotaxes.title = 'Water depth h'
        plotaxes.grid = True
        plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
        plotitem.plot_var = 0
        plotitem.plotstyle = 'b-'


        plotfigure = plotdata.new_plotfigure(name='Gauge eta',
                                             figno=301,type='each_gauge')
        plotfigure.figsize = (10,5)
        plotfigure.clf_each_gauge = True

        # Set up for axes in this figure:
        plotaxes = plotfigure.new_plotaxes()
        plotaxes.time_scale = time_scale
        plotaxes.time_label = time_label
        plotaxes.ylabel = 'meters relative to topo vdatum'
        plotaxes.xlabel_fontsize = 15
        plotaxes.ylabel_fontsize = 15
        plotaxes.title_fontsize = 20
        plotaxes.xlimits = 'auto'
        plotaxes.ylimits = 'auto'
        plotaxes.title = 'Surface eta = B+h'
        plotaxes.grid = True
        plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
        plotitem.plot_var = -1   # eta is the last component in the q array
        plotitem.plotstyle = 'b-'

Note that in these plots we used `plotitem.plot_var = 0` for the depth
plot and `plotitem.plot_var = -1` for eta, since in Python the index `-1` refers
to the last element in an array.  The values stored at the gauge
are typically `[h, hu, hv, eta]` but it is possible to specify in `setrun.py`
that only `[h, eta]` should be stored.

## Timing plots

The next part of `setplot.py` creates the timing plots by reading in the
files `timing.txt` and `timing.csv` from the output directory.  If you want
timing plots you can generally just use this code as is, although you might
want to change the units used from `'minutes'` and `'millions'` to
`'hours'` and `'billions'` if running a much bigger problem.

        # Plots of timing (CPU and wall time):

        def make_timing_plots(plotdata):
            import os
            from clawpack.visclaw import plot_timing_stats
            try:
                timing_plotdir = plotdata.plotdir + '/timing_figures'
                os.system('mkdir -p %s' % timing_plotdir)
                units = {'comptime':'minutes', 'simtime':'minutes', 'cell':'millions'}
                plot_timing_stats.make_plots(outdir=plotdata.outdir, make_pngs=True,
                                              plotdir=timing_plotdir, units=units)
                os.system('cp %s/timing.* %s' % (plotdata.outdir, timing_plotdir))
            except:
                print('*** Error making timing plots')

        # create a link to this webpage from _PlotIndex.html:
        otherfigure = plotdata.new_otherfigure(name='timing',
                        fname='timing_figures/timing.html')
        otherfigure.makefig = make_timing_plots


## Parameters for html version of plots

The final section of the plots mostly controls what goes onto the html
pages created with the `make plots` command, and doesn't matter when viewing
plots interactively with `Iplotclaw`.

        #---------------------------------------------------------------

        # Parameters used only when creating html and/or latex hardcopy
        # e.g., via pyclaw.plotters.frametools.printframes:

        plotdata.printfigs = True                   # print figures
        plotdata.print_format = 'png'               # file format

        # ALL frames and gauges
        plotdata.print_framenos = 'all'             # list of frames to print
        plotdata.print_gaugenos = 'all'             # list of gauges to print
        plotdata.print_fignos   = 'all'             # list of figures to print
        plotdata.html = True                        # create html files of plots?
        plotdata.html_homelink = '../README.html'   # pointer for top of index
        plotdata.latex = True                       # create latex file of plots?
        plotdata.latex_figsperline = 4              # layout of plots 2
        plotdata.latex_framesperline = 4            # layout of plots 1
        plotdata.latex_makepdf = False              # also run pdflatex?
        plotdata.mp4_movie = False                  # make mp4 animations?
        plotdata.parallel = True                    # make plots in parallel?

        return plotdata

A few notes:

You can replace `'all'` by a list of integers in specifying
- `print_framenos` (to only make plots for certain time frames)
- `print_gaugenos` (to only make plots for a subset of the gauges)
- `print_fignos` (to only create a subset of the plotfigures for each frame)

If `plotdata.parallel` is `True` then plots for several time frames will be
created simultaneously, the number controlled by the environment variable
`OMP_NUM_THREADS`.

By default a javascript html movie will be created for each plotfigure.

In addition you can make an mp4 movie for each plotfigure (provided you have
`ffmpeg` installed) by setting `plotdata.mp4_movie = True`.
