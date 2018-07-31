import sys
from random import randint

def lcm_naive(a, b):
  for l in range(1, a * b + 1):
    if l % a == 0 and l % b == 0:
      return l
  return a * b

def gcd_euclidean(a, b):
  if a == 0:
    return b
  return gcd_euclidean(b % a, a)

def lcm_better(a, b):
  return (a * b) // gcd_euclidean(a, b)



def main():
  count = 0
  while True:
    n1 = randint(1, 200)
    n2 = randint(1, 200)
    f1 = lcm_naive(n1, n2)
    f2 = lcm_better(n1, n2)
    print(n1, n2, f1, f2)
    if f2 != f1:
      print('Error', n1, n2, f1, f2)
      break
    count += 1
    if count == 10000:
      break


if __name__ == '__main__':
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    # print(lcm_better(a, b))
    main()