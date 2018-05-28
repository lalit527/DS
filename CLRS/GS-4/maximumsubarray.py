def max_sum_bf(arr):
  n = len(arr)
  sum_till_now = float('-inf')
  max_sum_till_now = float('-inf')

  for i in range(n):
    sum_till_now = arr[i]
    for j in range(i+1, n):
      sum_till_now += arr[j]
      if sum_till_now > max_sum_till_now:
        max_sum_till_now = sum_till_now
  
  print(max_sum_till_now, sum_till_now)

def find_max_crossing_subarray(A, low, mid, high):
  left_sum = float('-inf')
  sum_till_now = 0
  max_left = -1
  for i in range(mid, low - 1, -1):
    sum_till_now += A[i]
    if sum_till_now > left_sum:
      left_sum = sum_till_now
      max_left = i
  
  right_sum = float('-inf')
  sum_till_now = 0
  max_right = -1
  for j in range(mid + 1, high + 1):
    sum_till_now += A[j]
    if sum_till_now > right_sum:
      right_sum = sum_till_now
      max_right = j
  return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(A, low, high):
  if high == low:
    return (low, high, A[low])
  mid = (low + high) // 2
  left_low, left_high, left_sum = find_max_subarray(A, low, mid)
  right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
  cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

  if left_sum >= right_sum and left_sum >= cross_sum:
    print("left")
    return (left_low, left_high, left_sum)
  elif right_sum >= left_sum and right_sum >= cross_sum:
    print("right")
    return (right_low, right_high, right_sum)
  else:
    print("cross")
    return (cross_low, cross_high, cross_sum)


# arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
arr = [2, 3, 4, 5, 7]
# max_sum_bf(arr)
print(find_max_subarray(arr, 0, 4))
