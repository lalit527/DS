from stack import Stack

def print_stack(s):
  n = s.size
  top = s.top
  while n > 0:
    print(top.data)
    top = top.prev
    n -= 1

def merge_sort(s):
  if s is None or s.size <= 1:
    return s
  
  left = Stack()
  right = Stack()
  count = 0
  while s.size != 0:
    count += 1
    if count % 2== 0:
      left.push(s.pop())
    else:
      right.push(s.pop())

  left = merge_sort(left)
  right = merge_sort(right)
  merge(s, left, right)

def merge(s, left, right):
  while (left and left.size > 0) or (right and right.size > 0):
    if left and left.size == 0:
      s.push(right.pop())
    elif right and right.size == 0:
      s.push(left.pop())
    elif right.peek() > left.peek():
      s.push(left.pop())
    else:
      s.push(right.pop())
  


def sort_stack(s):
  r = Stack()
  while s.size > 0:
    tmp = s.pop()
    while r.size > 0 and tmp < r.peek():
      s.push(r.pop())
    r.push(tmp)
  
  while r.size > 0:
    s.push(r.pop())

S = Stack()
S.push(5)
S.push(10)
S.push(7)
S.push(12)
S.push(8)
S.push(3)
S.push(1)
merge_sort(S)
print_stack(S)