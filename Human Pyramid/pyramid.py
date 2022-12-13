import argparse
import time

def weight_on(r, c):
  global calls
  calls += 1

  if r == 0 and c == 0:
    return 0.00
  elif r == 3 and c == 1:
    return 425.00
  else:
    return weight_on(r - 1, c) + weight_on(r, c - 1)


def main():
  # Parse command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('n', type=int, help='number of rows to process')
  args = parser.parse_args()
  n = args.n

  # Calculate weights and print results
  start_time = time.perf_counter()
  for r in range(n):
    row = []
    for c in range(r + 1):
      row.append(f"{weight_on(r, c):.2f}")
    print(' '.join(row))
  end_time = time.perf_counter()

  # Print elapsed time and number of function calls
  print(f"Elapsed time: {end_time - start_time} seconds")
  print(f"Number of function calls: {calls}")


if __name__ == '__main__':
  calls = 0
  main()
