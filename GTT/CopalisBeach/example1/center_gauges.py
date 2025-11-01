"""
Take a set of gauges specified as in setrun.py and adjust them to be
centered in grid cells that are dx by dy and that are an integer number
of dx or dy away from x_edge and y_edge, respectively.

Then print the new gauge locations out in a way that can be pasted back
into setrun.py.

See  https://www.clawpack.org/nearshore_interp.html
for details on why this might be needed.

See also the documentation in the module center_points.py used below,
which can be used more generally for centering arbitrary points.

Typically (dx,dy) should be the finest refinement level expected at the
gauge location over the time period when the gauge output will be used.
Note that (dx,dy) may need to be chosen differently for different gauges.

Note that the domain need not be refined to this level everywhere in order
for grids at resolution (dx,dy) to be offset from the edges of the domain
by integer multiples of (dx,dy).

The initial "desired" points may be shifted by as much as (dx/2, dy/2) to
achieve this centering.
"""

import numpy as np
from clawpack.geoclaw import center_points

# original "desired" locations:
gauges = []
gauges.append([101, -124.19, 47.116, 0., 1e9])
gauges.append([102, -124.18, 47.116, 0., 1e9])
gauges.append([103, -124.1706, 47.116, 0., 1e9])

gauges_array = np.array(gauges)

x_desired = gauges_array[:,1]
y_desired = gauges_array[:,2]
x_edge = -128.5
y_edge = 45.

# center in 1/3" cells:
#dx = 1/(3*3600.)
#dy = 1/(3*3600.)

# center in 3" cells (and also in 1" and 1/3"):
dx = 3/3600.
dy = 3/3600.

x_centered, y_centered = center_points.adjust_xy(x_desired, y_desired,
                                                 x_edge, y_edge, dx, dy,
                                                 verbose=False)

gauges_array[:,1] = x_centered
gauges_array[:,2] = y_centered

for k in range(len(gauges)):
    print('gauges.append([%i, %.7f, %.7f, %g, %g])' % tuple(gauges_array[k,:]))


