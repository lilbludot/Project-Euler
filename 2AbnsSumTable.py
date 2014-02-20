import pickle
infile = open("AbndntTo20161.py", "r+")  
abundant_list = pickle.load(infile)
outfile= open("sum_table20161.py", "w+")



sum_table = [ n + k for n in abundant_list for k in abundant_list if k >= n]
pickle.dump(sum_table, outfile)

outfile.close()
infile.close()
