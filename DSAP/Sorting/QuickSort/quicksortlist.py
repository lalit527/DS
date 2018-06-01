from linklist import SingleLinkList

def length(head):
  if head is None:
    return head
  tmp = head
  while tmp.next is not None:
    tmp = tmp.next
  print(tmp)
  return tmp

def quicksort(head):
  n = length(head)
  print(n)
  _quicksort(head, n)

def _quicksort(head, tail):
  print(head.key, tail.key)



s = SingleLinkList()
arr = [12, 11, 13, 5, 6, 7]
for i in arr:
  s.insert(i)
quicksort(s.head)
# s.printData()