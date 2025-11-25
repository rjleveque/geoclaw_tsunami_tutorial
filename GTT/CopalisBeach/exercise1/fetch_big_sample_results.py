"""
Fetch the big_sample_results subdirectory (74M), which contains the full
_output directory from a sample run (including the large fort.b files
with the AMR output at each time). 
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

# fetch the big_sample_results directory:
GTT_tools.fetch('CopalisBeach/exercise1/big_sample_results', verbose=True)
