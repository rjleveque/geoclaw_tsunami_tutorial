
"""
Make:
- png plots of fgmax results for Google Earth overlays,
- png files for the colorbars,
- kml files to display each png,
- kmz file that includes all the other files.

Open the kmz file in Google Earth and select desired plots from the menu.
Note that if you right-click on a menu item and select "Get Info", you can
adjust the transparency to see the topography below the color plot.
"""


import os,sys,glob,zipfile,shutil

if 'matplotlib' not in sys.modules:
    import matplotlib
    matplotlib.use('Agg')  # Use an image backend

from pylab import *

from clawpack.geoclaw import topotools, dtopotools
from clawpack.visclaw import colormaps, gridtools
import matplotlib as mpl
from clawpack.geoclaw import kmltools, fgmax_tools
import contextlib


if 1:
    # use this to fetch sample_results from the online data repository:
    import fetch_sample_results
    outdir = 'sample_results/_output'
else:
    # use this if you have run the code locally to create '_output'
    outdir = '_output'

fgno = 1  # id number of fgmax grid
run_name = 'CopalisBeach_ASCE_SIFT'  # name used in kmz file name

name = '%s_fgmax%s' % (run_name, fgno)

# Read fgmax input and output:

fgmax = fgmax_tools.FGmaxGrid()

fgmax.outdir = outdir  # as set above

# read the input data used for this run:
data_file = os.path.join(fgmax.outdir, 'fgmax_grids.data')
fgmax.read_fgmax_grids_data(fgno=fgno, data_file=data_file)

# read the fgmax output:
fgmax.read_output()

# Compute B0: adjust fgmax.B by approximate dz at each point from dtopo file

dtopodir = '../../dtopo/dtopofiles'
dtopofile = os.path.join(dtopodir, 'ASCE_SIFT_Region2.dtt3')
fgmax.interp_dz(dtopofile, dtopo_type=3)
print(f'dz ranges from {fgmax.dz.min()} to {fgmax.dz.max()}')
fgmax.B0 = fgmax.B - fgmax.dz

# Define some colormaps:

# colormap for depth h onshore and surface eta offshore:
bounds_depth_eta = array([1e-6,1,2,5,10,15,20])

cmap_depth_eta = mpl.colors.ListedColormap([[.7,.7,1],[.5,.5,1],[0,0,1],
                 [1,.7,.7], [1,.4,.4], [1,0,0]])

# Set color for value exceeding top of range to purple:
cmap_depth_eta.set_over(color=[1,0,1])

# Set color for land points without inundation to transparent if on image:
cmap_depth_eta.set_under(color=[0,0,0,0])

norm_depth_eta = mpl.colors.BoundaryNorm(bounds_depth_eta, cmap_depth_eta.N)


# colormap for speed:
bounds_speed = np.array([1e-6,1,3,6,9,12,15,18])
cmap_speed = mpl.colors.ListedColormap([[.9,.9,1],[.6,.6,1],
                [.3,.3,1],[0,0,1], [1,.8,.8],
                [1,.6,.6], [1,0,0]])

# Set color for value exceeding top of range to purple:
cmap_speed.set_over(color=[1,0,1])

# Set color for land points without inundation to transparent if on image:
cmap_speed.set_under(color=[0,0,0,0])

norm_speed = mpl.colors.BoundaryNorm(bounds_speed, cmap_speed.N)

# colormap for stays_dry points in kmz:
bounds_dry = np.array([0,1e-6])
cmap_dry = mpl.colors.ListedColormap([[.7,1,.7]])
# Set color for land points without inundation to light green:
cmap_dry.set_under(color=[.7,1,.7])
norm_dry = mpl.colors.BoundaryNorm(bounds_dry, cmap_dry.N)


# start making plots:

# temporary directory for files, which will be deleted at end:
kml_dir = os.path.join(os.getcwd(), 'kmlfiles')
print('Will send kml file and plots to kml_dir = \n  ', kml_dir)
os.system('mkdir -p %s' % kml_dir);

close_figs = True

