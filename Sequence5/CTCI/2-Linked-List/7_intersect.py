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

def check_intersection(list1, list2):
  if list1 is None and list2 is None:
    return True
  if list1 is None or list2 is None:
    return False
  n, prev1 = length_list(list1)
  m, prev2 = length_list(list2)
  if prev1 != prev2:
    return False
  
  if n > m:
    w = n - m
    while w > 0:
      list1 = list1.next
      w -= 1
  elif m > n:
    w = m - n
    while w > 0:
      list2 = list2.next
  print(list1.data, list2.data)
  
  while list1 != list2:
    print(list1.data, list2.data)
    list1 = list1.next
    list2 = list2.next

  return True
  


S = SLL.SingleLinkList()
n1 = S.append(S.head, 3)
n2 = S.append(n1, 1)
n3 = S.append(n2, 5)
n4 = S.append(n3, 9)
n5 = S.append(n4, 7)
n6 = S.append(n5, 2)
n7 = S.append(n6, 1)
S1 = SLL.SingleLinkList()
h1 = S1.append(S1.head, 4)
h2 = S1.append(h1, 6)
S1.make_intersect(h2, n5)
print(check_intersection(S.head, S1.head))