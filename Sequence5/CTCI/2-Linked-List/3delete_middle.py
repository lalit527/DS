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
   


S = singlell.SingleLinkList()
S.appendRight(1)
S.appendRight(2)
S.appendRight(3)
S.appendRight(4)
S.appendRight(5)
S.appendRight(6)
S.appendRight(7)
# S.appendRight(7)
delete_middle(S)
S.print_list()