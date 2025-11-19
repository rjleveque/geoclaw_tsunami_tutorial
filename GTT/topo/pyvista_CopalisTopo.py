"""
Create a 3D plot of topography using PyVista

This version just plots the topo using a colormap based on elevation.

Some tips to using this:
    - With fname_png == None this opens an interactive window
      Provide a file name to instead create a screenshot
    - the camera_position was chosen using pyvista_CopalisTopo_sealevel.py,
      which prints out the camera_position whenever the slider bar is moved,
      allowing you to capture a good position and then paste it in to this file.
    - You can add a water surface at sea_level = 0 (or some other level)
      as indicated below, but this hides the topography underneath.
"""

from pylab import *
import pyvista as pv
from clawpack.geoclaw import topotools

fname_png = None  # None ==> interactive, or provide file name for screenshot

topo = topotools.Topography('../topo/topofiles/Copalis_13s.asc')
topo = topo.crop([-124.19486111, -124.15597222, 47.10791667, 47.14597222])

z = array([0.])
x = (topo.x - topo.x[0]) * 111e3 * cos(topo.y.mean()*pi/180)
y = -(topo.y - topo.y[0]) * 111e3
print('xmax = %.1fm, ymax = %.1fm' % (x.max(),y.max()))
X,Y,Z = meshgrid(x, y, z, indexing='ij')
topoxyz = pv.StructuredGrid(X,Y,Z)

B = flipud(topo.Z)  # should work for GeoClaw topofiles

# For regions with steep topography it may be useful to chop off hilltops:
Bmax = 50.
B = minimum(B, Bmax)

topoxyz.point_data['B'] = B.flatten(order='C')
warpfactor = 3  # amplification of elevations
topowarp = topoxyz.warp_by_scalar('B', factor=warpfactor)

p = pv.Plotter()
p.add_mesh(topowarp,cmap='gist_earth',clim=(-5,20))
p.add_title(f'Copalis Beach area with \nvertical amplification factor {warpfactor}',
            font_size=20)

if 0:
    # add water surface at some level:
    sea_level = 0.
    eta = where(B < sea_level, sea_level, nan)
    topoxyz.point_data['eta'] = eta.flatten(order='C')
    etawarp = topoxyz.warp_by_scalar('eta', factor=warpfactor)
    etamesh = p.add_mesh(etawarp,color='c')

p.camera_position =  [(723.397, -7287.272, 1911.49), (1762.85, -2652.806, -267.542), (0.061, 0.413, 0.908)]

p.window_size = (2500,1500)

if fname_png is None:
    # interactive view  (Close window to quit)
    p.show()
else:
    p.screenshot(fname_png)
    print('Created ',fname_png)
    p.close()
