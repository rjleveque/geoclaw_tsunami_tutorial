from pylab import *
import os
from clawpack.pyclaw.gauges import GaugeSolution

rundir = '.'  # to use the results in _output1a, etc from this directory
#rundir = 'sample_results'  # to use the results from the data repository
outdir_most = f'{rundir}/_output'

#example1_dir = '../example1'
example1_dir = '../example1/sample_results'
outdir_example1d = f'{example1_dir}/_output1d'

outdirs = [f'{example1_dir}/_output1d', f'{rundir}/_output']
c = ['k','r']  # colors for lines
labels = ['GeoClaw AMR from example1d', 'GeoClaw with MOST grids']

figure(500,figsize=(10,8))
clf()

gaugenos = [101, 102, 103]

for kg,gaugeno in enumerate(gaugenos):
    subplot(3,1,kg+1)
    for ke,outdir in enumerate(outdirs):
        gauge = GaugeSolution(gauge_id=gaugeno, path=outdir)
        exlabel = labels[ke]
        if gaugeno == 101:
            # offshore gauge, plot eta
            plot(gauge.t/60., gauge.q[-1,:], c[ke], label=exlabel)
            title_string = f'Surface eta at offshore Gauge {gaugeno}'
        elif gaugeno in [102,103]:
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
