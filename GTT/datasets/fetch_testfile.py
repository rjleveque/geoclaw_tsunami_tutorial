
"""
Fetch as single file as a test.
"""

import os

# import GTT_tools from $GTT/common_code
# This is harder than it should be because of the need to import it
# properly when the jupyter book is built on Github.

GTT = os.path.abspath('..')
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

# Specify the files to download:

datasets = ['datasets/testfile.txt']

# Fetch each file:

for dataset in datasets:
    print('====================================')
    GTT_tools.fetch(dataset, force=True, verbose=True)

