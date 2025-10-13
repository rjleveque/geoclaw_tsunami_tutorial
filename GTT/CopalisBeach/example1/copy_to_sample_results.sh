#!/bin/bash

# This script is only used to archive sample_results, not needed by users
# of this tutorial in general.

# Use this after running:
#   bash make_all.sh
#   python plot_gauge_h_eta.py

# create directories if needed for copying results:
mkdir -p sample_results
mkdir -p sample_results/_output1a
mkdir -p sample_results/_output1b
mkdir -p sample_results/_output1c
mkdir -p sample_results/_output1d

# copy screen output
cp geoclaw_output*.txt sample_results/

# copy full _plots directories:
cp -r _plots* sample_results/

# copy only gauges.data and gauge time series output from _output*:
cp _output1a/gauge* sample_results/_output1a/
cp _output1b/gauge* sample_results/_output1b/
cp _output1c/gauge* sample_results/_output1c/
cp _output1d/gauge* sample_results/_output1d/

# copy plots made by gauge plotting scripts:
cp Gauge*png sample_results/
