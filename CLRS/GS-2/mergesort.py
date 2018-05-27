def merge_sort(arr):
  _merge_sort(arr, 0, len(arr) - 1)

def _merge_sort(arr, start, end):
  if start < end:
    mid = (start + end) // 2
    _merge_sort(arr, start, mid)
    _merge_sort(arr, mid + 1, end)
    _merge_opt(arr, start, mid, end)

def _merge(arr, start, mid, end):
  l = mid - start + 1
  r = end - mid
  left = [None] * (l + 1)
  right = [None] * (r + 1)

  for i in range(l):
    left[i] = arr[start + i]

  for i in range(r):
    right[i] = arr[mid + i + 1]

  left[l] = float('inf')
  right[r] = float('inf')

  i = 0
  j = 0
  k = start
  for k in range(start, end + 1):
    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1

def _merge_opt(arr, start, mid, end):
  l = mid - start + 1
  r = end - mid
  left = [None] * (l)
  right = [None] * (r)

  for i in range(l):
    left[i] = arr[start + i]

  for i in range(r):
    right[i] = arr[mid + i + 1]

  i = 0
  j = 0
  k = start

  while (i < l) and (j < r):
    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1
      k += 1
    else:
      arr[k] = right[j]
      j += 1
      k += 1

  while i < l:
    arr[k] = left[i]
    i += 1
    k += 1

  while j < r:
    arr[k] = right[j]
    j += 1
    k += 1





arr = [5, 2, 4, 6, 1, 3]
merge_sort(arr)
print(arr)