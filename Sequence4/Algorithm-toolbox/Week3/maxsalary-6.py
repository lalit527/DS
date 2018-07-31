#Uses python3
from random import randint
import sys
def largest_number(a):
  #write your code here
  res = ""
  while len(a) > 0:
    max_digit = 0
    for i in range(len(a)):
      if int(a[i]) > int(a[max_digit]):
        max_digit = i
    res += a[max_digit]
    a.pop(max_digit)
  for x in a:
    res += x
  return res

# def is_current_max(cur, next):
#   n = len(cur)
#   m = len(next)
#   print(cur, next)
#   if n == m:
#    if cur < next:
#     return True
#   else:
#     i = 0
#     j = 0
#     while i < n and j < m:
#       print(i, j)
#       if cur[i] == cur[j] and n > m:
#         i += 1
#       elif cur[i] == cur[j] and m > n:
#         print(cur[i], cur[j])
#         j += 1
#       elif cur[i] > cur[j]:
#         return True
#       elif cur[i] < cur[j]:
#         return False
#  # return False

# def is_current_max(cur, next):
#   n = len(cur)
#   m = len(next)
#   if n == m:
#     if cur > next:
#       return True
#     else:
#       return False
#   i = 0
#   j = 0
#   while True:
#     if cur[i] > next[j]:
#       return True
#     elif cur[i] < next[j]:
#       return False
#     else:
#       if n > m:
#         i += 1
#         n -= 1
#         if m > 1:
#           m -= 1
#           j += 1
#       elif n < m:
#         j += 1
#         m -= 1
#         if n > 1:
#           n -= 1
#           i += 1
#       else:
#         return cur[i:] > next[j:]
#   return False

def is_current_max(cur, next):
  while True:
    if cur[0] > next[0]:
      return True
    elif cur[0] < next[0]:
      return False
    else:
      if len(cur) == len(next):
        return cur > next
      cur = cur[1:] or cur
      next = next[1:] or next

def is_current_max_better(cur, next):
  s = cur + next
  t = next + cur
  if int(s) > int(t):
    return True
  else:
    return False


def largest_number_fixed(a):
  #write your code here
  res = ""
  while len(a) > 0:
    max_digit = 0
    for i in range(1, len(a)):
      if is_current_max_better(a[i], a[max_digit]):
        max_digit = i
    res += a[max_digit]
    a.pop(max_digit)
  for x in a:
    res += x
  return res

## To test custom solution
def largest_number_fixed2(a):
  #write your code here
  res = ""
  while len(a) > 0:
    max_digit = 0
    for i in range(1, len(a)):
      if is_current_max(a[i], a[max_digit]):
        max_digit = i
    res += a[max_digit]
    a.pop(max_digit)
  for x in a:
    res += x
  return res


def largest_number_merging(a):
  #write your code here
  result = "".join(a)
  a = [character for character in result]
  res = ""
  while len(a) > 0:
    max_digit = 0
    for i in range(len(a)):
      if int(a[i]) > int(a[max_digit]):
        max_digit = i
    res += a[max_digit]
    a.pop(max_digit)
  for x in a:
    res += x
  return res


def main():
  count = 0
  while True:
    n = randint(1, 20)
    arr = []
    for _ in range(5):
      num = randint(1, 9999)
      arr.append(str(num))
      num = randint(1, 999)
      arr.append(str(num))
      num = randint(1, 99)
      arr.append(str(num))
      num = randint(1, 9)
      arr.append(str(num))
    arr2 = arr[:]
    print(arr)
    print(arr2)
    n1 = largest_number_fixed(arr)
    n2 = largest_number_fixed2(arr2)
    if n1 != n2:
      print('Error')
      print(n1, '<=======>', n2)
      break
    count += 1

    if count == 10:
      break


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = input.split()
    # a = data[1:]
    # print(largest_number_fixed(a))

  main()
    
