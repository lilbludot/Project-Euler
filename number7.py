"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from math import sqrt
UPPER_LIMIT =1000000
ns = [n for n in range(2,UPPER_LIMIT)]
stop = False
limit = int(sqrt(UPPER_LIMIT))
while not stop:
    new_ns = [ n for n in ns if n % ns[0] != 0 ]
    new_ns.append(ns[0])
    ns = list(new_ns)
    if ns[0] > limit:
        stop = True


factor_base = sorted(ns)
print "The size of the factor base with the upper bound of", UPPER_LIMIT, "is", len(factor_base)

#print factor_base 
print "The largest prime less than " + str(UPPER_LIMIT) + " is " + str(max(ns))+ "."

print "The 10001st prime is: " + str( factor_base[10000]) +  "."

 
