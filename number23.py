"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number.
For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number,
1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the
sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as the
sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.

"""
#Note: according to a Matematica page, all numbers greater than 20161
#are the sums of two abundant numbers.  I use 20161 here.
#Still the run time of this program is very long.  10 to 20 minutes or
#even more. 


#'sum_table20161' contains all the sums of two abundant numbers less than 20161

#loading up the sum table 

import pickle
infile = open("sum_table20161.py", "r+")
sum_table = pickle.load(infile)

UPPER_LIMIT = 20161

#using list comprehension to take the list of integers less than the Upper Limit
#that are not in the table of sums.

not_sum_of_abns = [i for i in range(1, UPPER_LIMIT + 1) if not\
                    (i in sum_table)]




print "The sum of all the positive integers which aren't the sum of "
print "two abundant numbers is: ", sum(not_sum_of_abns)

infile.close()

#Answer:
#The sum of all the positive integers which aren't the sum of 
#two abundant numbers is:  4179871

