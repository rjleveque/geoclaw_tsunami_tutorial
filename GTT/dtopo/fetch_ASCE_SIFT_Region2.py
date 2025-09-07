"""
Download the ASCE_SIFT_Region2.dtt3 dtopofile from the geoclaw repository.
Alternatively, this dtopofile can be created using the notebook
ASCE_SIFT_Region2.ipynb
"""

import shutil
import pooch

fname = 'ASCE_SIFT_Region2.dtt3'
url = 'https://depts.washington.edu/clawpack/geoclaw/dtopo/CSZ/%s' % fname
known_hash = 'md5:8177acadc118264e1cdbf114c391bac0'
fullpath = pooch.retrieve(url, known_hash)
shutil.copy(fullpath, './dtopofiles/%s' % fname)
