import sys

def make_happy(n, k, A):
  sum = 0
  for i in range(n):
    sum += A[i]
    if sum > k:
      return 'No'
  return 'Yes'

def main():
  line = sys.stdin.read()
  data = list(map(int, line.split()))
  num_cases = data[0]
  data = data[1:]
  for _ in range(num_cases):
    n = data[0]
    k = data[1]
    A = data[2: 2 + n]
    data = data[2+n:]
    print(make_happy(n, k, A))

if __name__ == "__main__":
  main()