import sys

def get_alt(a, n):
  result = [1] * n
  for i in range(n - 1, 0, -1):
    if a[i] * a[i + 1] < 0:
      result[i] = result[i + 1] + 1
    else:
      result[i] = 1
  print(result)

def main():
  num_cases = int(sys.stdin.readline())
  for _ in range(num_cases):
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split(' ')))
    get_alt(A, n)

if __name__ == "__main__":
  main()