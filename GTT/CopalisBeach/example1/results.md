---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Sample results for Copalis Beach

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

The directory `$GTT/CopalisBeach/example1`
contains some initial GeoClaw `setrun` and `setplot` functions to start
exploring tsunami modeling.

See [](README) for more about these examples.

#### Fetch the sample results

The code cell hidden below runs `fetch_sample_results.py` to download the
subdirectory `sample_results` that provides the figures shown on this page.

```{code-cell}
:tags: [hide-input, hide-output]
run fetch_sample_results.py
```

:::{warning}
This page may be broken due to issues with downloading sample results
needed for displaying the plots when building the book on Github.
If plots are missing, please check back later.
:::

The `setrun` files defined in this directory are all nearly identical, but
allow a different number of refinement levels.  The coarsest (3-level) case
runs quickly and shows how things are refined in most of the domain.
The other versions add refinement levels only near Copalis Beach, and so the
full domain plots look nearly identical and are not shown in the videos below.

See [](setrun_description) for detailed description of the `setrun1a.py`
script, and [](output1a_annotated) for more discussion of the output.

## Run times

These runs were done on a Macbook Pro with the M1 chip and 6 OpenMP threads.

|example | finest-level grid resolution | elapsed wall time | Total CPU time |
|---:|---:|---:|---:|
|setrun1a |24 arcsec  (level 3)| 35 seconds | 181 seconds |
|setrun1b | 6 arcsec  (level 5)| 314 seconds | 1716 seconds |
|setrun1c | 1 arcsec  (level 7)| 465 seconds | 2602 seconds |
|setrun1d | 1/3 arcsec  (level 8)| 1780 seconds | 10275 seconds |

More details about the run time is summarized in a table that gets written
to the `timing.txt` at the end of a run (this information is also printed
to the screen).  For example, here's `_output1d/timing.txt`:


    ============================== Timing Data ==============================

    Integration Time (stepgrid + BC + overhead)
    Level           Wall Time (seconds)    CPU Time (seconds)   Total Cell Updates
      1                     1.241                  2.417            0.999E+06
      2                     2.487                  9.488            0.115E+08
      3                    36.296                190.706            0.271E+09
      4                   183.886               1077.718            0.170E+10
      5                    13.987                 62.963            0.950E+08
      6                    33.994                169.437            0.276E+09
      7                   192.710               1065.166            0.169E+10
      8                  1249.079               7478.786            0.116E+11
    total                1713.681              10056.682            0.156E+11

    All levels:
    stepgrid             1673.687               9936.121    
    BC/ghost cells         18.104                 98.417
    Regridding             51.003                162.183  
    Output (valout)         0.361                  0.341  

    Total time:          1779.518              10275.146  
    Using  6 thread(s)

    Note: The CPU times are summed over all threads.
          Total time includes more than the subroutines listed above
    Note: timings are also recorded for each output step
          in the file timing.csv.

Note that more than 15 billion grid cells were updated during this computation
(counting each grid cell on every level for each time step on that level).
You can also see that the majority of the work was done on the finest Level 8
grids.

You can also view plots of these timing results for the
various runs from the link that shows up at the
bottom of the `_PlotIndex.html` file in each `_plots` directory.

Here's just one of the timing plots, from `_plots1d` for the finest level run:

![](./sample_results/_plots1d/timing_figures/timing_CumCPUTime.png)

This shows the cumulative CPU time (which are collected in
the file `timing.csv` in the `_output` directory at each output time, and
for these runs output every 10 minutes was specified).  Again we see that
the majority of the work was done on Level 8.  Note also the gray section
above the yellow Level 8 section on the plot.  This shows the amount of time
spent on "overhead" related to the way the AMR is implemented.  This cost
of using AMR is tiny compared to the coast savings inherent in putting finer
grids only where they are really needed!


Four `_plots` directories are created if you run the `make_all.sh` script,
as described in [](README).

:::{note}
Archived versions of all of these `_plots` directories are fetched to the
`sample_results` directory if you run the `fetch_sample_results.py` script,
as described in [](README), so that you can view them without needing to
perform all the runs. *(Script is still being debugged.)*
It is these versions that supply the illustrations on this page.
:::


## Comparison of the inundation

Shown around Copalis Beach with different finest-level resolution,
at time 50 minutes.

### 24" resolution

![](./sample_results/_plots1a/frame0005fig1.png)

### 6" resolution

![](./sample_results/_plots1b/frame0005fig1.png)


### 1" resolution

![](./sample_results/_plots1c/frame0005fig1.png)

### 1/3" resolution

![](./sample_results/_plots1d/frame0005fig1.png)


## Videos


### Full domain from 3-level run

Computed using  `setrun1a.py` with 24" resolution around Copalis

The other versions add refinement levels only near Copalis Beach, and so the
full domain plots look nearly identical and are not shown below.

Right click and select "Show all controls" to find the Play button.

![](./sample_results/_plots1a/movie_fig0.mp4)

### Inundation around Copalis from 3-level run

Computed using  `setrun1a.py` with 24" resolution around Copalis

Right click and select "Show all controls" to find the Play button.

![](./sample_results/_plots1a/movie_fig1.mp4)



### Inundation around Copalis from 5-level run

Computed using  `setrun1b.py` with 6" resolution around Copalis

Right click and select "Show all controls" to find the Play button.

![](./sample_results/_plots1b/movie_fig1.mp4)



### Inundation around Copalis from 7-level run

Computed using  `setrun1c.py` with 1" resolution around Copalis

Right click and select "Show all controls" to find the Play button.

![](./sample_results/_plots1c/movie_fig1.mp4)



### Inundation around Copalis from 8-level run

Computed using  `setrun1d.py` with 1/3" resolution around Copalis

Right click and select "Show all controls" to find the Play button.

![](./sample_results/_plots1d/movie_fig1.mp4)
