import pickle
from math import sqrt
fo = open("PrimesTo10000.py", "w")
UPPER_LIMIT = 10000
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

pickle.dump(factor_base, fo)
fo.close()





 
