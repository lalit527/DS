# python3
import sys


def count(a, num, s, e):
  count = 0
  n = e - s
  for i in range(s, e + 1):
    if a[i] == num:
      count += 1
  return count 

def get_majority_element_better(a, s, e):
  if s == e:
    return a[s]
  mid = (e - s) // 2 + s
  left = get_majority_element_better(a, s, mid)
  right = get_majority_element_better(a, mid + 1, e)
  
  if left == right:
    return left
  
  left_count = count(a, left, s, e)
  right_count = count(a, right, s, e)

  return left if left_count > ((e-s+1) // 2) else right if right_count > ((e-s+1) // 2) else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    ele = get_majority_element_better(a, 0, n-1) 
    if ele != -1:
        print(1)
    else:
        print(0)