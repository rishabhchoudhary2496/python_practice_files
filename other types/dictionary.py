#dictionary keys must be immutable
#elements are acessed by keys not index mutable  dynamic
#are ordered since python 3.7 unordered before
Tenet = {'rating':9,'director':'christophar nolan','released':2019}

Tenet['rottenTomatoes'] = '70%'
print(Tenet)
del Tenet['rottenTomatoes']
print(Tenet)

#duplicate keys not allowed keys must be of immutable type
# for k,v in Tenet.items(): #items create tuples of (k,v) in a list
#     print(f'key {k} v {v} ')

print(Tenet['rating'])
print(Tenet.get('rating'))

print('rating' in Tenet)
print(len(Tenet))
#dictionary methods
superHeroes = {'super':['Iron Man','Captain America','Thor']}
dc = {'name':'h'}
# superHeroes.update(dc) upate method merge dictonaries
superHeroes |= dc #mergin using union opeator python 3.9
print(superHeroes)
# print(superHeroes.clear()) #clears
# print(superHeroes.get('super')) #access value using key if key not found returns none
#if default is there then default value is retunred
print(superHeroes.items()) #return list of tuples view objects techically
print(superHeroes.keys()) #return list of keys view objects techically
print(superHeroes.values()) #return list of values view objects techically
print(superHeroes.pop('name')) #key required
print(superHeroes.popitem()) #removes last key,value pair
print(superHeroes)
# The .items(), .keys(), and .values() methods actually return something called a view object



#creating dictonay from two list
keys = [1,2,3,3]
values = ['apple','bananna','cherry',]
#zip method
print(dict(zip(keys,values)))

res = {keys[i]: values[i] for i in range(len(keys))}
  
# Printing resultant dictionary 
print ("Resultant dictionary is : " +  str(res))