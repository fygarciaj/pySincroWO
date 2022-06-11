from contextlib import nullcontext
from importlib.metadata import files
import zipfile
import os
from os.path import join
import json


path = r'C:'
# read config.json
dataConfig = {
   "sourcePath": path,
   "destinyPath" : path
}


def readJson():
    try:
        with open('config.json') as f:
            dataConfig = json.load(f)
            return dataConfig
    except:
        saveJson(dataConfig)
        pass


def saveJson(dataConfig):
    try:
        with open('config.json', 'w') as f:
            json.dump(dataConfig, f)
    except:
        pass


if __name__ == '__main__':
    
    dataConfig = readJson()
    sourcePath = dataConfig['sourcePath']
    destinyPath = dataConfig['destinyPath']

    if os.path.exists(sourcePath):
        print("La carpeta origen donde se encuentras las copias de seguridad es: " + sourcePath)
    if os.path.exists(destinyPath):
        print("La carpeta destino donde se pasaran las copias de seguridad es: " + sourcePath)



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

    # saveJson(dataConfig)
