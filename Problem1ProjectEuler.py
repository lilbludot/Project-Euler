def add_numbers(x,y,n):
    """ takes and adds up numbers x and its multiples up to n and y and its
     multiples up to n then adds the two sums together."""
    a=(n-1)/x
    sum_of_xs=x*(a)*(a+1)/2 #sum of all the multiples of x < n
    b=(n-1)/y
    c=b/x
    sum_zs=x*c*(c+1)/2
    sum_of_ys=y*((b)*(b+1)/2 - sum_zs) #sum of all the multiples of y<n minus the ones
    #that were double counted
    total=sum_of_xs+sum_of_ys
    print total
    


    
