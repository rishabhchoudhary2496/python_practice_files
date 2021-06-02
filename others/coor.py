
def callCoroutine(fun):
    def start(*args,**kwargs):
        current = fun(*args,**kwargs)
        next(current)
        return current
    return start

#cooroutines 
@callCoroutine
def searcher():
    import time
    book = 'This is harry potter book it also is adopted for movies'
    time.sleep(4)
    while True:
        text = (yield) #yield consumes passed data
        if text in book:
            print('Text in the book')
        else:
            print('not found!')


my_search = searcher()
my_search.send('movies')
my_search.send('This')

#coroutine vs genators
#coroutine consumes generator produces