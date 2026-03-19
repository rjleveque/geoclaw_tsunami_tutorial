"""
Create a 3D plot of topography using PyVista
with a slider to adjust sea_level, to help visualize effect of
subsidence (or sea level rise) on this location, and to better understand
topographic features.

Some tips to using this:
    - With make_snapshots = make_html = False, the view is interactive.
      With make_snapshots = True, a set of screenshots is made as png files.
      With make_html = True, an interactive html file is made (for sea_level=0)

    - When running interactively, whenever the slider bar is moved the current
      camera_position is printed. This is useful to select an initial position
      that you like (then copy and paste it into this script)

    - Can use an image as texture rather than coloring topography by elevation,
      by setting use_image_texture to True.
      In this case there is an unlabelled checkbox on the interactive view
      (lower left corner) to toggle the image on or off.

"""

from pylab import *
import pyvista as pv
from clawpack.geoclaw import topotools

# Some parameters to modify as described in pyvista.md

warpfactor = 3  # amplification of elevations
make_snapshots = False  # True to save a set of png files for different slr
make_html = False  # True to save an interactive html file
use_image_texture = True  # True to drape an image over the topo

# load the topography
topo = topotools.Topography('../topo/topofiles/Copalis_13s.asc')

# crop it to the fgmax/fgout regions used in CopalisBeach/example2:
fg_extent = [-124.195, -124.155, 47.11, 47.145]
topo = topo.crop(fg_extent)

z = array([0.])
x = (topo.x - topo.x[0]) * 111e3 * cos(topo.y.mean()*pi/180)
y = -(topo.y - topo.y[0]) * 111e3
print('xmax = %.1fm, ymax = %.1fm' % (x.max(),y.max()))
X,Y,Z = meshgrid(x, y, z, indexing='ij')
topoxyz = pv.StructuredGrid(X,Y,Z)

B = flipud(topo.Z)

# For regions with steep topography it may be useful to chop off hilltops:
Bmax = 50.
B = minimum(B, Bmax)

# warp the topo surface:
topoxyz.point_data['B'] = B.flatten(order='C')
topowarp = topoxyz.warp_by_scalar('B', factor=warpfactor)


global etamesh, texturesurf

p = pv.Plotter(off_screen=make_snapshots)

# color mesh based on elevation:
scalar_bar_args={'title_font_size':50, 'label_font_size':30,
                 'title':'Topography elevation (meters)'}
toposurf = p.add_mesh(topowarp,cmap='gist_earth',clim=(-5,20),
                      scalar_bar_args=scalar_bar_args)

if use_image_texture:
    # Add GE image as texture:
    GE_file ='fg_rectangle.jpg'
    GE_extent = fg_extent  # the [x1,x2,y1,y2] extent of the image

    texture = pv.read_texture(GE_file)

    # map points from lon-lat to meters from lower left corner:
    meanlat = topo.y.mean()  # mean latitude for aspect ratio
    x1,x2 = (asarray(GE_extent[:2]) - topo.x[0]) * 111e3 * cos(meanlat*pi/180)
    y1,y2 = (asarray(GE_extent[2:]) - topo.y[0]) * 111e3

    origin = (x1, y1, 0.)   # bottom left corner
    point_u = (x2, y1, 0.)  # bottom right corner
    point_v = (x1, y2, 0.)  # top right corner

    mapped_surf = topowarp.texture_map_to_plane(origin=origin,
                                                point_u=point_u,
                                                point_v=point_v)
    texturesurf = p.add_mesh(mapped_surf,texture=texture, opacity=1)


# initial eta plot:
sea_level = 0.
eta = where(B < sea_level, sea_level, nan)
topoxyz.point_data['eta'] = eta.flatten(order='C')
etawarp = topoxyz.warp_by_scalar('eta', factor=warpfactor)
etamesh = p.add_mesh(etawarp,color='c')

p.window_size = (2500,1500)

# initial camera position:
p.camera_position =  [(723.397, -7287.272, 1911.49), (1762.85, -2652.806, -267.542), (0.061, 0.413, 0.908)]

def set_sea_level(sea_level):
    global etamesh
    # replace water surface etamesh with a new version based on sea_level:
    eta = where(B < sea_level, sea_level, nan)
    topoxyz.point_data['eta'] = eta.flatten(order='C')
    etawarp = topoxyz.warp_by_scalar('eta', factor=warpfactor)
    p.remove_actor(etamesh)
    etamesh = p.add_mesh(etawarp,color='c')
    title_string = \
        f'Copalis Beach topography with vertical exageration x{warpfactor}' \
        + f'\nsea_level = {sea_level:.2f} m relative to MHW '
    p.add_title(title_string, font_size=20)

    if 1:
        # round off entries in p.camera_position and print out, so user
        # can copy and paste into this script once good position is found:
        camera_position = list(p.camera_position)
        for i,a in enumerate(camera_position):
            b = []
            for j in range(len(a)):
                b.append(round(a[j],3))
            camera_position[i] = tuple(b)
        print('p.camera_position = ', camera_position)


if make_html:
    slr = 0.  # set the desired sea_level for the html file
    set_sea_level(slr)
    if use_image_texture:
        fname = f'CopalisTopo_mhw{100*slr:03.0f}cm_with_image.html'
    else:
        fname = f'CopalisTopo_mhw{100*slr:03.0f}cm.html'
    p.export_html(fname)
    print('Created ', fname)

elif make_snapshots:
    for slr in [0,1,2,3]:
        set_sea_level(slr)
        p.add_title(f'MHW after {slr:.2f} m subsidence (or sea level rise)')
        fname_png = f'CopalisTopo_mhw{100*slr:03.0f}cm.png'
        p.screenshot(fname_png)
        print('Created ',fname_png)
    p.close()

else:
    # interactive view
    print('interactive... close window to quit')
    p.add_title('MHW after sea level rise / subsidence')

    # sea_level slider bar:
    p.add_slider_widget(set_sea_level, [-5,5], value=0,
                        title='Change in Sea Level (m)',
                        pointa=(0.1,0.2), pointb=(0.4,0.2),
                        slider_width=0.02, tube_width=0.005)


    if use_image_texture:

        # add checkbox to interactive version to toggle image on or off:

        def toggle_vis(flag) -> None:
            texturesurf.SetVisibility(flag)

        p.add_checkbox_button_widget(toggle_vis, value=True,
                    position=(90,10), color_on='green')


    p.show()  # show interactive view, close external window to exit
