import os,sys,shutil
import zipfile
import shutil
import pooch

GTT = os.environ['GTT']

GTT_cache = GTT + '_cache'
print('path to GTT_cache is\n     ', GTT_cache)

GTT_data_repository = GTT + '_data_repository'
print('path to GTT_data_repository is\n     ', GTT_data_repository)

GTT_data = os.path.join(GTT_data_repository, 'GTT_data')
print('path to GTT_data is\n     ', GTT_data)

# remote repository:
data_repository_url = \
    'https://depts.washington.edu/clawpack/geoclaw/GTT_data'

# Create object to be used for registry:
GTTdata = pooch.create(path=GTT_cache,
                       base_url=data_repository_url,
                       registry=None)

# load registry file:
registry_file_path = os.path.join(GTT_data_repository, 'registry.txt')
GTTdata.load_registry(registry_file_path)

if 1:
    all_datasets = GTTdata.registry_files
else:
    # if starting from scratch... need to keep this up to date:
    all_datasets = [
            'topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc',
            'topo/topofiles/Copalis_13s.asc',
            'topo/topofiles/csz_shore.txt',
            'dtopo/dtopofiles/ASCE_SIFT_Region2.dtt3',
            'CopalisBeach/example1/sample_results',
            'datasets/testfile.txt'
            ]


def copy_and_zip(file_path, verbose=False):
    relpath, fname = os.path.split(file_path)
    fullpath = os.path.join(GTT,file_path)
    fullpath_dir = os.path.split(fullpath)[0]
    repopath = os.path.join(GTT_data, file_path)
    zip_file_path = repopath + '.zip'
    repopath_dir = os.path.split(repopath)[0]
    os.system(f'mkdir -p {repopath_dir}')
    if 1:
        print('+++ repopath = ',repopath)
        print('+++ fullpath = ',fullpath)
        print('+++ os.path.isfile(fullpath) = ',os.path.isfile(fullpath))
        print('+++ os.path.isdir(fullpath) = ',os.path.isdir(fullpath))

    if os.path.isfile(fullpath) or os.path.isdir(fullpath):
        shutil.make_archive(repopath, 'zip', root_dir=fullpath_dir, base_dir=fname)
    else:
        raise ValueError('*** file not found: ', fullpath)
    if verbose:
        print(f'Created {zip_file_path}')

def make_registry(backup=True, verbose=True):
    if backup and os.path.isfile(registry_file_path):
        backup_registry_file_path = os.path.join(GTT_data_repository,
                                                 'backup_registry.txt')
        shutil.copy(registry_file_path, backup_registry_file_path)
        if verbose:
            print('Copied old registry.txt to backup_registry.txt')
    pooch.make_registry(GTT_data, registry_file_path)
    print('Created ', registry_file_path)

def add_dataset(dataset, verbose=True):
    copy_and_zip(dataset, verbose=verbose)
    # make a new registry file
    # note this recomputes all hashes, better way to add just one?
    make_registry(backup=True, verbose=True)


def make_all(datasets, verbose=True):
    """
    Note that remaking all the zip files may change their hashes, even if
    the contents we care about didn't change (because zip includes some
    metadata in the zipfile that may have changed).

    So it's best to just add new/changed files one at a time using
    copy_and_zip directly, and then redo the make_registry().

    And always push any changes to registry.txt to the git repo when
    rsync'ing GTT_data to the remote data repository.
    """

    for dataset in datasets:
        copy_and_zip(dataset, verbose)

    make_registry(backup=True, verbose=True)

if __name__ == '__main__':

    make_all(all_datasets)
