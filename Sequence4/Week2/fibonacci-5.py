# Uses python3
import sys
from random import randint

def get_pisano_period(m):
  a = 0
  b = 1
  for i in range(m * m):
    c = (a + b) % m
    a = b
    b = c
    if a == 0 and b == 1:
      return i + 1
  return m

def get_fibo_huge_naive(n, m):
  if n <= 1:
    return n
  previous = 0
  current = 1
  for _ in range(n - 1):
    previous, current = current, previous + current

  return current % m

def get_fibo_huge_last(n, m):
  if n <= 1:
    return n
  previous = 0
  current = 1
  for _ in range(n - 1):
    previous, current = current, (previous + current) % m

  return current % m

def get_fibo_huge_better(n, m):
  if n <= 1:
    return n

  previous = 0
  current = 1
  new_fibo = get_pisano_period(m)
  for _ in range(new_fibo - 1):
    previous, current = current, (previous + current) % m

  return current % m

def main():
  count = 0
  while True:
    n1 = randint(1, 20)
    n2 = randint(1, 10)
    f1 = get_fibo_huge_better(n1, n2)
    f2 = get_fibo_huge_last(n1, n2)
    print(n1, n2, f1, f2)
    if f2 != f1:
      print('Error', n1, n2, f1, f2)
      break
    count += 1
    if count == 10000:
      break

def test():
  count = 0
  while True:
    n = get_pisano_period(count)
    print(count, n)
    count += 1
    if count == 1000:
      break



if __name__ == '__main__':
  # main()
  test()
    # input = sys.stdin.read();
    # n, m = map(int, input.split())
    # print(get_fibo_huge_naive(n, m))
    # print(get_fibo_huge_better(10, 5))