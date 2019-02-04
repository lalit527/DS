import sys
from collections import defaultdict

def seprate_values_01(arr):
  n = len(arr)
  i = 0
  j = 1
  while i < n and j < n:
    while i < n and arr[i] == 0:
      i +=1
    while j < n and arr[j] == 1:
      j += 1
    if i < n and j < n:
      arr[i], arr[j] = arr[j], arr[i]
  return arr

def partition_3way(arr):
  n = len(arr)
  f = s = float('-inf')
  for i in range(n):
    if arr[i] > f:
      s = f
      f = arr[i]
    elif arr[i] > s and arr[i] != f:
      s = arr[i]
  pivot = s

  _partition_3way(arr, 0, n - 1, pivot)

def _partition_3way(arr, l, r, pivot):
  i = l
  lt = l
  gt = r
  while i <= gt:
    if arr[i] < pivot:
      arr[lt], arr[i] = arr[i], arr[lt]
      lt += 1
      i += 1
    elif arr[i] > pivot:
      arr[i], arr[gt] = arr[gt], arr[i]
      gt -= 1
    else:
      i += 1
  print(pivot)
  print(lt, gt)
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
    
  
if __name__ == "__main__":
  main()

