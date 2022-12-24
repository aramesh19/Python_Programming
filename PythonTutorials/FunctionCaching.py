import time
from functools import lru_cache

@lru_cache(maxsize=3)  #caches the last 3 function returns.
# this is function caching. this caches the values of the function the first time
# and when the same function is run the next time, it returns the values immediately.
def some_work(n):
    # task that takes 'n' seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print('Now running the program')
    some_work(4)
    print('Completed the call, running next time')
    some_work(4)
    print('The function ran again')



