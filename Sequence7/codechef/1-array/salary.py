import sys

def min_moves(n, W):
  s = 0
  _min = float('inf')
  for i in W:
    if i < _min:
      _min = i
    s += i
  return s - (n * _min)

def main():
  line = sys.stdin.read()
  data = list(map(int, line.split()))
  num_cases = data[0]
  data = data[1:]
  for _ in range(num_cases):
    n = data[0]
    W = data[1:n + 1]
    print(min_moves(n, W))
    data = data[n + 1:]

if __name__ == "__main__":
  main()