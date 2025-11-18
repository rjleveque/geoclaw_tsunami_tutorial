"""
Fetch all input data and sample results needed for building the book.
This script is called from .github/workflows/deploy.yml
to fetch data when building on Github.
"""

import os,sys

# import GTT_tools from $GTT/common_code:

GTT = os.path.abspath('GTT')
sys.path.insert(0,f'{GTT}/common_code')

try:
    import GTT_tools
except:
    # some debugging statments:
    print(f'importing GTT_tools failed from {GTT}/common_code')

all_datasets = [
        'topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc',
        'topo/topofiles/Copalis_13s.asc',
        'topo/topofiles/csz_shore.txt',
        'dtopo/dtopofiles/ASCE_SIFT_Region2.dtt3',
        'CopalisBeach/example1/sample_results',
        'CopalisBeach/exercise1/sample_results',
        'CopalisBeach/example2/sample_results'
        ]

for dataset in all_datasets:
    # fetch the sample_results directory:
    GTT_tools.fetch(dataset, verbose=True)
