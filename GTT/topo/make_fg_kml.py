
from clawpack.geoclaw import kmltools

fg_extent = [-124.195, -124.155, 47.11, 47.145]

name = 'fg_rectangle'
kmltools.box2kml(fg_extent, name=name, width=1)

print('   Rectangle has extent: ', fg_extent)
