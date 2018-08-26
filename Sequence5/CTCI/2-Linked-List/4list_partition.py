import single_link_list as SLL

def partion_list(node, x):
  b_start = None
  b_end = None
  a_start = None
  a_end = None
  while node is not None:
    if node.data >= x:
      if a_start is None:
        a_start = node
        a_end = node
      else:
        a_end.next = node
        a_end = node
    else:
      if b_start is None:
        b_start = node
        b_end = node
      else:
        b_end.next = node
        b_end = node

    node = node.next

  if a_end is not None:
    a_end.next = None

  if b_end is not None:
    b_end.next = a_start

def partition_list_opti(node, x):
  head = node
  tail = node
  while node is not None:
    next = node.next
    if node.data < x:
      node.next = head
      head = node
    else:
      tail.next = node
      tail = node
    node = next
  tail.next = None

  return head


def partion_list_opt2(S, x):
    node = S.tail = S.head
    while node:
      next = node.next
      node.next = None
      if node.data < x:
          node.next = S.head
          S.head = node
      else:
          S.tail.next = node
          S.tail = node
      node = next
        
    # Error check in case all nodes are less than x
    if S.tail.next is not None:
        S.tail.next = None



       
      

   


S = SLL.SingleLinkList()
S.appendRight(3)
S.appendRight(5)
S.appendRight(8)
S.appendRight(5)
S.appendRight(10)
S.appendRight(2)
S.appendRight(1)
# S.head = partition_list_opti(S.head, 5)
partion_list_opt2(S, 5)
S.print_list()