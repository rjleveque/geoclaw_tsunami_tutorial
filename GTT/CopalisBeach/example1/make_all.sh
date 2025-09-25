#!/bin/bash

# Run all examples for which _output directory does not exist.
# Remove the _output directory to force re-running.

# Note that rather than running all the codes, you can download the plots
# from all four simulations to a new subdirectory sample_results via:
#    $ python fetch_sample_results.py

for EX in 1a 1b 1c 1d; do
    if [ ! -d "./_output$EX" ]; then
        echo "==========> Working on example $EX"
        rm -rf _output$EX _plots$EX
        make .exe -f Makefile$EX | tee geoclaw_output$EX.txt
        make data -f Makefile$EX | tee -a geoclaw_output$EX.txt
        make output -f Makefile$EX | tee -a geoclaw_output$EX.txt
        make plots -f Makefile$EX | tee -a geoclaw_output$EX.txt
    else
        echo "==========> Directory _output$EX exists, not re-running"
    fi
done

