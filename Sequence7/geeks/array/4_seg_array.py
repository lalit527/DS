import sys
from collections import defaultdict

def seprate_values_01(arr):
  n = len(arr)
  i = j = 0
  while i < n or j < n:
    while arr[i] == 0:
      i +=1
    while arr[j] == 1:
      j += 1
    if i < n and j < n:
      arr[i], arr[j] = arr[j], arr[i]
  print(arr)


def main():
  n = int(sys.stdin.readline())
  data = []
  for _ in range(n):
    c = sys.stdin.readline()
    tmp = []
    tmp.extend(sys.stdin.readline().split())
    tmp = list(map(lambda x: int(x), tmp))
    data.append(tmp)
    print(seprate_values_01(tmp))
  
if __name__ == "__main__":
  main()
