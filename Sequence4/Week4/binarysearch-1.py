# Uses python3
import sys
from random import randint

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    while left < right:
      mid = (right + left) // 2
      if a[mid] == x:
        return mid
      elif a[mid] > mid:
        right = mid - 1
      else:
        left = mid + 1
    return -1

def linear_search(a, x):
  for i in range(len(a)):
    if a[i] == x:
      return i
  return -1


def main():
  count = 0
  while True:
    a = []
    b = []
    for i in range(10):
      d1 = randint(1, 9)
      d2 = randint(1, 9)
      a.append(d1)
      b.append(d2)
    a = set(a)
    b = set(b)
    a = list(a)
    b = list(b)
    print(a)
    print(b)
    a_r = ''
    b_r = ''
    for x in b:
      a_r += str(binary_search(a, x))
    for x in b:
      b_r += str(linear_search(a, x))
    if a_r != b_r:
      print(a)
      print(b)
      print(a_r)
      print(b_r)
      break
    count += 1
    if count == 100000:
      break
if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[n + 1]
    # a = data[1 : n + 1]
    # for x in data[n + 2:]:
    #     # replace with the call to binary_search when implemented
    #     print(binary_search(a, x), end = ' ')
    main()
