# python3

def cal_fibo_memo(n):
  fibo = [None] * (n + 1)
  fibo[0] = 0
  fibo[1] = 1
  for i in range(2, n + 1):
    fibo[i] = fibo[i-1] + fibo[i-2]
    
  return fibo[n]


if __name__ == '__main__':
  n = int(input())
  print(cal_fibo_memo(n))