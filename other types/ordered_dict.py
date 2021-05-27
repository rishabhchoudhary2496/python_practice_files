from collections import OrderedDict

numbers = OrderedDict()
numbers['one'] = 1
numbers['two'] = 2
numbers['three'] = 3
print(numbers)
numbers.popitem(last=True)
numbers.move_to_end(key='one')
print(numbers)