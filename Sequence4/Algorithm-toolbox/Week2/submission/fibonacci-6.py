# python3
import sys

def fibonacci_sum_better(n):
  n = n % 60
  if n <= 1:
    return n
  previous = 0
  current  = 1
  sum      = 1
  for _ in range(n - 1):
    previous, current = current, (previous + current % 10)
    sum += current
    sum %= 10

  return sum

if __name__ == '__main__':
  input = sys.stdin.read()
  n = int(input)
  print(fibonacci_sum_better(n))