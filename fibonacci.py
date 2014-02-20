global cache
cache={}

def memoizator(func):
    global cache
    cache={}
    def cache_updater(*args):
        global cache
        if args[0] in cache:
            return cache[args[0]]
        else:
            temp = func(*args)
            cache[args[0]] = temp
            return temp
    return cache_updater

@memoizator
def fibonacci(n):
    if n == 0 or  n == 1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)



    
