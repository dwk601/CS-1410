#human pyramids project with oop approach
import sys
from time import perf_counter

#person Class
class Person:
    #constructor
    def __init__(self, row, col, weight):
        self.row = row
        self.col = col
        self.weight = weight
        self.left = None
        self.right = None
        self.back = None
    #set the left person
    def setLeft(self, left):
        self.left = left
    #set the right person
    def setRight(self, right):
        self.right = right
    #set the back person
    def setBack(self, back):
        self.back = back
    #get the left person
    def getLeft(self):
        return self.left
    #get the right person
    def getRight(self):
        return self.right
    #get the back person
    def getBack(self):
        return self.back
    #get the weight
    def getWeight(self):
        return self.weight
    #get the row
    def getRow(self):
        return self.row
    #get the column
    def getCol(self):
        return self.col
    #get the weight on the back of the person
    def getWeightOnBack(self):
        #if the row and column is 0, means the top position, return 0
        if self.row == 0 and self.col == 0:
            return 0
        #if the column is 0, means the left position, return the weight on the back of the person in row r-1 and and column c
        elif self.col == 0:
            return (self.back.getWeightOnBack() +200)/2.0
        #if the column is r, means the right position, return the weight on the back of the person in row r-1 and and column c-1
        elif self.col == self.row:
            return (self.back.getWeightOnBack() +200)/2.0
        #if the column is neither 0 nor r, means the middle position, return the sum of weight on the back of the person in row r-1 and and column c-1 and the weight on the back of the person in row r-1 and and column c
        else:
            return (self.back.getWeightOnBack() +200)/2.0 + (self.left.getWeightOnBack() +200)/2.0

def main():
    #get the number of rows
    rows = int(input("Enter the number of rows: "))
    #start the timer
    start_time = perf_counter()
    #save and write the output to a file named part4.out
    sys.stdout = open("part4.out", "w")
    #create a list of list to store the persons
    pyramid = []
    #loop through the rows
    for r in range(0, rows):
        #create a list to store the persons in the row
        row = []
        #loop through the columns
        for c in range(0, r+1):
            #create a person
            person = Person(r, c, 0)
            #add the person to the list
            row.append(person)
        #add the list to the list of list
        pyramid.append(row)
    #loop through the rows
    for r in range(0, rows):
        #loop through the columns
        for c in range(0, r+1):
            #if the column is 0, means the left position, set the left person to None
            if c == 0:
                pyramid[r][c].setLeft(None)
            #if the column is r, means the right position, set the right person to None
            elif c == r:
                pyramid[r][c].setRight(None)
            #if the column is neither 0 nor r, means the middle position, set the left and right person
            else:
                pyramid[r][c].setLeft(pyramid[r-1][c])
                pyramid[r][c].setRight(pyramid[r-1][c-1])
            #if the row is 0, means the top position, set the back person to None
            if r == 0:
                pyramid[r][c].setBack(None)
            #if the row is not 0, set the back person
            else:
                pyramid[r][c].setBack(pyramid[r-1][c])
    #loop through the rows
    for r in range(0, rows):
        #loop through the columns
        for c in range(0, r+1):
            #calculate the weight
            weight = pyramid[r][c].getWeightOnBack()
            #print the weight
            print("{:5.1f}".format(weight), end=" ")
        #print a new line
        print()
    #end the timer
    end_time = perf_counter()
    #calculate the time
    time = end_time - start_time
    #print the time
    print("Time: ", time)

if __name__ == "__main__":
    main()