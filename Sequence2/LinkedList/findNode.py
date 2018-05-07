from singleLinkList import SingleLinkList

def length(head):
  count = 0
  tmp = head
  while tmp is not None:
    tmp = tmp.next
    count += 1
  return count

def findN(head, n):
  if n > length(head):
    return 
  slowPtr = head
  fastPtr = head
  while n >= 0:
    n -= 1
    fastPtr = fastPtr.next

  while fastPtr is not None:
    fastPtr = fastPtr.next
    slowPtr = slowPtr.next
  return slowPtr

s = SingleLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  s.insert(i)
node = findN(s.head, 6)
print(node.key if node else None)
