import sys
from random import randint

def gcd_naive(a, b):
  current_gcd = 1
  for d in range(2, min(a, b) + 1):
    if a % d == 0 and b % d == 0:
      if current_gcd < d:
        current_gcd = d

  return current_gcd

def gcd_euclidean(a, b):
  if a == 0:
    return b
  return gcd_euclidean(b % a, a)


def gcd_extended_euclidean(a, b, x, y):
  if a == 0:
    x = 0
    y = 1
    return b

  x1 = 1
  y1 = 1
  gcd = gcd_extended_euclidean(b % a, a, x1, y1)
  
  x = y1 - (b//a) * x1
  y = x1 
  return gcd

def main():
  count = 0
  while True:
    n1 = randint(1, 200)
    n2 = randint(1, 200)
    f1 = gcd_euclidean(n1, n2)
    f2 = gcd_extended_euclidean(n1, n2, 1, 1)
    print(n1, n2, f1, f2)
    if f2 != f1:
      print('Error', n1, n2, f1, f2)
      break
    count += 1
    if count == 10000:
      break


if __name__ == "__main__":
  # input = sys.stdin.read()
  # a, b = map(int, input.split())
  # print(gcd_euclidean(a, b))
  main()