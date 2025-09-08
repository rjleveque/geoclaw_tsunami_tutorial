"""
Download some files from the geoclaw topo repository.
These are the files created by the notebooks

- CopalisTopo.ipynb
- fetch_etopo22.ipynb

This way of doing it requires the pooch package,
    https://www.fatiando.org/pooch/latest/index.html
and allows checking hash codes to make sure the expected files are used.
"""

import shutil
import pooch
import os

topodir = 'topofiles'
os.system('mkdir -p %s' % topodir)

files = ['Copalis_13s.asc',
         'Copalis_13s.png',
         'csz_shore.txt',
         'etopo22_30s_-130_-122_40_50_30sec.asc',
         'etopo22_30s_-130_-122_40_50_30sec.png']

files_with_hash = [\
                   ('Copalis_13s.asc', 'md5:2b137e13a92a80a121d63e6ba511b50f'), 
                   ('Copalis_13s.png', 'md5:ef0f7174261409d94b63d4d28ec2d2ab'), 
                   ('csz_shore.txt', 'md5:505ba38f133548b1511da6f721e61745'), 
                   ('etopo22_30s_-130_-122_40_50_30sec.asc', 'md5:ac582cd6bb40acb3b1994a0341aa0dde'), 
                   ('etopo22_30s_-130_-122_40_50_30sec.png', 'md5:1bd8d2415cc9b26a34c57b0ee73c444c')]

for fname,hash in files_with_hash:
    url = 'https://depts.washington.edu/clawpack/geoclaw/topo/copes_hub/%s' \
                % fname
    fullpath = pooch.retrieve(url, known_hash=hash)
    shutil.copy(fullpath, './%s/%s' % (topodir,fname))

print('Copied the following files to %s/:' % topodir)
for fname,hash in files_with_hash:
    print('     %s' % fname)

