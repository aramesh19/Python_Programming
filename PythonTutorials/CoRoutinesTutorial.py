import time

def Searcher():
    book = 'this is a book on Python programming'
    time.sleep(4) # pause for 4 seconds

    while True:
        text = (yield)
        if text in book:
            print('your text is in book')
        else:
            print('text is NOT in the book')

search = Searcher() # coroutine is created.
next(search)
# after the above lines are executed,
# here after only the while loop is run.
search.send('Python')
input('Press any key')
search.send('Python pr')
search.close()