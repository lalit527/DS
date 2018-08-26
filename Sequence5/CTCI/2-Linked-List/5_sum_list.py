import single_link_list as SLL

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


S1 = SLL.SingleLinkList()
S1.appendRight(7)
S1.appendRight(1)
S1.appendRight(6)
S2 = SLL.SingleLinkList()
S2.appendRight(5)
S2.appendRight(9)
S2.appendRight(2)
S = add_list(S1, S2)
S.print_list()