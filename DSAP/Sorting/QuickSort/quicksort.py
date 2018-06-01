from linklist import SingleLinkList, Node
from queuelist import Queue, Node as QNode
from collections import deque

def quick_sort(S):
  n = S.length()
  if n < 2:
    return 
  p = S.peek()
  L = Queue()
  E = Queue()
  G = Queue()
  while not S.isEmpty():
    if S.peek() < p:
      L.enqueue(S.dequeue())
    elif p < S.peek():
      G.enqueue(S.dequeue())
    else:
      E.enqueue(S.dequeue())

  quick_sort(L)
  quick_sort(G)

  while not L.isEmpty():
    S.enqueue(L.dequeue())
  while not E.isEmpty():
    S.enqueue(E.dequeue())
  while not G.isEmpty():
    S.enqueue(G.dequeue())


def main():
  S = [12, 11, 13, 5, 6, 7]
  q = Queue()
  for i in S:
    q.enqueue(i)
  quick_sort(q)
  q.printQueue()


if __name__ == '__main__':
  main()