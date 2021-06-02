from functools import lru_cache

@lru_cache(maxsize=3) #cache last 3 calls maxsize how many calls to cache
def some_work(m):
    import time
    time.sleep(m)
    return(m)



if __name__ == '__main__':
    print(some_work(3))
    print('done')
    print(some_work(3))

