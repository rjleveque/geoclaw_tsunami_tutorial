"""
Module for converting MOST data and output to GeoClaw format.

This is Work In Progress -- haven't tested the output formats lately.

"""

import os, glob, re
from clawpack.geoclaw import topotools
import numpy as np

def read_most_grid(fname, longitude_shift= -360., verbose=True):
    """
    Read grid / topo file in MOST format and return object of class
    geoclaw.topotools.Topography

    :Input:
     - fname (str): filename of MOST file
     - longitude_shift (float): shift x values by this amount,
       normally either 0 to keep in longitude East or
       -360 to convert from longitude East to West
     - verbose (bool): print out dx,dy and size of topo array.

    :Output:
     - topo: object of class geoclaw.topotools.Topography

    You can easily plot the resulting topo object with e.g.:
        topo.plot()  # see documentation for optional arguments
    You can save it as a GeoClaw topofile using, e.g.:
        topo.write(new_fname, topo_type=3, header_style='asc', Z_format='%.3f')
    to create a file in ARCGIS .asc format with mm precision in Z values.
    """
    f = open(fname).readlines()
    mn = f[0].split()
    nx = int(mn[0])
    ny = int(mn[1])
    x = np.array([float(f[j]) for j in range(1,nx+1)])
    y = np.array([float(f[j]) for j in range(nx+1,nx+ny+1)])
    nheader = nx + ny + 1
    Z = np.loadtxt(fname,skiprows=nheader)

    x = x + longitude_shift  # e.g. to shift for longitude E to W
    Z = -Z  # since MOST topo is negative on shore, positive depth offshore

    dxarray = np.diff(x)
    dyarray = np.diff(y)
    dxmin = dxarray.min()
    dxmax = dxarray.max()
    dxave = dxarray.mean()
    dymin = dyarray.min()
    dymax = dyarray.max()
    dyave = dyarray.mean()

    rtol = 1e-3
    if (dxmax - dxmin) > rtol * dxave:
        print('*** WARNING: x  values may not be equally spaced')
        print(f'    dxmin={dxmin}, dxmax={dxmax}')
    if (dymax - dymin) > rtol * dyave:
        print('*** WARNING:  y values may not be equally spaced')
        print(f'    dymin={dymin}, dymax={dymax}')
    if abs(dxave-dyave) > rtol * dxave:
        print(f'*** WARNING: dxave = {dxave} and dyave = {dyave} are not equal')
        print('*** Assuming they should be')

    # force x and y to be equally spaced:
    x = np.linspace(x[0], x[-1], nx)
    y = np.linspace(y[0], y[-1], ny)

    topo = topotools.Topography()
    topo.set_xyZ(x,y,Z)
    dx,dy = topo.delta  # calculated from topo.x and topo.y
    if verbose:
        dxsec = dx * 3600
        dysec = dy * 3600
        print(f'Returning topo with dx = {dx:.6e} = {dxsec:.4f} arcseconds')
        print(f'                and dy = {dy:.6e} = {dysec:.4f} arcseconds')
        print(f'                with {nx} points in x and {ny} points in y')

    return topo

# =================================================
# Functions below have not been tested recently...

def most2fortt(fnameprefix):
    """
    Converts MOST output files to fort.t files.
    """
    files = glob.glob(r'%s*' % fnameprefix)
    files.sort()
    s = r"%s(?P<hours>[0-9]*)h(?P<minutes>[0-9]*)m(?P<seconds>[0-9]*)s" \
          % fnameprefix
    regexp = re.compile(s)
    frameno = 1
    for fname in files:
        result = regexp.search(fname)
        try:
            hours = result.group("hours")
            minutes = result.group("minutes")
            seconds = result.group("seconds")
        except:
            print("*** Cannot parse fname: ",fname)
            raise
        t = int(hours)*3600. + int(minutes)*60. + int(seconds)
        fortname = "fort.t" + str(frameno).zfill(4)
        f = open(fortname, 'w')
        f.write("%18.8e     time\n" % t)
        f.write("%5i                  meqn\n" % 1)
        f.write("%5i                  ngrids\n" % 1)
        f.write("%5i                  ndim\n" % 0)
        f.write("%5i                  maux\n" % 2)
        f.close()
        print("Created %s from %s at time t = %s" % (fortname, fname, t))
        frameno = frameno + 1


