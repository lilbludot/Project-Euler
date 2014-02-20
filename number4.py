# -*- coding: utf-8 -*-


"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math import sqrt

#identifying a pallindrome

def is_pallindrome(n):
    """determines whether the argument n is a pallindrome """
    s = str(n)
    s_length= len(s)
    for i in range(s_length/2):
        if s[i] != s[s_length - 1 - i]:
            return False
    return True
   


#the list of integers that are possibly the product of two 3 digit numbers
#is just all the numbers n, s.t. 10000 <= n <= 1,000,000

int_list = [i for i in range(10000, 1000000)]

pallindrome_list = [i for i in int_list if is_pallindrome(i)]
pallindrome_list.sort(reverse = True)




#Creating a factor base

#declaring some constants
N = 1000000
UPPER_LIMIT = N



#1. Starting with a list of integers 
ns = [n for n in range(2,UPPER_LIMIT)]


#2. finding the number at which to stop sieving at
limit = int(sqrt(UPPER_LIMIT))

#3.Sieving the list of integers getting rid of multiples of 2, 3, ...
stop = False

while not stop:
    new_ns = [ n for n in ns if n % ns[0] != 0 ]
    new_ns.append(ns[0])
    ns = list(new_ns)
    if ns[0] > limit:
        stop = True

#4. Cleaning up the list of primes by sorting
factor_base = sorted(ns)

print "the size of the factor base is", len(factor_base)


#factoring the pallindromes and storing the info in a dictionary
factored_pallindromes = { }
for num in pallindrome_list:
    divisors = list()
    m = num
    for p in factor_base:
        if m % p == 0:
            divisors.append(p)
            m = m / p

    factored_pallindromes[num] = divisors

short_palls = [x for x in pallindrome_list if max(factored_pallindromes[x])<1000]

for num in short_palls:
    print num, factored_pallindromes[num]

            
    
