from collections import namedtuple

Colors = namedtuple('Colors',['red','blue','green'])
colors = Colors(10,20,30)
print(colors.red)
print(colors.blue)
print(colors.green) #printing using key
print(colors[2]) #printing using index