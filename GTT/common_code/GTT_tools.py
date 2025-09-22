import os,sys
import shutil
import pooch

#GTT = os.environ['GTT']
GTT = os.path.abspath('..')

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

GTTdata = pooch.create(path=GTT_cache,
                       base_url=data_repository_url,
                       registry=None)

GTTdata.load_registry(registry_file_path)

def fetch(file_path, destination=None, force=False):

    relpath, fname = os.path.split(file_path)
    if destination is None:
        extraction_path = os.path.join(GTT,relpath)
    else:
        extraction_path = os.path.abspath(destination)
    #print('+++ extraction_path = ',extraction_path)
    new_file_fullpath = os.path.join(extraction_path, fname)
    #print('+++ new_file_fullpath = ', new_file_fullpath)

    file_exists =  os.path.isfile(new_file_fullpath) or \
                   os.path.isdir(new_file_fullpath)
    if file_exists:
        print('Not overwriting file or directory that already exists:\n', \
              new_file_fullpath)

    if force or not file_exists:
        zip_file_path = GTTdata.fetch(file_path + '.zip')
        assert os.path.isfile(zip_file_path), '*** problem fetching %s' \
                % zip_file_path
        #print('+++ Now exists: ',zip_file_path)

        shutil.unpack_archive(zip_file_path, extraction_path)
        #print(f'+++ extracted {extraction_path}/{fname}')
    else:
        print('Specify force=True to overwrite')
