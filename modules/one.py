
import pprint
# import shuffle
from sample_package import *
print(dir()) #it does import everything from package and place in symbol table

#Instead, Python follows this convention: if the __init__.py file in the package 
# directory contains a list named __all__, 
# it is taken to be a list of modules that should be imported

#import does not improt names start with _

#import styles 
import sys #have to use . notation to access modules objects
# from collections import namedtuple #import specific thing  from module
# from collections import * #import everyting from module

# print(mod1.avg_list([1,2,3,4,5,6]))
#form collection import namedtuple as tuple #as syntax alias like thing
movies = ['Silent Hill','Detective pikachu','resident evil','Home Alone','Conjuring']


# print(sys.path)
# print(shuffle.__file__) #prinnt location of module 
# print('name',shuffle.__name__) #module name that how we now im it is run as module or script
# print(shuffle.shuffleItems(movies))
# pprint.pprint(dir())


#how to reload a module if needed
# import importlib
# importlib.reload(module)

#import  module from packages
#import pkg.module or from pkg import module

#import pkg does not put it in symbol table acess something with . notaiton
#throws error

