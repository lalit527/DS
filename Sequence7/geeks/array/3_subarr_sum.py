import sys
from collections import defaultdict

def subarray_sum_naive(arr, val):
  n = len(arr)
  for i in range(n):
    value = arr[i]
    for j in range(i+1, n):
      if value + arr[j] < val:
        value += arr[j]
      elif value + arr[j] == val:
        return (i, j)
      else:
        break
  return (-1, -1)


def subarray_sum(arr, val):
  n = len(arr)
  cur_sum = arr[0]
  start = end = 0
  i = 1
  # import pdb; pdb.set_trace()
  while i <= n:
    while cur_sum > val and start < i - 1:
      cur_sum = cur_sum - arr[start]
      start += 1
    
    if cur_sum == val:
      return (start, i-1)

    if i < n:
      cur_sum = cur_sum + arr[i]
    i += 1
  return (-1, -1)

def subarray_sum_hash(arr, val):
  n = len(arr)
  count = value = 0
  D = defaultdict(lambda: 0)
  D[0] = 1
  for i in range(n):
    value += arr[i]
    if D[value - val]:
      count += D[value - val]
    D[value] = D[value] + 1
  return count

def main():
  n = int(sys.stdin.readline())
  data = []
  for _ in range(n):
    c, val = sys.stdin.readline().split()
    tmp = []
    tmp.extend(sys.stdin.readline().split())
    tmp = list(map(lambda x: int(x), tmp))
    data.append(tmp)
    print(subarray_sum_hash(tmp, int(val)))
  
if __name__ == "__main__":
  main()
