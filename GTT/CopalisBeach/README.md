# CopalisBeach examples

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

The directory `$GTT/CopalisBeach`
contains some example simulations of tsunamis inundating the coastal region
around [Copalis Beach, WA (-124.1733, 47.1134)](https://maps.app.goo.gl/RW275B5TzY4oQakaA) 

## Contents

- [](example1/README), Some initial runs, illustrating different grid
  resolutions, and timeframe and gauge plots specified in `setplot.py`.
  See also these [sample results](example1/results).

- [](example2/README), More complicated examples illustrating many other
  GeoClaw features.

- [](exercise1/README), An example to try modifying yourself.

- Additional examples and exercises to appear, in particular ones
  based on a farfield event, such as
  Alaska 1964 (or AKmaxWA), Tohoku 2011, or Kamchatka 2025.

## Input files

The examples use some topofiles and a dtopofile that can be
downloaded from an online archive in order to quickly get into the
GeoClaw simulation examples.

The topofiles can be obtained by executing these commands:

    $ cd $GTT/topo
    $ python fetch_CopalisTopo.py

The dtopofiles can be obtained by executing this command:

    $ cd $GTT/dtopo
    $ python fetch_ASCE_SIFT_Region2.py
    

Alternatively, you can run these notebooks, which were used to create the files:

- [](../topo/fetch_etopo22) - creates 
  `topofiles/etopo22_30s_-130_-122_40_50_30sec.asc`
  with 15 arcsecond resolution, covering full domain
- [](../topo/CopalisTopo) - creates
  `topofiles/Copalis_13s.asc` with 1/3 arcsecond resolution
- [](../dtopo/ASCE_SIFT_Region2) - creates
  `dtopofiles/ASCE_SIFT_Region2.dtt3`, an earthquake source
  `

The hypothetical earthquake being modeled is one that was developed to mimic
a "2500-year" event on a stretch of the Cascadia margin that includes
Copalis Beach.  We use it here because it is easy to generate the dtopofile
using GeoClaw tools, as explained in the notebook linked above.

In [](exercise1/README) some suggestions are given for downloading or
creating  other CSZ earthquake source models to test for comparison.

## Why Copalis Beach?

The region around Copalis Beach is shown in the Google Earth image below:

```{image} ../topo/images/CopalisTopo0.jpg
:width: 600px
:align: center
```

This region was chosen as a relatively small-scale example of interesting
coastal topography.  Moreover it is historically important in our understanding
of past CSZ tsunamis.  The
[ghost forest](https://en.wikipedia.org/wiki/Ghost_forest)
indicated in the satellite image above contains trees that were rapidly
killed by saltwater intrusion following coseismic coastal subsidence during
the earthquake of January 26, 1700, the last major CSZ event.  

:::{seealso}
- [The Copalis ghost forest, What is it and why visit?](https://wa100.dnr.wa.gov/willapa-hills/copalis-ghost-forest)
- For more information about this paleoseismology, see {cite}`orphan_tsunami`.
:::


