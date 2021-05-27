from array import *

vals = array('i',[1,2,3,4])
# vals = array('')
newArr = array(vals.typecode,(a**2 for a in vals))
print('new Arr',newArr)

charArray = array('u',['a','p','p','l','e'])
print(charArray)

print(vals[0])

vals.append(10)
print(vals)
vals.remove(10)
print(vals)
vals.reverse()
print(vals.tobytes())
print(vals.itemsize)
print(vals)


#looping over array

#1method
for i in vals:
    print(i)

#2method
for i in range(len(vals)):
    print(vals[i])
