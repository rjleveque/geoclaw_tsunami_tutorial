(alignment)=
# Alignment/Centering of Grids and Points

Various sets of grids and points are used in GeoClaw, for *input data*, as
*computational grids*, and for *output of results*. One convenient feature of
GeoClaw is that in principle these grids and points need not be aligned with
each other in any particular way and the code will run and generally
produce useful results.

However, there are some situations in which it is highly desirable to pay
more attention to their alignment, and a few cases where misleading results
might be obtained that could be avoided by adjusting the alignment.

(alignment:types)=
## Types of grids/points used in GeoClaw

First a summary of some of the different grids/points used in GeoClaw:

- **Input grids**

  - At least one topofile is needed in GeoClaw, but often several are used
    that cover different (possibly overlapping) regions and often at
    different resolutions. We always assume these are specified on a
    rectangular uniformly spaced grid of points. The specific point values
    generally depend on the source of the DEM. 

  - For many GeoClaw problems a dtopofile is also specified, again on a
    uniform grid of points.

- **Computational grids**

  - The finite volume method used in GeoClaw produces an approximate cell 
    average of quantities `(h, hu, hv)` and so the solution can be thought
    of as piecewise constant over each grid cell.

  - Alternatively one could view each cell value as a pointwise value at the
    center of the computational cell, which is sometimes
    done when interpolating to output grids or points, as described further
    below.

  - When AMR is used, there can be many different AMR levels of computational
    grids at different resolutions. In this case the grids at different
    levels always are aligned with one another. For example, if refining by
    a factor of 3 from Level 1 to Level 2 then each Level 1 cell in the
    refined region is covered by exactly 9 cells at level 2. 

- **Output grids and points**

  - In addition to the frame output (full AMR solution at specified output
    times), an *fgout grid* can be specified for more frequent output on
    a specified "fixed grid".  GeoClaw will interpolate from the
    computational grids to the fgout grid as needed.

  - We can specify *fgmax grids*, where the maximum of various quantities
    is monitored over the full simulation.  Again GeoClaw must typically
    interpolate values to these grids from the computational grids

  - We can also specify discrete synthetic *gauge locations*, where time
    series of the solution are output.

(alignment:interp)=
## Interpolation methods

Transferring information from one grid to another grid or set of points
typically requires some form of interpolation.  Two forms are used in
GeoClaw, as described in the next sections. For this discussion we assume we
want to interpolate to some arbitrary gauge location, but the same
approaches are used to interpolate to points on an fgout or fgmax grid.

(alignment:interp0)=
### Piecewise constant (order 0) interpolation

Since the finite volume method produces cell averages, we can think of the
solution as constant over each grid cell. To interpolate to
a gauge location, for example, we can determine what grid cell the gauge
lies in (on the finest AMR level available at this point) and then simply
take the cell average values in that cell as the value at the gauge.

(alignment:interp1)=
### Piecewise bilinear (order 1) interpolation

In many cases a better approximation to the value at a point can be obtained
using bilinear interpolation.  Consider the cell averages of the solution as
defining pointwise values at the cell centers.  Then determine what 4 cell
centers surround the gauge location of interest.  The 4 values a the 4 cell
centers defines a unique bilinear function over the rectangle they define.
This function has the form $L(x,y) = a_0 + a_1x
+ a_2y + a_3xy$ and we can solve for the 4 coefficients by requiring that the
function agrees with the 4 given values at the corners of the rectangle.
This function is then evaluated it the gauge location or other point of
interest.



## Computing GeoClaw cell-averaged `B` values from topofile
- Separate page on this?
- Always use bilinear, so `B` values never agree with DEM values


## Alignment of topofiles and computational grids

- Cell centers at various resolutions
- Reasons for wanting exact alignment:
  - Need output at DEM points for inundation maps
  - Want to use topofile to define fgmax grid
- Even vs odd refinement factors
- Note that `dx = dy` in UTM gives non-square in meters
- Adjusting xlower, etc to achieve alignment

## Constant vs. bilinear interpolation of solution

- Bilinear generally better if all neighboring cell centers wet
- Problems near shoreliine, margin of flow

## Interpolation to gauges

- Use bilinear where all wet, constant otherwise
- Discontinuities in `B`  can result, at fixed grid resolution

### Centering gauges

- Can usually shift gauge slightly
- if not, could shift domain but only to match 1 gauge
- Comparing results on different grid resolutions (even ref ratios best)




