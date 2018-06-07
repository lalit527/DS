# python3
from random import randint

def cal_fibo_memo(n):
  fibo = [None] * (n + 1)
  fibo[0] = 0
  fibo[1] = 1
  for i in range(2, n + 1):
    fibo[i] = fibo[i-1] + fibo[i-2]
    
  return fibo[n]

def cal_last_digit(n):
  fibo = [None] * (n + 1)
  fibo[0] = 0
  fibo[1] = 1
  for i in range(2, n + 1):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % 10
    
  return fibo[n]

def main():
  count = 0
  while True:
    n = randint(1, 200)
    f1 = cal_fibo_memo(n)
    f2 = cal_last_digit(n)
    print(n, f1, f2)
    if f2 != (f1 % 10):
      print('Error', n, f1, f2)
      break
    count += 1
    if count == 10000:
      break

if __name__ == '__main__':
  n = int(input())
  print(cal_fibo_memo(n))
  # main()

