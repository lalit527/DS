def find_max_crossing_subarray(A, low, mid, high):
  left_sum = float('-inf')
  total = 0
  max_left = -1
  max_right = -1
  for i in range(mid, low-1, -1):
    total += A[i]
    if total > left_sum:
      left_sum = total
      max_left = i 
  right_sum = float('-inf')
  total = 0
  for i in range(mid + 1, high + 1):
    total += A[i]
    if total > right_sum:
      right_sum = total
      max_right = i
  return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(A, low, high):
  if high == low:
    return (low, high, A[low])
  else:
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_subarray(A, low, mid)
    right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)

    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
      return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
      return (right_low, right_high, right_sum)
    else:
      return (cross_low, cross_high, cross_sum )


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print(find_max_subarray(A, 0, len(A) - 1))