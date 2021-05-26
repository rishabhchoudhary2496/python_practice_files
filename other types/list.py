list_num = [2,4,6,8,10,12]
print(list_num)
print(list_num[3])
print(list_num[-1])

#adding item to list
list_num.append(14)
print(list_num)
list_num.insert(-1,16)
print(list_num)

#removing items from list
list_num.pop()
print(list_num)

list_num.pop(0)
print(list_num)

#remove first occurrents of item
list_num[0]= 20
list_num.remove(10)
print(list_num)


#list slicing
print(list_num[::-1])

#sorted list
sorted_list = sorted(list_num)
print(sorted_list)
sorted_list = sorted(list_num,reverse=True) #cna take key to perform custom sorting
print(sorted_list)
list_num.sort() #sort on original list
print(list_num)

s= 'Revenant'
slice_string = s[:]
print(slice_string)
print(f'original string location {id(s)} and slice string location {id(slice_string)}')
#same location


#different location
list_slice = list_num[:]
print(f'original list location {id(list_num)} and slice string location {id(list_slice)}')

#in operator list
print(5 in list_num)
print(5 not in list_num)

#concat operator
list_num = list_num + [22,24]
print(list_num)

#repeat operator
print(list_num*2)

#min max operator
print(min(list_num))
print(max(list_num))
#len
print(len(list_num))
list_num[1:3] = [100,200]
list_num +='roger'
list_num.append('hello')
list_num.extend([90,21])
print(list_num)
#print(list_num.clear()) #remove all items

#list comprehension
new_list = [x*2 for x in list_num]
print(new_list)

#combinators
combinators = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combinators)

