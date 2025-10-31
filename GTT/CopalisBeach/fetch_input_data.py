"""
Fetch as set of input files needed for running the examples in
$GTT/CopalisBeach/example1, as specified in the `input_files` list
defined in this script.

These are fetched from an online data repository (if they are not
already present, or if the local version differs from what is in the
archive).
"""

import os, sys

# import GTT_tools from $GTT/common_code
# This is harder than it should be because of the need to import it
# properly when the jupyter book is built on Github.

try:
    # try to use environment variable GTT, if set:
    GTT = os.environ['GTT']
except:
    #  this should work on Github:
    GTT = os.path.abspath('..')
print('GTT path is ',GTT)

sys.path.insert(0,f'{GTT}/common_code')

try:
    import GTT_tools
except:
    # some debugging statments:
    print(f'importing GTT_tools failed from {GTT}/common_code')

# Specify the input files to download:

input_files = ['topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc',
        'topo/topofiles/Copalis_13s.asc',
        'dtopo/dtopofiles/ASCE_SIFT_Region2.dtt3'
    ]

# Fetch each file:

for data_file in input_files:
    print('====================================')
    GTT_tools.fetch(data_file, force=True, verbose=True)
