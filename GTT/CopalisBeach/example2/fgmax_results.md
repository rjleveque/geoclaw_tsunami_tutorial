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

(copalis:example2:fgmax_results)=
# Sample fgmax results

From the
[GeoClaw Tsunami Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial)

The directory `$GTT/CopalisBeach/example2`
contains a GeoClaw example that produces results on fgout and fgmax grids.

:::{seealso}
- [](README) for more about this example,
- [](plot_fgmax) is a Jupyter notebook that plots the fgmax results.
- [chile2010_fgmax-fgout]() shows results from the example included with
  GeoClaw in `$CLAW/geoclaw/examples/tsunami/chile2010_fgmax-fgout`, which
  also illustrates how to make fgout animations, similar to what is
  described here, using the Chile 2010 event in the offshore region.
:::

The script `fetch_sample_results.py` can be used to fetch some sample
results if you want to run the post-processing script or notebook in
this directory without running the GeoClaw code.

```{code-cell}
:tags: [remove-input, remove-output]
run fetch_sample_results.py
```

## Plotting fgmax results on folium maps

The notebook [](plot_fgmax_folium) produces an intereactive plot of the
maximum water depth on top of a leaflet.js map produced using the Python
package [folium](https://python-visualization.github.io/folium/latest/).

The map created there is also saves as an html file that can be posted on
the web for any viewer to interact with, or embedded in a webpage as is done
here:

<iframe
    width="800"
    height="800"
    src="https://faculty.washington.edu/rjl/misc/folium_map_with_max_depth.html"
    frameborder="0"
    allowfullscreen>text
</iframe>


