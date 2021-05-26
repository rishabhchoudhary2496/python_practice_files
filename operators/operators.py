print(3+2)
print(3-2)
print(3*2)
print(3**2) #power
print(6%2) #modulues
print(6//2) #floor divison

a = 0
a += 10
a >>=3
print(a)
#walrus operator assigns and returns value in same line
print(walrus:=False)

inputs = list()
while (current := input('Write Someting: ')) != 'quit':
    inputs.append(current)
    print(current)