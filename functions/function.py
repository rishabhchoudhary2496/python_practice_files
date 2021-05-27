def print_greeting(greeting):
    print(greeting)

def sum_custom(a,b):
    """This is function calculates"""
    return a+b

print_greeting('hello there')

result = sum_custom(10,20)
print(sum_custom.__doc__)
print(id(sum))

print(result)


# positional arguments
def f(qty,item,price=50):
     print(f'{qty} {item} cost ${price:.2f}')


f(2000,20,10) #positional argument are bound by order and number so can aceess right value only in order they passed

#there are another way to call fucntion with keyword arguments in form key=value pair
#order can be different int this case though no of argumens must match

f(price=2000,item=10,qty=2)

#when we mix postional and keyword args in same call keyword args must come first
# f(10,price=1000,10) #postional arguments follows keyword arguments

#call with default argumentsp
f(10,20)

def fg(my_list=[]): #pitfall default args in only defined at first time so subsequent
    print(id(my_list))  #calls with not redefine it that's why appending to same list happendng
    my_list.append('###') #even if we mentioned list empty in default args no arg is passed
    return my_list

print(fg())
print(fg())
print(fg())

#fix of the problem
def ft(my_list=None):
     if my_list is None:
         my_list = []     
     my_list.append('###')   
     return my_list

print(ft())
print(ft())
print(ft())

# passing behaviour python
def fn(fx):
    fx=10

#whenf fn called fx points to same reference object hodling 5
#when fx=10 at this point fx points to refreces holding 10

x=5
print('before calling x',x)
fn(5)
print('after calling x',x)

def f(x):
     x = 'foo'

#passed args wont change when we exist function because 
#on entry x holds the reference which contain the 40 and when x reassign 10
#then what happend is that x reference to different object holding foo
#often called pass by assignment
for i in (
         40,
         dict(foo=1, bar=2),
         {1, 2, 3},
         'bar',
         ['foo', 'bar', 'baz']):
         f(i)
         print(i)

# Does that mean a Python function can never modify its arguments at all? 
# Actually, no, that isn’t the case! Watch what happens here:

def n(p):
    p[0] = 'modifed'

my_list = ['apple','banana','cherry']
n(my_list)
print(my_list)