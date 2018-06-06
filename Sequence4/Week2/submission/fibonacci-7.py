# python3
import sys

def fibonacci_partial_sum_better(from_, to):
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

if __name__ == '__main__':
  input = sys.stdin.read();
  from_, to = map(int, input.split())
  print(fibonacci_partial_sum_better(from_, to))