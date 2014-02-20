"""
This program finds and saves the list of abundant numbers up to
the UPPER_LIMIT to a file
"""


#setting up to save the list of abundant numbers to a just created file
import pickle
abundant_file = open("AbndntTo20161.py", "w")


#defining some constants
UPPER_LIMIT = 20161
divisor_limit = UPPER_LIMIT/2
divisor_list = [i for i in range(1, divisor_limit + 1)]
abundant_list = []


#creating a function that can be used within the 'map' function. It will
#check for divisibility by n
def modder(x):
    return lambda n: n if x %n == 0 else 0



for n in range(12, UPPER_LIMIT + 1):
    f = modder(n)
    ns_divisors = map(f, divisor_list)
    if n < divisor_limit:
        temp = sum(ns_divisors) - n #subtract n because we want proper divisors only
    else:
        temp = sum(ns_divisors)
    if  temp > n:
        abundant_list.append(n)



#dumping the list of abundant numbers into the file
pickle.dump(abundant_list, abundant_file)
abundant_file.close()
