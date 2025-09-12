#!/bin/bash

# Run all examples for which _output directory does not exist
# and copy some results into sample_results for the tutorial pages.
# Remove the _output directory to force re-running, converting a png to jpg

for EX in 1a 1b 1c 1d; do
    if [ ! -d "./_output$EX" ]; then
        echo "==========> Working on example $EX"
        rm -rf _output$EX _plots$EX
        make .exe -f Makefile$EX | tee sample_results/geoclaw_output$EX.txt
        make data -f Makefile$EX | tee -a sample_results/geoclaw_output$EX.txt
        make output -f Makefile$EX | tee -a sample_results/geoclaw_output$EX.txt
        make plots -f Makefile$EX | tee -a sample_results/geoclaw_output$EX.txt
        cp -f _plots$EX/movie_fig0.mp4 sample_results/example${EX}_movie_fig0.mp4
        cp -f _plots$EX/movie_fig1.mp4 sample_results/example${EX}_movie_fig1.mp4
        magick _plots$EX/frame0005fig1.png sample_results/example${EX}_frame0005fig1.jpg
        echo "copied some plots and videos to sample_results/sample_results/example${EX}_*"
    else
        echo "==========> Directory _output$EX exists, not re-running"
    fi
done

