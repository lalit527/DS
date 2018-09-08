import sys

def majority_element_naive(a, s, e):
  for i in range(e+1):
    current = a[i]
    count = 0
    for j in range(e+1):
      if a[i] == a[j]:
        count += 1
    if count > (e//2):
      return a[i]
  return ""

def count(a, s, e, x):
  count = 0
  for i in range(s, e+1):
    if a[i] == x:
      count += 1
  return count

def majority_element_dnc(a, s, e):
  if s == e:
    return a[e]
  mid = ((e - s) // 2) + s
  left = majority_element_dnc(a, s, mid)
  right = majority_element_dnc(a, mid + 1, e)

  if left == right:
    return left
  
  left_count = count(a, s, e, left)
  right_count = count(a, s, e, right)

  if left_count > ((e - s + 1) // 2):
    return left
  elif right_count > ((e - s + 1) // 2):
    return right
  else:
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    ele = majority_element_dnc(a, 0, n-1) 
    if ele != -1:
        print(1)
    else:
        print(0)