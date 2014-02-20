stop = False
counter = 1
k = 837799
while not stop:
    if k %2 == 0:
        k = k/2
    else: 
        k = 3*k + 1
    counter += 1
    if k == 1:
        stop = True
       
print counter
