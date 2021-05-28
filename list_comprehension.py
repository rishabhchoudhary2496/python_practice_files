numbers = list(range(1,100))


string_list = [str(n) for n in numbers]
for i in string_list:
    print("string ",int(i)*4 *104)

divided_by_five_list = [n for n in numbers if n%5 ==0]
print(divided_by_five_list)

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]
print('***even numbers***')
print(even_numbers)
print('***odd numbers***')
print(odd_numbers)