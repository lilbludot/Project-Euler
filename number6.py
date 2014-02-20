"""Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum."""

#Creating a list of the natural numbers up to 100
Numbers = [i for i in range(101)]

#Finding the sum of the numbers 
SumOfNumbers = sum(Numbers)

#Squaring the sum of the numbers
Square_of_Sum = SumOfNumbers ** 2

#Using map to square all the numbers in the list
def square(n):
    return n ** 2
Numbers_Squared = map (square, Numbers)

#Summing up all the squares
Sum_of_Squares = sum(Numbers_Squared)


#Printing results
print "The square of the sum is:", Square_of_Sum

print "The sum of the squares is:", Sum_of_Squares

print "The difference is: ", Square_of_Sum - Sum_of_Squares
