def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)


print(factorial(0))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2)



print(fibonacci(16))