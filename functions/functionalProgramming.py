my_sum = sum

print(my_sum([1,2,3])) #first class membors function can bes assigned to variable like js

numbers = list(range(1,100))


#map takes map(fn,iterable) returns an iterator called map object
power2 = list(map(lambda x: x*2,numbers))
multiplyby100 = list(map(lambda x: x*100,power2))
print(multiplyby100)

# reversed_list = list(map(lambda x: reversed(x),power2))

#fileter function

from collections import namedtuple as tp
#filer has same singature as map (fun,iterable) return filter iterable object
# names = ['mark','john','terry', 'samingo']

# biggerNames = list(filter(lambda name: len(name) > 4,names))
# print(biggerNames)  

countries = ['','Argentina', 'Brazil', 'Columbia','Denmark']
#filerning empty nnone is falsy
filer_empty = list(filter(None,countries))
print(filer_empty)

from functools import reduce

#reduce function
data = [2,4,5,6,7,8]

print(reduce(lambda x,y: x*y,data))



#enumerate function returns count and value  useful when need to use index
list = ['s','p','e','a','k']

#join string method str.join(iterable)
word = ''.join(list)
print(word)


for count,value in enumerate(list):
    print(count,value)