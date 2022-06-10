from contextlib import nullcontext
from importlib.metadata import files
from math import isnan
from operator import length_hint
import zipfile
import os
from os.path import join
import json


path = r'C:'
# read config.json
data = {}


def readJson():
    with open('config.json') as f:
        data = json.load(f)
    return data


def saveJson(data):
    with open('config.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':

    if len(data) == 0:
        print('data is null')
        data = readJson()
        path = data['path']

    try:

        for folder, subfolders, files in os.walk(path):
            print(folder)
            for file in files:
                if file.endswith('.bak'):
                    filenamezip = file[0:-3]
                    file_zip = zipfile.ZipFile(join(path, file+'.zip'), 'w')
                    print('El archivo ' + join(folder, file) +
                          ' se esta comprimiendo....')
                    file_zip.write(join(path, file),
                                   compress_type=zipfile.ZIP_DEFLATED)
                    file_zip.close()
    except Exception as e:
        print(e)

    saveJson(data)
