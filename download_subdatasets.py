import os
import tarfile
import zipfile
import requests

CONFIG = {
    'csv_server': 'https://fonetik.fr',
    'subdatasets_dir': 'subdatasets',
    'input_file': 'subdatasets.tar.gz',
    'subdataset': 'wikt_samples.csv',
    'root_dir': '.',
    'languages': ['ent', 'eno','ar', 'br', 'de', 'en', 'es', 'fi', 'fr', 'fro', 'it', 'ko', 'nl', 'pt', 'ru', 'sh', 'tr']
}

def download_file(config):
    filename = config['input_file'] 
    url_file = config['csv_server'] + '/' + filename
    if not os.path.exists(filename):
        # unfortunately wget does not work because of a redirection
        # with the server containing the CSV
        # so wget.download(url_file) doe not work
        print('downloading %s' % filename)
        r = requests.get(url_file, allow_redirects=True)
        with open(filename, 'wb') as f:
            f.write(r.content)


def extract_files(config):

    cwd = os.getcwd()
    os.chdir(config['root_dir'])
    dest_dir = config['root_dir'] + '/' + config['subdatasets_dir']
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    os.chdir(dest_dir)
    try:
        filename = '../' + config['input_file']
        file = tarfile.open(filename, 'r:gz')
        try: file.extractall()
        finally: file.close()
    finally:
        os.chdir(cwd) 


def concatenate_all(config):
    print('concatenate all')
    with open(config['subdataset'], 'w') as outfile:
        for language in config['languages']:
            fname = config['subdatasets_dir'] + '/' + language + '_wikt_samples.csv'
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def main():
    config = CONFIG
    download_file(config)
    extract_files(config)
    concatenate_all(config)

if __name__ == "__main__":
    main()



