def merge(A, start, mid, end):
  l = (mid - start + 1)
  r = (end - mid)
  left = [None] * l
  right = [None] * r
  k = 0
  for i in range(start, mid+1):
    left[k] = A[i]
    k += 1
  
  k = 0
  for j in range(mid+1, end+1):
    right[k] = A[j]
    k += 1

  i = 0
  j = 0
  k = start
  while i < l and j < r:
    if left[i] < right[j]:
      A[k] = left[i]
      i += 1
    else:
      A[k] = right[j]
      j += 1
    k += 1

  while i < l:
    A[k] = left[i]
    i += 1
    k += 1
  
  while j < r:
    A[k] = right[j]
    j += 1
    k += 1



def merge_sort(A):
  n = len(A)
  _merge_sort(A, 0, n - 1)



def _merge_sort(A, start, end):
  if start >= end:
    return
  mid = (start + end) // 2
  _merge_sort(A, start, mid)
  _merge_sort(A, mid+1, end)
  merge(A, start, mid, end)


def main():
  A = [9, 8 , 5, 1, 7, 6]
  merge_sort(A)
  print(A)

if __name__ == "__main__":
  main()