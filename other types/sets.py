names = set(('bin','root','root','proc','mark',2,4))
numbers = {1,2,1,1,4}
#sets are unordered
print(names)
print(numbers)


#to define empty set() method has to used with no param because {} will create empty dictonary
#set can only contain immutable items so no list and dictonary can be added to se 
# list_set = {[1,2,3]} 
print(names|numbers) #union operator set both should be set
print(names.union(numbers)) #union method can take any iterable and convert to set
print(names&numbers) #intersection operator
print(names.intersection(numbers)) #intersection methods
print(names - numbers) #difference operator returns only 1set element
print(names.difference(numbers))
print(names.update(numbers))

# another set methods
names.add('some') # add item to set
print(names)
names.remove('bin') #remove from set
print(names)
names.discard('a') #remove if item is in set if not does nothing
print(names)
print(names.pop()) #remove last element if set empty throws exception

print(names.clear()) #remove all elements