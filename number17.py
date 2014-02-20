"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""
#creating the dictionaries for the numbers in words
ones_plus = {0 : "", 1:"one", 2 : "two", 3:"three", 4:"four", 5:"five", 6 : "six", \
         7 : "seven", 8 : "eight", 9 : "nine" , 10 : "ten", 11 : "eleven", \
              12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen",\
              16 : "sixteen", 17 : "seventeen", 18 : "eighteen", \
              19 : "nineteen" }
tens = {2 : "twenty", 3 : "thirty", 4 : "forty", 5 : "fifty", 6 : "sixty", \
        7 : "seventy", 8 : "eighty", 9 : "ninety"}

#initializing the_list it will contain all the integer names from 1 to 1000
#in one long string
the_list = ""


def up_to_two_digit(n):
    """Takes a two digit integer and returns its name as an string"""
    if n < 20 :
        return ones_plus[n]
    else:
        temp = str(n)
        return tens[int(temp[0])] + ones_plus[int(temp[1])]
def three_digit(n):
    """Takes a three digit integer and returns its name as a string"""
    temp1 = up_to_two_digit(n %100)
    if n %100 == 0:
        add_and = "hundred"
    else:
        add_and = "hundredand"
    temp2 = one_or_two_digit(n/100) + add_and
    temp = temp2 + temp1
    return temp
        
for n in range(1, 1001):
    if n < 100:
        the_list += up_to_two_digit(n)
    elif n < 1000:
        the_list += three_digit(n)
    else:
        the_list += "onethousand"

print "The number of letters in the list is:", len(the_list)
    
