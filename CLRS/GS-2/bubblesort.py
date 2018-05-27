def bubble_sort(arr):
  for i in range(len(arr) - 1):
    for j in range(len(arr) - 1, i, -1):
      if arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]

arr = [5, 2, 4, 6, 1, 3]
bubble_sort(arr)
print(arr)