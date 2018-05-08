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

def reverseN(head, n):
  if head is None:
    return head
  fast = head.next
  prev = None
  count = 0
  while count < n and head is not None:
    head.next = prev
    prev = head
    head = fast
    fast = fast.next if fast else None
    count += 1
  if head is not None:
    prev = prev.next
    prev.next = reverseN(prev, n)
  return prev

s = SingleLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  s.insert(i)
node = reverseN(s.head, 2)
s.head = node
s.printData()
