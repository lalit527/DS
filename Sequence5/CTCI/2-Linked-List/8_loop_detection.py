import single_link_list as SLL
from collections import deque

def length_list(head):
  h = 0
  prev = None
  while head is not None:
    h += 1
    prev = head
    head = head.next
  return h, prev

def check_loop(S):
  if S is None:
    return None, None
  slow = S.head
  fast = S.head
  while slow is not None and fast is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      break

  if fast == None or fast.next == None:
    return None, None
  
  slow = S.head
  prev = None
  while slow != fast:
    prev = fast
    slow = slow.next
    fast = fast.next
  return prev, fast




  


S = SLL.SingleLinkList()
n1 = S.append(S.head, 3)
n2 = S.append(n1, 1)
n3 = S.append(n2, 5)
n4 = S.append(n3, 9)
n5 = S.append(n4, 7)
n6 = S.append(n5, 2)
n7 = S.append(n6, 1)
h1 = S.append(n7, 4)
h2 = S.append(h1, 6)
S.make_intersect(h2, n5)
loop_bgn, loop_end = check_loop(S)
print(loop_bgn.data, loop_end.data)