x = 1


def incrementer():
    global x #to access global variable inside fun
    x = x+10
    print(x)


incrementer()
print(x)

p= 89
def harry():
    p = 20
    def inner():
        global p
        p = 88
    inner()
    print('after calling inner',p)

harry()
print(p)