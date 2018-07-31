# Uses python3
import sys
from random import randint

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    # print(previous)
    # print(current)
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
        # print(current)

    return sum % 10

def fibonacci_sum_better(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    # print(previous)
    # print(current)
    for _ in range(n - 1):
        previous, current = current, (previous + current % 10)
        sum += current
        sum %= 10
        # print(current)

    return sum

def fibonacci_sum_show(n):
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

def fibonacci_sum_rep(n):
    # n = n % 60
    # if n <= 1:
    #   return n
    fibo = [None] * (n + 1)
    fibo[0] = 0
    fibo[1]  = 1
    fibo2 = [None] * (n + 1)
    fibo2[0] = 0
    fibo2[1]  = 1
    for i in range(2, n+1):
      fibo[i] = (fibo[i-1] + fibo[i-2]) % 10
      fibo2[i] = (fibo2[i-1] % 10 + fibo2[i-2] % 10) % 10
        # previous, current = current, (previous + current % 10)
        # sum += current
        # sum %= 10
        # print(current, previous)
    print(fibo)
    print(fibo2)
    return 1

def main():
  count = 0
  while True:
    n1 = randint(1, 200)
    f1 = fibonacci_sum_naive(n1)
    f2 = fibonacci_sum_show(n1)
    print(n1, f1, f2)
    if f2 != f1:
      print('Error', n1, f1, f2)
      break
    count += 1
    if count == 1000:
      break


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_rep(n))
    # main()
