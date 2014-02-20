"""What is the largest prime factor of the number 600851475143 ?"""

from math import sqrt
#declaring some constants
N = 600851475143
UPPER_LIMIT = int(sqrt(N))+1

#Creating a factor base

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
print "The size of the factor base with the upper bound of", UPPER_LIMIT, "is", len(factor_base)

#print factor_base 
print "The largest prime less than " + str(UPPER_LIMIT) + " is " + str(max(ns))+ "."

#Trial division of N by primes in the factor base. Saving the primes that
#evenly divide into N into the list called 'divisors'
m = N
divisors = list()
for p in factor_base:
    if m % p == 0:
        divisors.append(p)
        m = m / p
        
#m is what is left after the primes from the factor base were divided out of N
# if m is not equal to 1, higher powers of primes divided into m or m is a prime

print m

print divisors

print "The largest divisor of", N, "is:", max(divisors)


        
        

 
