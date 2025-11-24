(topodir)=
# topo directory

The `geoclaw_tsunami_tutorial/GTT/topo` directory contains scripts and
notebooks that download or create topo files.

- [](fetch_etopo22) downloads the 30 arcsecond topofile used offshore.
  This is a rendered version of the Jupyter notebook `fetch_etopo22.ipynb`.
- [](CopalisTopo) creates the 1/3 arcsecond topofile used around Copalis Beach.
  This is a rendered version of the Jupyter notebook `CopalisTopo.ipynb`.
- The scripts `pyvista_CopalisTopo.py` and `pyvista_CopalisTopo_sealevel.py`
  can be used to visualize this topography in 3D, as described in
  [](pyvista).

The subdirectory `topo/topofiles` contains the actual topofiles that are
used as GeoClaw input in various examples. 

Rather than generating these topofiles using the notebooks above,
they can be downloaded using the script `../CopalisBeach/fetch_input_data.py`.

See [](topo_intro) for a more general introduction to topofiles.

