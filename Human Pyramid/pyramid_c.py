import sys
from time import perf_counter

from time import time

# A module-level cache to store previously computed results
# The key is the tuple (r, c) and the value is the previously computed weight
cache = {}

def weight_on(r, c):
  if r > 23:
    return 0

  # Check if the weight has been previously computed
  if (r, c) in cache:
    # Return the previously computed value
    return cache[(r,c)]

  # Compute the weight by adding the weights of the people above it
  weight = 75 * r + 100 * c
  weight += weight_on(r + 1, c)
  weight += weight_on(r + 1, c + 1)

  # Save the computed value in the cache before returning it
  cache[(r,c)] = weight
  return weight

def main():
  # Parse command line arguments
  if len(sys.argv) != 2:
    print("Usage: python pyramid.py n")
    sys.exit(1)
  n = int(sys.argv[1])

  # Calculate weights and print results
  start_time = perf_counter()
  for r in range(n):
    row = []
    for c in range(r + 1):
      row.append(f"{weight_on(r, c):.2f}")
    print(' '.join(row))
  end_time = perf_counter()

  # Print elapsed time and number of function calls
  print(f"Elapsed time: {end_time - start_time} seconds")
  print(f"Number of function calls: {len(cache)}")

if __name__ == '__main__':
  main()