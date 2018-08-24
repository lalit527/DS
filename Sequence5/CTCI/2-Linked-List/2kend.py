import singlell

def get_kth_from_end(S, k):
  n = k
  tmp = S.head
  while n > 0:
    # print(n)
    tmp = tmp.next
    n -= 1
  # print(tmp.data)
  cur = S.head
  while tmp is not None:
    print(tmp.data, cur.data)
    tmp = tmp.next
    cur = cur.next
  print(cur.data)

S = singlell.SingleLinkList()
S.appendRight(1)
S.appendRight(2)
S.appendRight(3)
S.appendRight(4)
S.appendRight(5)
S.appendRight(6)
S.appendRight(7)
get_kth_from_end(S, 3)
# S.print_list()