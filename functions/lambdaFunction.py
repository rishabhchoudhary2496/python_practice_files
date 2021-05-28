# syntax lambda input: body

# add 1 to number using lambda
add_1 = lambda x: x+1
print_fullName = lambda firstName,lastName: print(f'{firstName.title()} {lastName.title()}')

print_fullName('mark','evans')
print(add_1(10))
print((lambda x: x*2)(12)) # could be invoked this way also

# print((lambda x: pass)(1))

#In a lambda function, statements like return, pass, assert, or raise will raise a SyntaxError exceptio

#does not support type annontations
#does not suppport @syntax decorator can be wrapped with function
