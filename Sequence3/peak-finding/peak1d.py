def peak_finder(arr):
  n = len(arr)
  max_index = 0
  for i in range(n):
    if i == 0 and arr[i] > arr[i + 1]:
      print(arr[i])
    elif (i == n - 1) and arr[i] > arr[i - 1]:
      print(arr[i])
    elif arr[i - 1] <= arr[i] >= arr[i + 1]:
      print(arr[i])



arr = [1, 3, 20, 4, 1, 7]
n = len(arr)
peak_finder(arr)