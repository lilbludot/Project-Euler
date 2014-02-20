"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""
#loading up a file containing all the primes up to 10000, saving it into
#the list 'factor_base'
import pickle
infile = open("PrimesTo10000.py", "r+")  
factor_base = pickle.load(infile)

#narrowing down the list of potential amicable numbers up to 10000 by
#removing all the primes 
long_list = [n for n in range(4, 10000)]
potentials = [ n for n in long_list if not (n in factor_base)]

#creating the list of divisors
divisors = [k for k in range(1, 5001)]

#creating a function that can be used within the 'map' function. It will
#check for divisibility by n
def modder(x):
    return lambda n: n if x %n == 0 else 0

global cache
cache={}
amicables = []
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
def divisor_sum(n):
    f = modder(n)
    divisor_list = map(f, divisors)
    if n > 5000:
        x = sum(divisor_list)
    else:
        x = sum(divisor_list)- n
    return x
    



for k in potentials:
    temp = divisor_sum(k)
    if temp != k :
        temp2 = divisor_sum(temp)
        if temp2 == k and not (k in amicables):
            amicables.append(k)
            amicables.append(temp)
        
        
        





infile.close()
