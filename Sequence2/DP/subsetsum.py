def hasSubset(arr, n, sum):
  if sum == 0:
    return True
  
  if sum > 0 and n < 0:
    return False

  if arr[n-1] > sum:
    return hasSubset(arr, n-1, sum)
  
  return hasSubset(arr, n-1, sum) or hasSubset(arr, n-1, sum - arr[n-1])


def hasSubset_memo(arr, n, sum):
  subset = [[True] * (sum + 1)] * (n+1)
  
  # if sum is 0 answer is true
  for i in range(0, n+1):
    subset[i][0] = True

  # if sum is not 0 and array is empty, return False
  for j in range(1, sum+1):
    subset[0][j] = False
  
  for i in range(1, n+1):
    for j in range(1, sum+1):
      if j < arr[i-1]:
        subset[i][j] = subset[i-1][j]
      elif j>= arr[i-1]:
        subset[i][j] = subset[i-1][j] or subset[i-1][j - arr[i-1]]

  return subset[n][sum]





arr = [1, 2, 3]
sum = 7
n = len(arr)
print(hasSubset_memo(arr, n, sum))