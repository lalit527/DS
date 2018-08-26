import singlell

def remove_duplicate(S):
  tmp = S.head
  seen_nodes = set()
  prev = None
  while tmp is not None:
    if tmp.data in seen_nodes:
      if prev is not None:
        prev.next = tmp.next
      else:
        S.head = None      
      if tmp.next is None:
        S.tail = prev
    else:
      seen_nodes.add(tmp.data)
      prev = tmp
    tmp = tmp.next

def remove_dup_notmp(S):
  tmp = S.head
  prev = None
  while tmp is not None:
    cur = tmp
    while cur.next is not None:
      if tmp.data == cur.next.data:
        cur.next = cur.next.next
      else:
        cur = cur.next
    tmp = tmp.next


S = singlell.SingleLinkList()
S.appendLeft(1)
S.appendLeft(2)
S.appendLeft(2)
S.appendLeft(2)
S.appendLeft(2)
S.appendLeft(2)
S.appendLeft(2)
remove_dup_notmp(S)
S.print_list()