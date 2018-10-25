import sys
from collections import deque

def next_greater(n, W):
  S = deque()
  n = len(W) - 1
  S.append(W[n])
  for i in W[n - 1::-1]:
    if S[-1] > i:
      break
    else:
      S.append(i)
  print(S)
   

def main():
  num_cases = int(sys.stdin.readline().strip())
  for _ in range(num_cases):
    n = sys.stdin.readline().strip()
    W = list(map(int, sys.stdin.readline().strip().split(' ')))
    print(next_greater(n, W))

if __name__ == "__main__":
  main()