def most2fortq(fnameprefix):
    """
    Converts MOST output files to fort.q files.
    """
    files = glob.glob(r'%s*' % fnameprefix)
    files.sort()
    frameno = 1
    for fname in files:
        f = open(fname).readlines()
        mn = f[0].split()
        ncols = int(mn[0])
        nrows = int(mn[1])
        xll = float(f[1])
        dx = float(f[2]) - xll
        xll = xll - 360.
        yll = float(f[nrows+ncols])
        dy =  float(f[nrows+ncols-1]) - yll
        if abs(dx-dy) > 1.e-6:
            print('*** WARNING: dx = ',dx,'  dy = ',dy)
        cellsize = dx

        fortname = 'fort.q' + str(frameno).zfill(4)
        f2 = open(fortname,'w')
        f2.write("%5i                  grid_number\n" % 1)
        f2.write("%5i                  AMR_level\n" % 1)
        f2.write("%5i                  mx\n" % ncols)
        f2.write("%5i                  my\n" % nrows)
        f2.write("%5i                  xlow\n" % xll)
        f2.write("%5i                  ylow\n" % yll)
        f2.write("%5i                  dx\n" % dx)
        f2.write("%5i                  dy\n" % dy)
        f2.write("\n")

        for k in range(len(f)-1, nrows+ncols, -1):
            for s in f[k].split():
                z = float(s)
                f2.write("%18.8e\n" % z)
        f2.close()
        print("Created %s from %s" % (fortname,fname))
        frameno += 1

def get_comMIT_topo(x1,x2,y1,y2, dx='1m', fname='most_topo.most'):
    r"""
    Get a topo file from the comMIT Bathymetry server, see
      http://sift.pmel.noaa.gov/ComMIT/bathymetry_help.html
    Inputs:
      - *x1, x2* (floats) extent of longitude (between 0 and 360)
      - *y1, y2* (floats) extent of latitude (between -90 and 90))
      - *dx* (float or str) cellsize in decimal degrees,
             or string such as '1m', '30s' for arcminutes or arcseconds.
        Note that etopo1 bathymetry is used to construct this file and then
        linear interpolation is used if the resolution requested is finer
        than 1 minute.  But onshore topography comes from a different database
        and may be finer.
      - *fname* (str) File name to save as.

    The result is in MOST format.
    You can convert to GeoClaw form using most2tt3, e.g.
        >>> most2geoclaw.most2tt3('most_topo.most')
    But note that this seems to create a file with topo_type == -3.

    Retrieving seems to only work for some values of x1,x2,y1,y2 and not others
    for reasons not yet understood!

    """
    import os, time
    import subprocess
    fname_most = os.path.splitext(fname)[0] + '.most'

    s = "wget -O " + fname_most + \
        " 'http://sift.pmel.noaa.gov/ComMIT/bathymetry/create.most" + \
        "?xmin=%s&xmax=%s&ymin=%s&ymax=%s&cellsize=%s'"  % (x1,x2,y1,y2,dx)

    wait_time = 3
    time.sleep(wait_time)
    subprocess.check_call(s,shell=True)
    lines = open(fname_most).readlines()
    attempts = 1
    while (len(lines) < 2) and (attempts < 5):
        print("Status: ",lines[0])
        print("Will retry in %s seconds..." % wait_time)
        time.sleep(wait_time)
        subprocess.check_call(s,shell=True)
        lines = open(fname_most).readlines()
        attempts += 1
    if attempts<5:
        print("File downloaded with dimensions: ",lines[0])
    else:
        print("Tried %s times and file not ready... " % attempts)
        print("     wait a bit and try same call again")



if __name__=='__main__':
    import sys
    most2tt3(sys.argv[1])
