#for high level file operations
import os
import shutil
import time
from pprint import pprint

#making a copy of a file
# print('Before ',os.listdir())
# shutil.copyfile('info.txt','info-copy.txt')
# print('After ',os.listdir())

#copying a file to another directory
# shutil.copy('sample.txt','other types/sample2.txt')



def file_meta(file_name):
    stat_info = os.stat(file_name)
    print(' Mode :',oct(stat_info.st_mode))
    print('  Created :', time.ctime(stat_info.st_ctime))
    print('  Accessed:', time.ctime(stat_info.st_atime))
    print('  Modified:', time.ctime(stat_info.st_mtime))

# os.mkdir('journalDev')
# print('Source File: ')
# file_meta('some.txt')

# if you want to copy a file with same meta deta 
# shutil.copy2('some.txt','journalDev')

# print('DESTINATION FILE:')
# file_meta('journaldev/some.txt')


#cloning a directory recursively
# shutil.copytree('journalDev','JournalDevCopy')
# print('\nAFTER:')
# pprint(os.listdir('JournalDevCopy'))

#remove directory
# shutil.rmtree('JournalDevCopy')
# shutil.rmtree('journalDev')

#finding file
# print(shutil.which('python.exe')) #gives file path which is added to path

#monitoring file sapce
print(shutil.disk_usage(os.getcwd()))


# Recursively move a file or directory (src) to another location (dst) and return the destination
shutil.move('.vscode','vs-copy')