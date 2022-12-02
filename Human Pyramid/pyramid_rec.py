import sys
from time import perf_counter

#recursive weight_on function for the human pyramid
def weight_on(r,c): 
    #count the number of times the function is called
    weight_on.counter += 1
    #if the row and column is 0, means the top position, return 0
    if r == 0 and c == 0:
        return 0
    #if the column is 0, means the left position, return the weight on the back of the person in row r-1 and and column c
    elif c == 0:
        return (weight_on(r-1,0) +200)/2.0
    #if the column is r, means the right position, return the weight on the back of the person in row r-1 and and column c-1
    elif c == r:
        return (weight_on(r-1,c-1) +200)/2.0
    #if the column is neither 0 nor r, means the middle position, return the sum of weight on the back of the person in row r-1 and and column c-1 and the weight on the back of the person in row r-1 and and column c
    else:
        return (weight_on(r-1,c-1) +200)/2.0 + (weight_on(r-1,c) +200)/2.0
#print the number of function calls
weight_on.counter = 0

def main():
    #get the number of rows
    rows = int(input("Enter the number of rows: "))
    #start the timer
    start_time = perf_counter()
    #save and write the output to a file named part2.out
    sys.stdout = open("part2.out", "w")
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
    #close the file
    sys.stdout.close()

if __name__ == "__main__":
    main()