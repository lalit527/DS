from singleLinkList import SingleLinkList

def length(head):
  count = 0
  tmp = head
  while tmp is not None:
    tmp = tmp.next
    count += 1
  return count

def createCycle(head, n):
  l = length(head)
  if n > l:
    return None
  last = head
  node = head
  count = 1
  while last.next is not None:
    last = last.next
  while count <= n:
    node = node.next
    count += 1
  last.next = node


def checkCycle(head):
  slowPtr = head
  fastPtr = head.next
  while fastPtr is not None:
    if fastPtr == slowPtr:
      print(countLoop(slowPtr))
      return True
    fastPtr = fastPtr.next.next
    slowPtr = slowPtr.next
  return False

def countLoop(head):
  tmp = head.next
  count = 1
  while tmp.next != head:
    tmp = tmp.next
    count += 1
  count += 1
  removeLoop(tmp)
  return count

def removeLoop(head):
  if head:
    head.next = None

s = SingleLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  s.insert(i)

createCycle(s.head, 2)
node = checkCycle(s.head)
print(node)
s.printData()