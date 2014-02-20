for i in range(1001):
    for j in range(1001):
        for k in range(1001):
            if i**2 + j**2 == k**2:
                print i,j,k
                if i + j + k == 1000:
                    print "Found it! It is:", i, j, k
