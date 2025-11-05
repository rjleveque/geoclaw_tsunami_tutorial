"""
Make an mp4 animation of fgout grid results.
This is done in a way that makes the animation quickly and with minimum
storage required, by making one plot and then defining an update function
that only changes the parts of the plot that change in each frame.

Make the animation via:
    python make_fgout_animation.py

If this script is executed in IPython or a notebook it may go into
an infinite loop for reasons unknown.  If so, close the figure to halt.

To view individual fgout frames interactively, this should work:
    import make_fgout_animation
    make_fgout_animation.update(fgframeno)  # for desired fgout frame no

"""

import sys
if 'matplotlib' not in sys.modules:
    # Use an image backend to insure animation has size specified by figsize
    import matplotlib
    matplotlib.use('Agg')

from pylab import *
import os, glob
from clawpack.visclaw import plottools, geoplot
from clawpack.visclaw import animation_tools
from matplotlib import animation, colors
from datetime import timedelta

from clawpack.geoclaw import fgout_tools

if 1:
    # use this to fetch sample_results from the online data repository:
    import fetch_sample_results
    outdir = 'sample_results/_output'
else:
    # use this if you have run the code locally to create '_output'
    outdir = '_output'


event = 'ASCE_SIFT'
fgno = 1  # which fgout grid


# look for fgout frames in outdir:
fgout_frames = glob.glob(os.path.join(outdir, \
                                      'fgout%s.t*' % str(fgno).zfill(4)))

nout = len(fgout_frames)
print('Found %i fgout frames' % nout)

if 1:
    # all frames:
    fgframes = range(1, nout+1)
else:
    # for testing on smaller set of frames:
    fgframes = range(1,nout+1,10)

output_format = 'binary32'  # should agree with setrun.py

# Instantiate object for reading fgout frames:
fgout_grid = fgout_tools.FGoutGrid(fgno, outdir, output_format)
fgout_grid.read_fgout_grids_data()


if 1:
    # background image:
    fg_image = imread('fg_background.jpg')
    fg_extent = [-124.195, -124.155, 47.11, 47.145]
else:
    fg_image = None

# Plot one frame of fgout data and define the Artists that will need to
# be updated in subsequent frames:

fgframe1 = fgframes[0]
fgout = fgout_grid.read_frame(fgframe1)

plot_extent = fgout.extent_edges
ylat = fgout.Y.mean()  # for aspect ratio of plots

fig = figure(figsize=(8,8))
ax = axes()

if fg_image is not None:
    ax.imshow(fg_image, extent=fg_extent)
    B = nan*fgout.B  # set to all nans so B doesn't plot
else:
    # if no background image, use topography
    B = fgout.B

    #B_plot = ax.imshow(flipud(B.T), extent=fgout.extent_edges,
           #cmap=geoplot.land1_colormap)
           #cmap=geoplot.googleearth_transparent)

    B_plot = plottools.pcolorcells(fgout.X,fgout.Y,fgout.B,
                                   cmap=geoplot.land_colors)
    B_plot.set_clim(0,15)


ax.set_xlim(plot_extent[:2])
ax.set_ylim(plot_extent[2:])

# Define zeta to be h onshore, h+B=eta offshore
# Here we define onshore using the current fgout.B at each time
# (rather than using the initial B0 as was done for fgmax)

onshore = fgout.B > 0
zeta = where(onshore, fgout.h, fgout.h+fgout.B)
zeta = ma.masked_where(fgout.h<0.01, zeta)

zeta_plot = plottools.pcolorcells(fgout.X, fgout.Y, zeta,
                                 cmap=geoplot.tsunami_colormap)

zeta_plot.set_clim(-20,20)

cb = colorbar(zeta_plot, extend='both', shrink=0.7)
cb.set_label('meters')

title_text = ax.set_title('%s\nSurface/Depth at time %s  (frame %i)' \
            % (event, timedelta(seconds=fgout.t), fgframe1))

ax.set_aspect(1./cos(ylat*pi/180.))
ticklabel_format(useOffset=False)
xticks(rotation=20)
ax.set_xlim(plot_extent[:2])
ax.set_ylim(plot_extent[2:])


def update(fgframeno):
    """
    Update an exisiting plot with solution from fgout frame fgframeno.
    Note: Even if blit==True in call to animation.FuncAnimation,
    the update_artists do not need to be passed in, unpacked, and repacked
    as in an earlier version of this example (Clawpack version <= 5.10.0).
    """

    fgout = fgout_grid.read_frame(fgframeno)
    print('Updating plot at time %s' % timedelta(seconds=fgout.t))

    # reset title to current time:
    title_text.set_text('%s\nSurface/Depth at time %s  (frame %i)' \
            % (event, timedelta(seconds=fgout.t), fgframeno))

    if fg_image is None:
        # replot topo B since grid resolution may have changed:
        B_plot.set_array(fgout.B.T.flatten())

    # reset zeta to current state:
    onshore = fgout.B > 0
    zeta = where(onshore, fgout.h, fgout.h+fgout.B)
    zeta = ma.masked_where(fgout.h<0.01, zeta)
    zeta_plot.set_array(zeta.T.flatten())


if __name__ == '__main__':

    print('Making anim...')
    anim = animation.FuncAnimation(fig, update, frames=fgframes,
                                   interval=200, blit=False)

    # Output files:
    name = 'fgout_animation'

    fname_mp4 = name + '.mp4'

    fname_html = None
    #fname_html = name + '.html'

    if fname_mp4:
        fps = 5
        print('Making mp4...')
        writer = animation.writers['ffmpeg'](fps=fps)
        anim.save(fname_mp4, writer=writer)
        print("Created %s" % fname_mp4)

    if fname_html:
        # html version:
        animation_tools.make_html(anim, file_name=fname_html, title=name)
