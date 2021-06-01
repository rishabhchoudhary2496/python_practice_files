from colorama import Fore

def errorHandler(fn):
        def wrapper(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except Exception as e:
                print(Fore.RED,'Exception occurred',e)
                print(Fore.RESET)
            
        return wrapper


@errorHandler
def division(dividend,divisor):
    return dividend / divisor #returning quotient


division('102',10)

print('continue running code...')
