"""
Plot the water depth h and the water surface h+B in a couple different
ways to illustrate what happens when the grid refinement level changes.
"""

from pylab import *
import os
from clawpack.pyclaw.gauges import GaugeSolution

outdir = '_output1c'  # best illustrates changes in topo with AMR level

if not os.path.isdir(outdir):
    # if there's no local version, assume fetch_sample_results.py was run:
    outdir = f'sample_results/{outdir}'


# illustrate for the offshore gauge 101 and the onshore gauge 102:
gaugenos = [101, 102]

# ======================================================================
# plot showing refinement level at gauge location (as time series)
# not often needed, but here it's used to explain discontinuities in
# h time series offshore or in eta time series onshore

for kg,gaugeno in enumerate(gaugenos):
    fig,ax = subplots(figsize=(12,6))
    gauge = GaugeSolution(gauge_id=gaugeno, path=outdir)
    t = gauge.t / 60.   # convert to minutes
    tfinal = t[-1]      # final time
    level = gauge.level

    ax.plot(t, level, 'b', linewidth=1)

    ax.set_ylabel('AMR level)', fontsize=12)
    ax.set_xlabel('time (minutes)',fontsize=12)

    gauge_title_string = f'Gauge {gaugeno} from {outdir}' \
        + '\n AMR Level at longitude x = %.5f, latitude y = %.5f' \
                    % (gauge.location[0], gauge.location[1])
    ax.set_title(gauge_title_string, fontsize=15)

    ax.set_xlim(-5, tfinal)
    ax.set_ylim(0,9)

    ax.grid(True)

    # label with resolutions of each level:
    res = ['4 arcmin', '2 arcmin', '24 arcsec', '12 arcsec',
           '6 arcsec', '3 arcsec', '1 arcsec', '1/3 arcsec']
    for k in range(len(res)):
        level = k+1
        text(61, level+0.05, f'Level {level}: {res[k]}',
             ha='left', va='bottom', color='b', fontsize=12)

    if 1:
        fname = f'Gauge{gaugeno}_AMRlevel.png'
        savefig(fname)
        print('Created ', fname)



# ======================================================================
# plot showing B and eta together with water in between

for kg,gaugeno in enumerate(gaugenos):
    fig,ax = subplots(figsize=(12,6))
    gauge = GaugeSolution(gauge_id=gaugeno, path=outdir)
    t = gauge.t / 60.   # convert to minutes
    tfinal = t[-1]      # final time
    q = gauge.q
    h = q[0,:]          # time series for depth h
    eta = q[-1,:]       # time series for surface eta (last component of q)
    B = eta - h         # time series for topography B

    fill_between(t, B, -10, color=[.8,1,.6])  # land below topo is green
    fill_between(t, B, eta, color=[.7,.7,1])  # water between B and eta is blue

    ax.plot(t, B, 'g', label='topo/bathy B', linewidth=2)
    ax.plot(t, eta, 'b', label='surface eta')

    ax.set_ylabel('elevation relative to topo vdatum (meters)', fontsize=12)
    ax.set_xlabel('time (minutes)',fontsize=12)

    gauge_title_string = f'Gauge {gaugeno} from {outdir}' \
        + '\n B and eta at longitude x = %.5f, latitude y = %.5f' \
                    % (gauge.location[0], gauge.location[1])
    ax.set_title(gauge_title_string, fontsize=15)

    ax.set_xlim(-5, tfinal)
    ax.set_ylim(-10, 20)

    ax.legend(loc='upper right', framealpha=1)

    ax.grid(True)


    if 1:
        fname = f'Gauge{gaugeno}_B_eta.png'
        savefig(fname)
        print('Created ', fname)


# ======================================================================
# plot showing h and eta together but with different vertical scales:

for kg,gaugeno in enumerate(gaugenos):
    fig,ax = subplots(figsize=(12,6))
    gauge = GaugeSolution(gauge_id=gaugeno, path=outdir)
    t = gauge.t / 60.   # convert to minutes
    tfinal = t[-1]      # final time
    q = gauge.q
    h = q[0,:]          # time series for depth h
    eta = q[-1,:]       # time series for surface eta (last component of q)
    B = eta - h         # time series for topography B
    offset = B[-1]      # B at final time

    # define lambda functions to use for secondary axis:
    eta2h = lambda eta: eta - offset
    h2eta = lambda h: h + offset

    ax2 = ax.secondary_yaxis('right', functions=(eta2h,h2eta))

    ax.plot([0,tfinal],[h[0]+offset,h[0]+offset], 'k--', \
            label='initial h = %.2fm' % h[0])


    ax.plot(t, h+offset, 'r', label='water depth h', linewidth=3)
    ax.plot(t, eta, 'b', label='surface eta')
    ax.set_ylabel('surface elevation relative to topo vdatum (meters)',
                  color='b', fontsize=12)
    ax2.set_ylabel('water depth (meters)',
                  color='r', fontsize=12)
    ax.set_xlabel('time (minutes)',fontsize=12)

    gauge_title_string = f'Gauge {gaugeno} from {outdir}' \
        + '\n h and eta at longitude x = %.5f, latitude y = %.5f' \
                    % (gauge.location[0], gauge.location[1])
    ax.set_title(gauge_title_string, fontsize=15)

    ax.set_xlim(-5, tfinal)

    if 0:
        ylimits = ax.get_ylim()
        ytext = h[0]-offset + 0.005*(ylimits[1]-ylimits[0])
        ax.text(3.1, ytext, 'initial water depth = %.2fm' % h[0])


    ax.legend(loc='upper right', framealpha=1)

    ax.grid(True)


    if 1:
        fname = f'Gauge{gaugeno}_h_eta.png'
        savefig(fname)
        print('Created ', fname)
