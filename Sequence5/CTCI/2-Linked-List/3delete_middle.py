import singlell

def get_middle(S):
  slow = S.head
  fast = S.head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
  return slow

def delete_middle(S):
  middle = get_middle(S)
  tmp = S.head
  prev = None
  while tmp != middle:
    prev = tmp
    tmp = tmp.next
  prev.next = tmp.next

def delete_middle_nohead(node):
  tmp = node
  while tmp.next is not None:
    tmp.data  = tmp.next.data
    tmp = tmp.next
  tmp.next = None

S = singlell.SingleLinkList()
S.appendRight(1)
S.appendRight(2)
S.appendRight(3)
S.appendRight(4)
S.appendRight(5)
S.appendRight(6)
S.appendRight(7)
# S.appendRight(7)
# delete_middle(S)
middle = get_middle(S)
delete_middle_nohead(middle)
S.print_list()