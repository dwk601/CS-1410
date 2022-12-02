import sys
from time import perf_counter

#Ideally, we want to avoid computing weight_on for the same row and column more than once. To achieve this, we can save the results for any position in a module-level dictionary named cache. The key for the dictionary is the tuple (r,c) and the value is the previously computed weight on the person in that (r,c) position. This technique is called “caching” or "memoizing", and is a common technique for avoiding recomputing results.
cache = {}

#With caching, the first thing that weight_on should do is check to see if there is a previously-computed entry for the key (r,c) in cache. If there is, return it. Otherwise, compute the weight recursively by appropriately adding the weights of the people above it and save the result in cache before returning it
def weight_on(r,c): #recursive weight_on function for the human pyramid
    #count the number of times the function is called
    weight_on.counter += 1
    #if the row and column is 0, means the top position, return 0
    if r == 0 and c == 0:
        return 0
    #if the column is 0, means the left position, return the weight on the back of the person in row r-1 and and column c
    elif c == 0:
        if (r-1,0) not in cache:
            cache[(r-1,0)] = weight_on(r-1,0)
        return (cache[(r-1,0)] +200)/2.0
    #if the column is r, means the right position, return the weight on the back of the person in row r-1 and and column c-1
    elif c == r:
        if (r-1,c-1) not in cache:
            cache[(r-1,c-1)] = weight_on(r-1,c-1)
        return (cache[(r-1,c-1)] +200)/2.0
    #if the column is neither 0 nor r, means the middle position, return the sum of weight on the back of the person in row r-1 and and column c-1 and the weight on the back of the person in row r-1 and and column c
    else:
        if (r-1,c-1) not in cache:
            cache[(r-1,c-1)] = weight_on(r-1,c-1)
        if (r-1,c) not in cache:
            cache[(r-1,c)] = weight_on(r-1,c)
        return (cache[(r-1,c-1)] +200)/2.0 + (cache[(r-1,c)] +200)/2.0

def main():
    #get the number of rows
    rows = int(input("Enter the number of rows: "))
    #start the timer
    start_time = perf_counter()
    #save and write the output to a file named part3.out
    sys.stdout = open("part3.out", "w")
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
    print("Number of function calls: {}".format(weight_on.counter))
    #print the number of cache hits
    print("Number of cache hits: {}".format(len(cache)))
    #close the file
    sys.stdout.close()

if __name__ == "__main__":
    weight_on.counter = 0
    main()