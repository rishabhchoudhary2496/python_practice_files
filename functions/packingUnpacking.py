names = ['a','b','c']


#called argument tuple packing unpacking  used with * operator
#any iterable can be unpacked and passed
def print_names(*args): #packing args into tuples for variable length argument
    for i in args:
        print(i)


print_names(*names) #unpacking the list and passing


#argument dictionary packing used with ** operator

def data(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key,value in kwargs.items():
    #     print(f'key {key} and value {value}')


def gu(a,b,c):
    print(f'a={a},b={b},c={c}')

d = {'a':'this','b':'error','c':'dj'}
gu(**d) #unpackng dict
data(one=1,two=2) #even positional arg passed throws typerror 

v = [10,20]
dp = {'name':'some','address':'#wjs'}

# def uiop(*args,**kwargs):
#     print(args)
#     print(kwargs)


# uiop(*v,**dp)

# def concat(*args,prefix=':'):
#     print(f'{prefix} {".".join(args)}')


# concat('a','b','c',prefix='->')


def o(a: int, b: str) -> float:
    print(a)

print(o.__annotations__)