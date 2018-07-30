def isSubsetSum (arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
 
    if arr[n-1] > sum:
        return isSubsetSum (arr, n-1, sum)
 
    
     
    return isSubsetSum (arr, n-1, sum) or isSubsetSum (arr, n-1, sum-arr[n-1])

def findPartion (arr, n):
    sum = 0
    for i in range(0, n):
        sum += arr[i]

    if sum % 2 != 0:
        return False

    return isSubsetSum (arr, n, sum // 2)

def isSubsetSum_memo(arr, n):
  sum = 0
  for i in range(n):
    sum += arr[i]

  if sum%2 != 0:
    return False

  rows = sum // 2 + 1
  cols = n + 1
  # part[sum//2+1][n+1]
  part = [[False for i in range(cols)] for j in range(rows)]

  for i in range(cols):
    part[0][i] = True

  for i in range(1, rows):
    part[i][0] = False

  for i in range(rows):
    for j in range(1, cols):
      part[i][j] = part[i][j-1]
      if i >= arr[j-1]:
        part[i][j] = part[i][j] or part[i - arr[j - 1]][j - 1]
  print(part)
  return part[sum//2][n]
  
def partition_souve(arr):
  pass

arr = [3, 1, 5, 9, 12]
n = len(arr)
if isSubsetSum_memo(arr, n) == True:
    print ("Can be divided into two subsets of equal sum")
else:
    print ("Can not be divided into two subsets of equal sum")