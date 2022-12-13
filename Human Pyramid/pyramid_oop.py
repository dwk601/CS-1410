#human pyramids project with oop approach
import sys
from time import perf_counter

#person Class
class Person:
  def __init__(self, row, col, weight):
    self.row = row
    self.col = col
    self.weight = weight
    self.shoulder = None
  
  def weight_on(self):
    if self.shoulder is not None:
      return self.shoulder
    else:
      # Recursively compute the weight on the person's shoulder
      # and store the result in self.shoulder
      self.shoulder = self.weight + ...
      return self.shoulder

def main():
  # Parse command line arguments
  if len(sys.argv) != 2:
    print("Usage: python pyramid.py n")
    sys.exit(1)
  n = int(sys.argv[1])

  # Create a list of lists of Person objects
  pyramid = []
  for r in range(n):
    row = []
    for c in range(r + 1):
      row.append(Person(r, c, 75 * r + 100 * c))
    pyramid.append(row)

  # Calculate weights and print results
  start_time = perf_counter()
  for r in range(n):
    row = []
    for c in range(r + 1):
      row.append(f"{pyramid[r][c].weight_on():.2f}")
    print(' '.join(row))
  end_time = perf_counter()

  # Print elapsed time and number of function calls
  print(f"Elapsed time: {end_time - start_time} seconds")
  print(f"Number of function calls: {Person.calls}")

if __name__ == '__main__':
  main()