# Uses python3
import sys
from random import randint

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def get_majority_element_betr(a, s, n):
  length = n - s
  if length >= 1:
    if a[0] == a[1]:
      return a[0]
    else:
      return -1
  elif length == 1:
    return a[0]

  mid = (s + n) // 2
  left = get_majority_element_betr(a, s, mid)
  right = get_majority_element_betr(a, mid + 1, n)

  if left == -1 and right >= 0:
    return right

  if right == -1 and left >=0:
    return left

  if left == right:
    return left
  else:
    return -1

def get_majority_element_naive(a, s, n):
  for i in a:
    cur_ele = i
    count = 0
    for j in a:
      if i == j:
        count += 1
    if count > n//2:
      return i
  return -1

def count(a, num):
  count = 0
  n = len(a)
  print('count', a, num)
  for i in range(n):
    if a[i] == num:
      count += 1
  return count 

def get_majority_element_better(a, s, e):
  if s == e:
    return a[s]
  mid = (e - s) // 2 + s
  print('s-e', s, e, 'mid--', mid)
  left = get_majority_element_better(a, s, mid)
  right = get_majority_element_better(a, mid + 1, e)
  print('left-right', left, right, 'mid--', mid)
  
  if left == right:
    return left
  
  left_count = count(a, left)
  right_count = count(a, right)

  print('lcount-rcount', left_count, right_count)

  return left if left_count > len(a) // 2 else right if right_count > len(a) // 2 else -1


def main():
  n = randint(1, 100)
  a = []
  count = 1
  while True:
    for _ in range(n):
      a.append(randint(1, 100))
    n1 = get_majority_element_naive(a, 0, n-1)
    n2 = get_majority_element_better(a, 0, n-1)
    print(a)
    print(n1, n2)
    if (n1 == -1 and n2 != -1) or (n1 == 1 and n2 != -1):
      print('Error', a, n1, n2)
      break
    count += 1
    if count == 10000:
      break

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    ele = get_majority_element_naive(a, 0, n - 1) 
    print(ele)
    if ele != -1:
        print(1)
    else:
        print(0)
    # main()
