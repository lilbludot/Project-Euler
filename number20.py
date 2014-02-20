"""
Find the sum of the digits in the number 100! """
import math
s = str(math.factorial(100))
digit_list = [int(n) for n in s]

print "The sum of the digits in 100! is:", sum(digit_list)
