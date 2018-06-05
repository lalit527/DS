# python3
from random import randint

def cal_fibo_itr(n):
  if (n <= 1):
    return n
  previous = 0
  current = 1
  for _ in range(n - 1):
    previous, current = current, current + previous
  
  return current


def cal_fibo(n):
  if (n <= 1):
    return n

  return cal_fibo(n - 1) + cal_fibo(n - 2)


def cal_fibo_memo(n):
  fibo = [None] * (n + 1)
  fibo[0] = 0
  fibo[1] = 1
  for i in range(2, n + 1):
    fibo[i] = fibo[i-1] + fibo[i-2]
    
  return fibo[n]


def main():
  count = 0
  while True:
    n = randint(1, 20)
    f1 = cal_fibo_itr(n)
    f2 = cal_fibo_memo(n)
    print(n, f1, f2)
    if f1 != f2:
      print('Error', n, f1, f2)
      break
    count += 1
    if count == 10000:
      break

if __name__ == '__main__':
  n = int(input())
  print(cal_fibo(n))
  # main()

