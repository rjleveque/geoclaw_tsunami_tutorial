"""
Fetch the sample_results and other files needed for the tutorial notebooks
"""

import os,sys

# import GTT_tools from $GTT/common_code
# This is harder than it should be because of the need to import it
# properly when the jupyter book is built on Github.

try:
    # try to use environment variable GTT, if set:
    GTT = os.environ['GTT']
except:
    #  this should work on Github:
    GTT = os.path.abspath('../..')
print('GTT path is ',GTT)

sys.path.insert(0,f'{GTT}/common_code')

try:
    import GTT_tools
except:
    # some debugging statments:
    print(f'importing GTT_tools failed from {GTT}/common_code')

# fetch the sample_results directory:

datasets = ['PTHA/ptha_rog/Events', 'PTHA/ptha_rog/figures',
            'PTHA/ptha_rog/MapsTopo', 'PTHA/ptha_rog/SampleResults']

for dataset in datasets:
    GTT_tools.fetch(dataset, verbose=True)
