from singleLinkList import SingleLinkList

def reverseList(head):
  tmp = head
  prev = None
  head = head.next
  while tmp is not None:
    tmp.next = prev
    prev = tmp
    tmp = head
    if head:
      head = head.next
  return prev

s = SingleLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  s.insert(i)
node = reverseList(s.head)
s.head = node
s.printData()
