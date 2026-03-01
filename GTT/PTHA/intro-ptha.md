(intro-ptha)=
# Introduction to PTHA

One use of tsunami modeling is to perform hazard assessment for a community or
structure in relation to possible future tsunamis.  Since it is impossible to
know the details of future tsunamis, this is often done either by

- A scenario-based approach, in which one or more hypothetical future events
  are considered (for example one event that is thought to be a "worst case",
  or a few hypothetical events of varying severity).

- A probabilistic approach where some probability distribution is assumed
  for future events and then we attempt to determine the resulting probability
  distribution of some quantity of interest, such as the inundation depth at
  a location or as a map over an entire community.

There is often some overlap between these approaches, e.g. by a "worst case"
event we might mean one that has at least a 2500-year return time according
to some probabilistic model. Or to approximate the probability distribution
of a quantity of interest we may sample a large number of scenarios from the
underlying probability distribution and perform a tsunami simulation of each.

:::{note}
More info could be added, e.g.
- logic trees vs. other ways to specify probability distributions
- epistemic vs aleatoric uncertainty
:::

## Review paper and Tutorial

The review paper
of [Grezio et al. 2017](https://doi.org/10.1002/2017RG000579),
"Probabilistic Tsunami Hazard Analysis: Multiple Sources and Global Applications"
provides an overview of PTHA.  As part of this, a tutorial was created in the
form of Jupyter notebooks.  These notebooks have been adapted for these
notes can can be find in the following sections.  See [](PTHA-Tutorial)
for more information and links.

A self-contained repository containing these notebooks can be found at https://github.com/rjleveque/ptha_rog.
