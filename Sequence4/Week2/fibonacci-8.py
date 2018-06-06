# Uses python3
from sys import stdin
from random import randint

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares_test(n):
  if n <= 1:
    return n
  fibo = [None] * (n + 1)
  fibo2 = [None] * (n + 1)
  fibo[0] = 0
  fibo[1] = 1
  fibo2[0] = 0
  fibo2[1] = 1
  for i in range(2, n + 1):
    fibo[i] = (fibo[i - 2] + fibo[i - 1]) % 10
    fibo2[i] = (fibo[i] * fibo[i]) % 10
  print(fibo)
  print(fibo2)
  return fibo[n]

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


def main():
  count = 0
  while True:
    n1 = randint(0, 200)
    f1 = fibonacci_sum_squares_naive(n1)
    f2 = fibonacci_sum_squares_better(n1)
    print(n1, f1, f2)
    if f2 != f1:
      print('Error', n1, f1, f2)
      break
    count += 1
    if count == 10000:
      break


if __name__ == '__main__':
    # n = int(stdin.read())
    # print(fibonacci_sum_squares_better(n))
  main()