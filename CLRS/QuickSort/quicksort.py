import random

def _quicksort(arr, s, e):
  if s < e:
    q = hoare_partition(arr, s, e)
    _quicksort(arr, s, q-1)
    _quicksort(arr, q+1, e)

def partition(arr, s, e):
  x = arr[e]
  i = s - 1
  for j in range(s, e):
    if arr[j] <= x:
      i = i + 1
      arr[j], arr[i] = arr[i], arr[j]
  arr[i + 1], arr[e] = arr[e], arr[i+1]
  return i + 1

def random_partition(arr, s, e):
  i = random.randint(s, e)
  arr[i], arr[e] = arr[e], arr[i]
  return partition(arr, s, e)

def quicksort(arr):
  n = len(arr)
  _quicksort(arr, 0, n-1)


def hoare_partition(arr, s, e):
  x = arr[s]
  i = s
  j = e
  done = False
  while not done:
    while j <= e and arr[j] < x:
      j -= 1
    while i<= e and arr[i] >= x:
      i += 1
    if i < j:
      arr[i], arr[j] = arr[j], arr[i]
    else:
      done = True
  return j

arr = [ 12, 11, 13, 5, 6, 7]
quicksort(arr)
print(arr)