"""
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?  """

import zeller

months = ["january", "february", "march", "april", "may", "june", "july",\
          "august", "september", "october", "november", "december"]
counter = 0
for i in range(1901, 2001):
    for m in months:
        temp = zeller.alg(m, 1, i)
        if temp == "Sunday":
            counter += 1
        else:
            True

print "The number of Sundays is:", counter
