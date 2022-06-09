from importlib.metadata import files
import zipfile
import os
from os.path import join



path = r'F:\01062022'

for folder, subfolders, files in os.walk(path):
    print(folder)
    for file in files:
        if file.endswith('.bak'):
            filenamezip = file[0:-3]
            file_zip = zipfile.ZipFile(join(path, file+'.zip'), 'w')
            print('El archivo '+ join(folder,file)+ ' se esta comprimiendo....')
            file_zip.write(join(path, file), compress_type=zipfile.ZIP_DEFLATED)
            file_zip.close()

