import sys

def missing_element(arr):
  # n = len(arr) - 1
  n = arr[-1]
  expected = (n * (n + 1)) // 2
  actual = arr[0]
  for e in arr[1:]:
    actual += e
  return expected - actual

def missing_element_better(arr):
  n = len(arr)
  x = arr[0]
  y = 1
  for i in range(1, n):
    x  = x ^ arr[i]

  for i in range(2, n+2):
    y = y ^ i

  return (x ^ y)

def main():
  n = int(sys.stdin.readline())
  data = []
  for _ in range(n):
    c = int(sys.stdin.readline())
    tmp = []
    tmp.extend(sys.stdin.readline().split())
    tmp = list(map(lambda x: int(x), tmp))
    data.append(tmp)
    print(missing_element_better(tmp))
  
if __name__ == "__main__":
  main()
