"""
Create a 3D plot of topography using PyVista
with a slider to adjust sea_level, to help visualize effect of
subsidence (or sea level rise) on this location, and to better understand
topographic features.

Some tips to using this:
    - With make_snapshots == False, running this produces an interactive view
      With make_snapshots == True, a set of screenshots is made instead.
    - Whenever the slider bar is moved the current camera_position is printed,
      useful to select an initial position you like (copy and paste)
    - Can use image as texture rather than coloring topography as elevation,
      by setting use_image_texture to True

"""

from pylab import *
import pyvista as pv
from clawpack.geoclaw import topotools

topo = topotools.Topography('../topo/topofiles/Copalis_13s.asc')

# extent to be used for fgmax and fgout in CopalisBeach/example2:
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

topoxyz.point_data['B'] = B.flatten(order='C')
warpfactor = 3  # amplification of elevations
topowarp = topoxyz.warp_by_scalar('B', factor=warpfactor)


global etamesh

make_snapshots = False
use_image_texture = False

p = pv.Plotter(off_screen=make_snapshots)

if use_image_texture:
    # Add GE image as texture:
    GE_file ='fg_rectangle.jpg'
    GE_extent = fg_extent

    texture = pv.read_texture(GE_file)

    # map from lon-lat to meters from corner:
    x1,x2 = (asarray(GE_extent[:2]) - topo.x[0]) * 111e3 * cos(topo.y.mean()*pi/180)
    y1,y2 = (asarray(GE_extent[2:]) - topo.y[0]) * 111e3

    o = (x1, y1, 0.)
    u = (x2, y1, 0.)
    v = (x1, y2, 0.)

    mapped_surf = topowarp.texture_map_to_plane(o, u, v)
    p.add_mesh(mapped_surf,texture=texture)
else:
    p.add_mesh(topowarp,cmap='gist_earth',clim=(-5,20))


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
    #p.clear() # causes seg fault
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

if not make_snapshots:
    p.add_title('MHW after sea level rise / subsidence')
    p.add_slider_widget(set_sea_level, [-5,5], value=0,
                        title='Change in Sea Level (m)',
                        pointa=(0.1,0.1), pointb=(0.4,0.1),)
    p.show()
else:
    for slr in [0,1,2,3]:
        set_sea_level(slr)
        p.add_title('MHW after %i m subsidence (or sea level rise)' % slr)
        fname_png = 'CopalisTopo_mhw%im.png' % slr
        p.screenshot(fname_png)
        print('Created ',fname_png)
    p.close()
