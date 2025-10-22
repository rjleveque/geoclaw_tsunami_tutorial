import os,sys
import shutil
from cloudpathlib import CloudPath

#GTT = os.environ['GTT']  # Doesn't work on Github

common_code_dir = os.path.split(__file__)[0]  # drop filename
GTT = os.path.split(common_code_dir)[0]  # drop subdirectory
print('setting GTT = ',GTT)

# remote repository:
data_repository_url = \
    'https://depts.washington.edu/clawpack/geoclaw/GTT_data'

remote_path = CloudPath(data_repository_url)


def fetch(file_path, destination=None, force=False, verbose=False):
    """
    New version of fetch using cloudpathlib
    """
    relpath, fname = os.path.split(file_path)
    if destination is None:
        extraction_path = os.path.join(GTT,relpath)
    else:
        extraction_path = os.path.abspath(destination)
    if verbose: print('extraction_path = ',extraction_path)
    new_file_fullpath = os.path.join(extraction_path, fname)
    if verbose: print('new_file_fullpath = ', new_file_fullpath)

    file_exists =  os.path.isfile(new_file_fullpath) or \
                   os.path.isdir(new_file_fullpath)

    if force and file_exists:
        #shutil.rmtree(new_file_fullpath)
        print(f'Removing {new_file_fullpath}')
        os.system(f'rm -rf {new_file_fullpath}')

    zip_file = '%s.zip' % file_path
    zip_file_path = remote_path / zip_file
    assert zip_file_path.exists(), '*** zip_file_path missing: %s' \
            % zip_file_path

    # debug:
    #print('+++ file_path: ',file_path)
    #print('+++ zip_file_path: ',zip_file_path)

    if force or not file_exists:

        #print('+++ Extract ',zip_file_path)
        #print('+++ to: ', extraction_path)

        shutil.unpack_archive(zip_file_path, extraction_path)

        if verbose: print(f'Extracted {extraction_path}/{fname}')

    else:
        print('Not overwriting file or directory that already exists:\n', \
              new_file_fullpath)
        print('Specify force=True to overwrite')

    if verbose:
        print('Data is cached at: ', zip_file_path.fspath)
        if os.path.isfile(new_file_fullpath):
            print('File now exists: ', new_file_fullpath)
        elif os.path.isdir(new_file_fullpath):
            print('Directory now exists: ', new_file_fullpath)
        else:
            print('Could not find expected fullpath: ', new_file_fullpath)
