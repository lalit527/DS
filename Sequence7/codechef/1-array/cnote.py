import sys

def can_buy(x, y, n, k, p, c):
  if x - y <= p and c <= k:
    return True
  return False

def main():
  line = sys.stdin.read()
  data = list(map(int, line.split()))
  num_cases = data[0]
  data = data[1:]
  for _ in range(num_cases):
    x = data[0]
    y = data[1]
    n = data[2]
    k = data[3]
    j = 4
    for i in range(n):
      p = data[j] 
      c = data[j + 1] 
      j += 2
      flag = can_buy(x, y, n, k, p, c)
      if flag:
        print('LuckyChef')
        break
    if not flag:
      print('UnluckyChef')
    data = data[4 + (n * 2):]

if __name__ == "__main__":
  main()