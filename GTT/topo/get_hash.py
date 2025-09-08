"""
Simple script to get the hash codes for a set of files to use in pooch
    https://www.fatiando.org/pooch/latest/index.html
"""

import pooch

files = ['Copalis_13s.asc',
         'Copalis_13s.png',
         'csz_shore.txt',
         'etopo22_30s_-130_-122_40_50_30sec.asc',
         'etopo22_30s_-130_-122_40_50_30sec.png']

topodir = './topofiles'

alg = 'md5'

files_with_hash = []

for file in files:
    fname = '%s/%s' % (topodir,file)
    hash = pooch.file_hash(fname, alg=alg)
    hash_string = '%s:%s' % (alg, hash)
    files_with_hash.append((file, hash_string))

#print(files_with_hash)

print('files_with_hash = [\\')
for ftuple in files_with_hash:
    print('    ', ftuple)
print('    ]')

