#!/bin/bash

# clean up any old results:
rm -rf _output1a _plots1a

# make sure the code is compiled:
make .exe -f Makefile1a | tee geoclaw_output1a.txt

# create .data files (appending screen output):
make data -f Makefile1a | tee -a geoclaw_output1a.txt

# run GeoClaw:
echo ==========> Running GeoClaw...
make output -f Makefile1a | tee -a geoclaw_output1a.txt

# plot the results:
echo ==========> Plotting results...
make plots -f Makefile1a | tee -a geoclaw_output1a.txt

