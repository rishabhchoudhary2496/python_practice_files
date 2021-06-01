import sys
print(sys.argv) #argument paseed
print(sys.builtin_module_names)

n = 10
l = 100
print(sys.getrefcount(l)) #returns the no of refrences for object
print(sys.getsizeof(n))
print(sys.getsizeof(l)) #returns size of object
print(sys.getrecursionlimit())
print(sys.getwindowsversion())
print(sys.maxsize) #returnes max value of variable
print(sys.path) #retusn path env list
print(sys.platform)
sys.exit()