"""
Fetch as set of input files needed for running the examples in
$GTT/CopalisBeach/example1, as specified in the `input_files` list
defined in this script.

These are fetched from an online data repository (if they are not
already present, or if the local version differs from what is in the
archive).
"""

import os

# import GTT_tools from $GTT/common_code
# This is harder than it should be because of the need to import it
# properly when the jupyter book is built on Github.

GTT = os.path.abspath('../..')
print('GTT path is ',GTT)

try:
    from clawpack.clawutil.util import fullpath_import
    GTT_tools = fullpath_import(f'{GTT}/common_code/GTT_tools.py')
except:
    # some debugging statments:
    print('importing clawpack.clawutil.util failed')
    import clawpack
    print(f'clawpack version: {clawpack.__version__}')
    import sys
    sys.path.insert(0,f'{GTT}/common_code')
    import GTT_tools

# Specify the input files to download:

input_files = ['topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc',
        'topo/topofiles/Copalis_13s.asc',
        'dtopo/dtopofiles/ASCE_SIFT_Region2.dtt3'
    ]

# Fetch each file:

for data_file in input_files:
    print('====================================')
    GTT_tools.fetch(data_file, force=True, verbose=True)

