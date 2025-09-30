from pylab import *
import os
from clawpack.pyclaw.gauges import GaugeSolution

rundir = '.'  # to use the results in _output1a, etc from this directory
#rundir = 'sample_results'  # to use the results from the data repository


c = ['k','g','b','r']  # colors for lines
resolution = ['24','6','1','1/3']  # finest grid resolution in arcsec
    
figure(500,figsize=(10,8))
clf()

gaugenos = [101, 102]

for kg,gaugeno in enumerate(gaugenos):
    subplot(2,1,kg+1)
    for ke,exno in enumerate(['1a','1b','1c','1d']):
        outdir = os.path.join(rundir, f'_output{exno}')
        gauge = GaugeSolution(gauge_id=gaugeno, path=outdir)
        exlabel = f'from run {exno}, finest resolution {resolution[ke]} arcsec'
        if gaugeno == 101:
            # offshore gauge, plot eta
            plot(gauge.t/60., gauge.q[-1,:], c[ke], label=exlabel)
            title_string = f'Surface eta at offshore Gauge {gaugeno}'
        elif gaugeno == 102:
            # onshore gauge, plot h
            plot(gauge.t/60., gauge.q[0,:], c[ke], label=exlabel)
            title_string = f'Water depth at onshore Gauge {gaugeno}'

    grid(True)
    legend(loc='upper right', framealpha=1)
    #xlim(0,2)
    #ylim(-2,4)
    xlabel('Minutes after earthquake')
    ylabel('meters')
    title(title_string, fontsize=15)

tight_layout()
fname = 'GaugeComparison.png'
savefig(fname)
print('Created ', fname)
