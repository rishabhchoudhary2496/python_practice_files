import shutil
import os


for root,dir,files in os.walk(os.getcwd()):
    for file in files:
        filename,extension = file.split('.')
        if extension == 'mp3':
            shutil.rmtree(file)
    print('operation completed')