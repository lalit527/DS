import single_link_list as SLL
from collections import deque

def length_list(S):
  h = 0
  head = S.head
  while head is not None:
    h += 1
    head = head.next
  return h

def length_list_h(head):
  h = 0
  while head is not None:
    h += 1
    head = head.next
  return h

def middle_node(S):
  prev = None
  slow = S.head
  fast = S.head
  while fast and fast.next:
    prev = slow
    slow = slow.next
    fast = fast.next.next
  return prev, slow

def is_palindrome(S):
  if S is None:
    return True
  stack = deque()
  tmp = S.head
  while tmp is not None:
    stack.append(tmp.data)
    tmp = tmp.next
  
  tmp = S.head
  while tmp is not None:
    ele = stack.pop()
    if ele != tmp.data:
      return False
    tmp = tmp.next
  return True

def rev_list(node):
  if node is None:
    return
  prev = None
  curr = node
  fast = node.next
  while curr is not None:
    # print(1, prev.data if prev else None)
    # print(2, curr.data if curr else None)
    # print(3, fast.data if fast else None)
    curr.next = prev
    prev = curr
    curr = fast
    fast = fast.next if fast else None
  return prev

def is_palindrom_opt1(S):
  if S is None:
    return True
  l = length_list(S)
  first_head = S.head
  prev_node, middle = middle_node(S)
  prev_node.next = None
  if l % 2 != 0:
    sec_head = middle.next
    middle_node.next = None
  else:
    sec_head = middle
  sec_head = rev_list(sec_head)
  h1 = first_head
  h2 = sec_head
  while h1 and h2:
    if h1.data != h2.data:
      return False
    h1 = h1.next
    h2 = h2.next
  if h1 is not None or h2 is not None:
    return False
  sec_head = rev_list(sec_head)
  if l % 2 != 0:
    prev_node.next = middle
    middle_node.next = sec_head
  else:
    prev_node.next = sec_head

  return True

class Result:
  def __init__(self, node, result):
    self.result = result
    self.node = node

def is_palindrome_rec(head):
  l = length_list_h(head)
  p = _is_palinfrom_rec(head, l)
  return p.result

def _is_palinfrom_rec(head, length):
  if head is None or length <= 0:
    return Result(head, True)
  elif length == 1:
    return Result(head.next, True)

  res = _is_palinfrom_rec(head.next, length - 2)
  if not res.result or res.node is None:
    return res
  
  res.result = (res.node.data == head.data)
  res.node = res.node.next
  return res
  

  
  


S = SLL.SingleLinkList()
S.appendRight(3)
S.appendRight(5)
S.appendRight(8)
S.appendRight(5)
S.appendRight(8)
S.appendRight(5)
S.appendRight(3)
print(is_palindrome_rec(S.head))
S.print_list()