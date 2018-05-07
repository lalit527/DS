from singleLinkList import SingleLinkList

def length(head):
  count = 0
  tmp = head
  while tmp is not None:
    tmp = tmp.next
    count += 1
  return count

def mergeList(head1, head2):
  result = SingleLinkList()
  return _mergeList(head1, head2, result)

def _mergeList(head1, head2, result):
  if head1 is None:
    result.insert(head2.key)
    return
  if head2 is None:
    result.insert(head1.key)
    return
  if head1.key < head2.key:
    result.insert(head1.key)
    result.next = _mergeList(head1.next, head2, result)
  else:
    result.insert(head2.key)
    result.next = _mergeList(head1, head2.next, result)
  return result

def mergeInPlace(head1, head2):
  result = None
  if head1 is None:
    return head2
  if head2 is None:
    return head1
  if head1.key < head2.key:
    result = head1
    result.next = mergeInPlace(head1.next, head2)
  else:
    result = head2
    result.next = mergeInPlace(head1, head2.next)
  return result
  
ol = SingleLinkList()
el = SingleLinkList()
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
for i in odd:
  ol.insert(i)
for i in even:
  el.insert(i)
# node = mergeList(ol.head, el.head)
# node.printData()
node = mergeInPlace(ol.head, el.head)
ol.printData()
