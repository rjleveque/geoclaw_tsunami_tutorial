"""
Script to compare time series at gauges between two different GeoClaw runs.
with results in outdir and outdir2.

Set up to produce plots for 3 gauges in one figure for
$GTT/CopalisBeach/exercise1

Modify outdir and outdir2 to compare runs varying different things. 
You might also want to modify `labels` to give properly descriptive labels
in the figure legends.
"""

from pylab import *
import os
from clawpack.pyclaw.gauges import GaugeSolution

GTT = os.environ['GTT']

rundir = '.'  # to use the results from this directory
outdir = f'{rundir}/_output'

# compare to the sample results for exercise 1:
rundir2 = f'{GTT}/CopalisBeach/exercise1/sample_results'
outdir2 = f'{rundir2}/_output'

outdirs = [outdir, outdir2]
c = ['k','r']  # colors for lines
labels = ['my run', 'sample results']

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
    xlabel('Minutes after earthquake')
    ylabel('meters')
    title(title_string, fontsize=15)

tight_layout()
fname = 'GaugeComparison.png'
savefig(fname)
print('Created ', fname)
