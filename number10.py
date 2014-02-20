"""
Find the sum of all the primes below two million."""


from math import sqrt
#declaring the upper limit for the factor base, i.e. the list of primes
UPPER_LIMIT = 2000000

#creating the list of all integers up to the upper limit
ns = [n for n in range(2,UPPER_LIMIT)]

#Sieving the list of integers:

stop = False

#finding the integer at which to stop the sieving
limit = int(sqrt(UPPER_LIMIT))

#the sieving loop:
while not stop:
    new_ns = [ n for n in ns if n % ns[0] != 0 ]
    new_ns.append(ns[0])
    ns = list(new_ns)
    if ns[0] > limit:
        stop = True

#cleaning and presenting info:
        
factor_base = sorted(ns)
print "The size of the factor base with the upper bound of", UPPER_LIMIT, "is", len(factor_base)

#print factor_base 
print "The largest prime less than " + str(UPPER_LIMIT) + " is " + str(max(ns))+ "."

#finding the sum of all the primes below the upper limit:

total = sum(factor_base)


print "The sum of all the primes less than", UPPER_LIMIT, "is:", total



 
