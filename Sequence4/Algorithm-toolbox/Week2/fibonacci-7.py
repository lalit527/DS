# Uses python3
import sys
from random import randint

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_better(from_, to):
    sum = 0
    if from_ <= 1:
      sum = 1
    fibo = [None] * (to + 1)
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, to + 1):
      fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 10
      if i >= from_:
        sum += fibo[i] 
        sum %= 10
    # print(fibo)
    return sum

def fibonacci_partial_sum_pisano(from_, to):
  if from_ == 0  and to == 0:
    return 0
  if from_ > to:
    return 0

  from_ %= 60
  to %= 60
  if to < from_:
    to += 60
  sum = 0
  if from_ <= 1:
    sum = 1
  fibo = [None] * (to + 1)
  fibo[0] = 0
  fibo[1] = 1
  for i in range(2, to + 1):
    fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 10
    if i >= from_:
      sum += fibo[i] 
      sum %= 10
  return sum


def main():
  count = 0
  while True:
    n1 = randint(1, 200)
    n2 = randint(n1, 200)
    f1 = fibonacci_partial_sum_naive(n1, n2)
    f2 = fibonacci_partial_sum_pisano(n1, n2)
    print(n1, n2, f1, f2)
    if f2 != f1:
      print('Error', n1, n2, f1, f2)
      break
    count += 1
    if count == 1000:
      break

if __name__ == '__main__':
    # input = sys.stdin.read();
    # from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_pisano(from_, to))
    #print(get_pisano_period(100000000))
  main()