#CS1410 Human Pyramid
import sys
from time import perf_counter

#cache dictionary
cache = dict()

#Write a recursive function weight_on(r,c) that returns the weight on the back of the person in row r and and column c. Rows and columns are 0-based in row-major order. The top position is (0,0) and person H is in position (3,1)
#weight recursive function
def weight_on(r,c):
    #check if the row and column are in the cache
    if (r,c) in cache:
        return cache[(r,c)]
    
    #initialize the weight
    weight = 0
    #if r and c is zero, means the top position
    if r == 0 and c == 0:
        return weight
    #check the left and right position
    if c == 0:
        weight = (weight_on(r-1,0) +200)/2.0
    elif c == r:
        weight = (weight_on(r-1,c-1) +200)/2.0
    else:
        left = (weight_on(r-1,c-1) +200)/2.0
        right = (weight_on(r-1,c) +200)/2.0
        weight = left + right
    #save the weight in the cache
    cache[(r,c)] = weight
    return weight

rows = int(sys.argv[1])
#start the timer
start_time = perf_counter()
#loop through the rows
for r in range(0, rows):
    #loop through the columns
    for c in range(0, r+1):
        #print the weight
        print("{:5.1f}".format(weight_on(r,c)), end=" ")
    #print a new line
    print()
#end the timer
end_time = perf_counter()
#calculate the time
elapsed_time = end_time - start_time
print("Elapsed time: {:.3f} seconds".format(elapsed_time))

