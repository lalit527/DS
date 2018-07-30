# python3

def cal_last_digit(n):
  fibo = [None] * (n + 1)
  fibo[0] = 0
  fibo[1] = 1
  for i in range(2, n + 1):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % 10
    
  return fibo[n]

if __name__ == '__main__':
  n = int(input())
  print(cal_last_digit(n))