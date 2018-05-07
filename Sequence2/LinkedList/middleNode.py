from singleLinkList import SingleLinkList

def middle(head):
  slowPtr = head
  fastPtr = head
  while fastPtr is not None and fastPtr.next is not None:
    fastPtr = fastPtr.next.next
    slowPtr = slowPtr.next
  return slowPtr

s = SingleLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  s.insert(i)
middleNode = middle(s.head)
print(middleNode.key)findNode.py
