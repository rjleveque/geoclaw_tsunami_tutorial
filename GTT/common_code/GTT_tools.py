import os,sys
import shutil
import pooch

#GTT = os.environ['GTT']  # Doesn't work on Github

#print('file = ', __file__)  # full path to this file
common_code_dir = os.path.split(__file__)[0]  # drop filename
GTT = os.path.split(common_code_dir)[0]  # drop subdirectory
print('setting GTT = ',GTT)

# remote repository:
data_repository_url = \
    'https://depts.washington.edu/clawpack/geoclaw/GTT_data'

# local cache for downloaded files:
GTT_cache = GTT + '_cache'
print('path to GTT_cache is\n     ', GTT_cache)

# location of reposity registry:
GTT_data_repository = GTT + '_data_repository'
#print('path to GTT_data_repository is\n     ', GTT_data_repository)
registry_file_path = os.path.join(GTT_data_repository, 'registry.txt')

# Create object to be used for fetching files:
GTTdata = pooch.create(path=GTT_cache,
                       base_url=data_repository_url,
                       registry=None)

# load registry file:
GTTdata.load_registry(registry_file_path)

def check_cache(data_paths=GTTdata.registry_files):
    """
    For each data_path in data_paths (by default all files in the registry),
    compare the hash of the data_path in cache to GTTdata.registry[data_path]
    to see if it is out of date.

    Note that this assumes the registry is up to date with the remote
    data repository, which is should be if a `git pull` has recently been
    done in $GTT.
    """
    missing = []
    out_of_date = []
    for data_path in data_paths:
        cached_file = os.path.join(GTT_cache, data_path)
        if not os.path.isfile(cached_file):
            missing.append(data_path)
        else:
            cached_file_hash = pooch.file_hash(cached_file)
            registry_hash = GTTdata.registry[data_path]
            if cached_file_hash != registry_hash:
                out_of_date.append(data_path)

    print('The following files in GTT_cache are up to date:')
    for data_path in data_paths:
        if (data_path not in missing) and (data_path not in out_of_date):
            print('    ', data_path)

    if len(missing) > 0:
        print('The following files are missing from GTT_cache:')
        for data_path in missing:
            print('    ', data_path)

    if len(out_of_date) > 0:
        print('The following files in GTT_cache are out of date:')
        for data_path in out_of_date:
            print('    ', data_path)


def up_to_date(data_path):
    """
    Check if a file is up to date with the remote data repository version
    """
    target_file = os.path.join(GTT, data_path.replace('.zip',''))
    cached_file = os.path.join(GTT_cache, data_path)

    cached_file_missing = not os.path.isfile(cached_file)
    if not cached_file_missing:
        cached_file_hash = pooch.file_hash(cached_file)
        registry_hash = GTTdata.registry[data_path]
        out_of_date = cached_file_hash != registry_hash

    if cached_file_missing:
        print('cached file missing: ', cached_file)
    elif out_of_date:
        print('cached file out of date, with hash ',cached_file_hash)
        print('  registry_hash = ', registry_hash)
    else:
        print('cached file up to date: ', cached_file)


def fetch(file_path, destination=None, force=False, verbose=False):

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

    if force or not file_exists:
        try:
            zip_file_path = GTTdata.fetch(file_path + '.zip')
        except:
            print('*** registry file might be out of date, git pull?')
            raise
        assert os.path.isfile(zip_file_path), '*** problem fetching %s' \
                % zip_file_path
        if verbose: print('Now exists: ',zip_file_path)

        #shutil.unpack_archive(zip_file_path, new_file_fullpath)
        shutil.unpack_archive(zip_file_path, extraction_path)
        if verbose: print(f'Extracted {extraction_path}/{fname}')

    else:
        print('Not overwriting file or directory that already exists:\n', \
              new_file_fullpath)
        print('Specify force=True to overwrite')

    if verbose:
        if os.path.isfile(new_file_fullpath):
            print('File now exists: ', new_file_fullpath)
        elif os.path.isdir(new_file_fullpath):
            print('Directory now exists: ', new_file_fullpath)
        else:
            print('Could not find expected fullpath: ', new_file_fullpath)