onshore = fgmax.B0 > 0
h_onshore = where(onshore, fgmax.h, nan)
eta_offshore = ma.masked_where(onshore, fgmax.h+fgmax.B0)

h_wet_onshore = ma.masked_where(h_onshore==0., h_onshore)
#print('fgmax.x, fgmax.y shapes: ',fgmax.x.shape, fgmax.y.shape)
#print('+++ h_wet_onshore.shape = ',h_wet_onshore.shape)
png_filename=kml_dir+'/h_onshore_max_for_kml.png'
fig,ax,png_extent,kml_dpi = kmltools.pcolorcells_for_kml(fgmax.X, fgmax.Y,
                                                 h_wet_onshore.T,
                                                 png_filename=png_filename,
                                                 dpc=2, cmap=cmap_depth_eta, norm=norm_depth_eta)
if close_figs: close('all')


png_filename=kml_dir+'/eta_offshore_max_for_kml.png'
fig,ax,png_extent,kml_dpi = kmltools.pcolorcells_for_kml(fgmax.x, fgmax.y,
                                                 eta_offshore.T,
                                                 png_filename=png_filename,
                                                 dpc=2, cmap=cmap_depth_eta, norm=norm_depth_eta)
if close_figs: close('all')



speed = ma.masked_where(fgmax.h==0., fgmax.s)
png_filename = '%s/speed_max_for_kml.png' % kml_dir
fig,ax,png_extent,kml_dpi = kmltools.pcolorcells_for_kml(fgmax.x, fgmax.y,
                                                 speed.T,
                                                 png_filename=png_filename,
                                                 dpc=2, cmap=cmap_speed, norm=norm_speed)
if close_figs: close('all')


stays_dry = ma.masked_where(fgmax.h>0., fgmax.h)
png_filename = '%s/stays_dry_for_kml.png' % kml_dir
fig,ax,png_extent,kml_dpi = kmltools.pcolorcells_for_kml(fgmax.x, fgmax.y,
                                                 stays_dry.T,
                                                 png_filename=png_filename,
                                                 dpc=2, cmap=cmap_dry, norm=norm_dry)
if close_figs: close('all')


# ### Make colorbars for kml files


kmltools.kml_build_colorbar('%s/colorbar_depth_eta.png' % kml_dir, cmap_depth_eta,
                           norm=norm_depth_eta, label='meters', title='h/eta', extend='max')
kmltools.kml_build_colorbar('%s/colorbar_speed.png' % kml_dir, cmap_speed,
                           norm=norm_speed, label='meters / second', title='speed', extend='max')
if close_figs: close('all')


# ### Make the kml file to display the png files and colorbars



png_files=['h_onshore_max_for_kml.png', 'speed_max_for_kml.png','stays_dry_for_kml.png',
           'eta_offshore_max_for_kml.png']
png_names=['max depth onshore','max speed','stays dry',
           'eta_offshore']
cb_files = ['colorbar_depth_eta.png', 'colorbar_speed.png']
cb_names = ['colorbar_depth_eta', 'colorbar_speed']



fname = os.path.join(kml_dir, name+'.kml')
kmltools.png2kml(png_extent, png_files=png_files, png_names=png_names,
                 name=name, fname=fname,
                 radio_style=False,
                 cb_files=cb_files, cb_names=cb_names)


# Create .kmz file including all plots

savedir = os.getcwd()
with contextlib.chdir(kml_dir):
    files = glob.glob('*.kml') + glob.glob('*.png')
    print('kmz file will include:')
    for file in files:
        print('    %s' % os.path.split(file)[-1])

    fname_kmz = '%s_fgmax%s.kmz' % (run_name, fgno)
    with zipfile.ZipFile(fname_kmz, 'w') as zip:
        for file in files:
            zip.write(file)

    path_kmz = os.path.join(savedir, fname_kmz)
    shutil.move(fname_kmz, path_kmz)
    print('Created %s' % os.path.abspath(path_kmz))

# remove temp directory:
shutil.rmtree(kml_dir)
