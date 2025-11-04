import os,sys,shutil
import zipfile
import shutil

GTT = os.environ['GTT']

GTT_data_repository = GTT + '_data_repository'
print('path to GTT_data_repository is\n     ', GTT_data_repository)

GTT_data = os.path.join(GTT_data_repository, 'GTT_data')
print('path to GTT_data is\n     ', GTT_data)

if 0:
    # remote repository:
    data_repository_url = \
        'https://depts.washington.edu/clawpack/geoclaw/GTT_data'
    remote_path = CloudPath(data_repository_url)


# List of all datasets to be transferred to remote repository:
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
    if 0:
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



if __name__ == '__main__':

    if 0:
        # to copy and zip all datasets listed above:
        datasets = all_datasets
    else:
        # specify the new/modified datasets to copy and zip:
        datasets = ['CopalisBeach/example2/sample_results']

    for dataset in datasets:
        copy_and_zip(dataset, verbose=True)

    print('To rsync to remote data repository:')
    print("""rsync -avz GTT_data/ clawpack@homer.u.washington.edu:public_html/geoclaw/GTT_data/""")
