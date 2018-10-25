import sys
from collections import defaultdict

def does_exsit(A, D):
  result = []
  for i in A:
    result.append(D[i])
  return result

def main():
  D = defaultdict(lambda: 'NO')
  num_cases = int(sys.stdin.readline())
  for _ in range(num_cases):
    n, k = sys.stdin.readline().split()
    forgotten = sys.stdin.readline().strip().split(' ')
    for _ in range(int(k)):
      data = sys.stdin.readline().split()
      l, current = data[0], data[1:]
      for i in current:
        D[i] = 'YES'
    result = does_exsit(forgotten, D)
    print(' '.join(result))
    
if __name__ == "__main__":
  main()