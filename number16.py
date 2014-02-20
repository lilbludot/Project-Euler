"""
What is the sum of the digits of the number 2^1000?
"""
import math 

BASE = 2
EXPONENT = 1000
SIZE = int(math.log10(BASE ** EXPONENT))
digits = [0 for j in range(SIZE + 2)]
digits[0] = BASE


def multiplier(x):
    return x*BASE

for i in range(EXPONENT-1):
    temp_list = map(multiplier, digits)
    digits = temp_list   
    #print temp_list
    for k in range(SIZE + 1):
        if temp_list[k] > 9:
            temp = temp_list[k]%10
            carry = temp_list[k]/10
            digits[k] = temp
            digits[k+1] += carry
        else:
            True
             
print digits         
    
print sum(digits)

