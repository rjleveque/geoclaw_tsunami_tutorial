"""
Fetch the sample_results subdirectory
"""

import os,sys

#GTT = os.environ['GTT']  # doesn't work for Github build
GTT = os.path.abspath('../..')  # path to $GTT

print('GTT path is ',GTT)
sys.path.insert(0,f'{GTT}/common_code')

import GTT_tools  # from $GTT/common_code

GTT_tools.fetch('CopalisBeach/example1/sample_results', verbose=True)

