
import os
GTT = os.path.abspath('../..')
print('GTT path is ',GTT)

try:
    from clawpack.clawutil.util import fullpath_import
    GTT_tools = fullpath_import(f'{GTT}/common_code/GTT_tools.py')
except:
    print('importing clawpack.clawutil.util failed')
    import clawpack
    print(f'clawpack version: {clawpack.__version__}')
    import sys
    sys.path.insert(0,f'{GTT}/common_code')
    import GTT_tools

input_files = ['topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc',
        'topo/topofiles/Copalis_13s.asc',
        'dtopo/dtopofiles/ASCE_SIFT_Region2.dtt3'
    ]

for data_file in input_files:
    print('====================================')
    GTT_tools.fetch(data_file, force=True, verbose=True)

