from collections import Counter
#Counter collection returns dict of count of elements in iterable
#subclass of dict

numbers = [10,11,11,10,20,203,301,201,102,102,101]
cnt = Counter(numbers)
print('cnt',cnt.elements()) #returns iterator 
print('cnt',cnt.most_common())
