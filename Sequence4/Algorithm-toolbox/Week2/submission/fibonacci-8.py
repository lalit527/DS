# python3
import sys

def fibonacci_sum_squares_better(n):
  n = n % 30
  if n <= 1:
    return n
  fibo = [None] * (n + 1)
  fibo[0] = 0
  fibo[1] = 1
  sum = 1
  for i in range(2, n + 1):
    fibo[i] = (fibo[i - 2] + fibo[i - 1]) % 10
    sum += (fibo[i] * fibo[i])
    sum %= 10
  return sum

if __name__ == '__main__':
  input = sys.stdin.read()
  n = int(input)
  print(fibonacci_sum_squares_better(n))