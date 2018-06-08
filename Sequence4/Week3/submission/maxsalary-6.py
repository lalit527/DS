#Uses python3

import sys

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

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number_fixed(a))