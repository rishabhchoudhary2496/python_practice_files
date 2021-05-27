numbers = list(range(1,100))

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]
print('***even numbers***')
print(even_numbers)
print('***odd numbers***')
print(odd_numbers)