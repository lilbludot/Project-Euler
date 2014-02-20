"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

MAXIMUM = 1000000

chain_lengths = [0 for k in range(0, MAXIMUM +1 )]
for i in range(1,MAXIMUM):
    stop = False
    counter = 1
    k = i
    while not stop:
        if k %2 == 0:
            k = k/2
        else: 
            k = 3*k + 1
        counter += 1
        if k == 1:
            stop = True
            chain_lengths[i] = counter  


print "The longest chain length for all positive integers less than", MAXIMUM
print "Is:", max(chain_lengths)
print "It is produced by the starting number:",\
      chain_lengths.index(max(chain_lengths))
