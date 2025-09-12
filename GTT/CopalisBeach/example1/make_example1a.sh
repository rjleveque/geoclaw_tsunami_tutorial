#!/bin/bash

# clean up any old results:
rm -rf _output1a _plots1a

# make sure the code is compiled:
make .exe -f Makefile1a | tee sample_results/geoclaw_output1a.txt

# create .data files (appending screen output):
make data -f Makefile1a | tee -a sample_results/geoclaw_output1a.txt

# run GeoClaw:
echo ==========> Running GeoClaw...
make output -f Makefile1a | tee -a sample_results/geoclaw_output1a.txt

# plot the results:
echo ==========> Plotting results...
make plots -f Makefile1a | tee -a sample_results/geoclaw_output1a.txt

cp -f _plots1a/movie_fig0.mp4 sample_results/example1a_movie_fig0.mp4
cp -f _plots1a/movie_fig1.mp4 sample_results/example1a_movie_fig1.mp4

# To do the same for other examples, use make_all.sh

