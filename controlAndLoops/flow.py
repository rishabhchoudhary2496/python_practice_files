age = 14

if age > 13 and age <= 18:
    print('You are a teenager')
elif age > 18 and age<=35:
    print('Your are allowed to visit this')
else:
    print('shh..')


#for loop
re_zero = ['emilia','subaru','rem','ram','beatrice','roswall','rom','reinhard']

for character in re_zero:
    if character == 'rom':
        continue
    print(character)

for i in range(12):
    print(i)
 
i=10
while i<20:
    print(i)
    i +=1