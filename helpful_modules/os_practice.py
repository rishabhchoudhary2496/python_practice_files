import os

print(os.name) #os name
# for k in os.environ: #gives enviorment list
#  print(f'Name {k} path {os.environ[k]}')
print(os.getcwd()) #getting current working directory
print(os.cpu_count()) 
print(os.get_exec_path())
print(os.getlogin()) #login user name
print(os.getppid()) #parent process id
print(os.chdir('D://trying_things/python3')) #chdir  takes path
print(os.access('new.txt',os.F_OK)) #returns for file can be accessed
print(os.listdir()) #list directory
#os.walks fetches all paths inside dir
for root,dir,files in os.walk(os.getcwd()):
    print(files)

# os.mkdir('osDire') #makes directory in current path
#os.mkdirs() create multile directory recursively
#os.rmdir() #delete directory
print(os.stat('sample.txt'))
