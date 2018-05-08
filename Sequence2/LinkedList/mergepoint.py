from singleLinkList import SingleLinkList

def length(head):
  count = 0
  tmp = head
  while tmp is not None:
    tmp = tmp.next
    count += 1
  return count

def mergeCommonList(head1, head2):
  p = head1
  q = head2
  l1 = length(head1)
  l2 = length(head2)
  n = 0
  if l1 > l2:
    dif = l1 - l2
    while n < dif:
      p = p.next
      n += 1
  else:
    dif = l2 - l1
    while n < dif:
      q = q.next
      n += 1
  while p.next is not None and q.next is not None:
    if p.next.key == q.next.key:
      return True
    p = p.next
    q = q.next
  return False
  
l1 = SingleLinkList()
l2 = SingleLinkList()
arr1 = [1, 5, 7, 9, 10, 12]
arr2 = [2, 4, 15, 17, 5, 7, 9, 10, 12]
for i in arr1:
  l1.insert(i)
for i in arr2:
  l2.insert(i)
result = mergeCommonList(l1.head, l2.head)
print(result)
