import single_link_list as SLL

class PartialSum:
  def __init__(self):
    self.sum = None
    self.carry = 0
  

def length_list(S):
  h = 0
  head = S.head
  while head is not None:
    h += 1
    head = head.next
  return h

def add_list(S1, S2):
  if S1 is None:
    return S2
  if S2 is None:
    return S1
  if S1 is None and S2 is None:
    return None
  S = SLL.SingleLinkList()
  carry = 0
  head1, head2 = S1.head, S2.head
  while head1 or head2:
    result = carry
    if head1:
      result += head1.data
    if head2:
      result += head2.data
    
    S.appendRight(result % 10)
    carry = result // 10
    head1 = head1.next
    head2 = head2.next
  if carry:
    S.appendRight(carry)
  return S

def add_list_rev(S1, S2):
  h1 = length_list(S1)
  h2 = length_list(S2)
  if h1 > h2:
    m = h1 - h2
    while m > 0:
      h2.appendLeft(0)
      m -= 1
  elif h2 > h1:
    m = h2 - h1
    while m > 0:
      h1.appendLeft(0)
      m -= 1
  n1 = S1.head
  n2 = S2.head
  sum = _add_list_rev(n1, n2)
  tmp = sum.sum
  while tmp is not None:
    print(tmp.data)
    tmp = tmp.next

  if sum.carry == 0:
    return sum.sum
  else:
    result = insert_before(sum.sum, sum.carry)
    return result
  

def insert_before(list, data):
  node = SLL.SingleLinkList.Node(data)
  if list is not None:
    node.next = list
  return node

def _add_list_rev(n1, n2):
  if n1 is None and n2 is None:
    sum = PartialSum()
    return sum
  sum = _add_list_rev(n1.next, n2.next)
  val = sum.carry + n1.data + n1.data
  full_result = insert_before(sum.sum, val % 10)
  sum.sum = full_result
  sum.carry = val // 10
  return sum

def sum_lists_followup(ll_a, ll_b):
    # Pad the shorter list with zeros
    if length_list(ll_a) < length_list(ll_b):
        for i in range(length_list(ll_b) - length_list(ll_a)):
            ll_a.add_to_beginning(0)
    else:
        for i in range(length_list(ll_a) - length_list(ll_b)):
            ll_b.add_to_beginning(0)

    # Find sum
    n1, n2 = ll_a.head, ll_b.head
    result = 0
    while n1 and n2:
        result = (result * 10) + n1.data + n2.data
        n1 = n1.next
        n2 = n2.next

    # Create new linked list
    ll = SLL.SingleLinkList()
    for i in str(result):
      ll.appendRight(i)

    return ll


S1 = SLL.SingleLinkList()
S1.appendRight(7)
S1.appendRight(1)
S1.appendRight(6)
S2 = SLL.SingleLinkList()
S2.appendRight(5)
S2.appendRight(9)
S2.appendRight(2)
# S = add_list(S1, S2)
# S.print_list()
S1 = SLL.SingleLinkList()
S1.appendRight(6)
S1.appendRight(1)
S1.appendRight(7)
S2 = SLL.SingleLinkList()
S2.appendRight(5)
S2.appendRight(9)
S2.appendRight(2)
S = add_list_rev(S1, S2)
# S.print_list()
head = S
while head is not None:
  print(head.data)
  head = head.next