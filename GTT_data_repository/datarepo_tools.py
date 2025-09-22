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

def copy_and_zip(relpath, verbose=False):
    fullpath = os.path.join(GTT,relpath)
    repopath = os.path.join(GTT_data, relpath)
    zip_file_path = repopath + '.zip'
    repopath_dir = os.path.split(repopath)[0]
    os.system(f'mkdir -p {repopath_dir}')
    #print('+++ repopath = ',repopath)
    #print('+++ fullpath = ',fullpath)
    #print('+++ os.path.isdir(fullpath) = ',os.path.isdir(fullpath))
    if os.path.isdir(fullpath):
        shutil.make_archive(repopath, 'zip', fullpath)
    elif os.path.isfile(fullpath):
        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            zip_file.write(fullpath)
    else:
        raise ValueError('*** file not found: ', fullpath)
    if verbose:
        print(f'converted {fullpath} to {zip_file_path}')

def make_registry(backup=True, verbose=True):
    registry_file_path = os.path.join(GTT_data_repository, 'registry.txt')
    if backup and os.path.isfile(registry_file_path):
        backup_registry_file_path = os.path.join(GTT_data_repository,
                                                 'backup_registry.txt')
        shutil.copy(registry_file_path, backup_registry_file_path)
        if verbose:
            print('Copied old registry.txt to backup_registry.txt')
    pooch.make_registry(GTT_data, registry_file_path)
    print('Created ', registry_file_path)

def make_all(verbose=True):
    datapaths = [
        'topo/topofiles/etopo22_30s_-130_-122_40_50_30sec.asc',
        'topo/topofiles/Copalis_13s.asc',
        'topo/topofiles/csz_shore.txt',
        'dtopo/dtopofiles/ASCE_SIFT_Region2.dtt3',
        'CopalisBeach/example1/sample_results',
    ]

    for datapath in datapaths:
        copy_and_zip(datapath, verbose)

    make_registry(backup=True, verbose=True)
