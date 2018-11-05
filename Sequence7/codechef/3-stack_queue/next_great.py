import sys
from collections import deque

def next_greater(n, W):
  S = deque()
  n = len(W) - 1
  S.append(n)
  n -= 1
  while n >= 0:
    top = S[-1]
    if W[top] > W[n]:
      break
    else:
      S.append(n)
    n -= 1

  if n <= 0:
    return -1

  i = len(S)
  print(S, i, n)
  while i > 0:
    front = S.popleft()
    print(front)
    if W[front] > W[n]:
      W[front], W[n] = W[n], W[front]
      S.append(front)
      break
    else:
      S.append(front)
    i -= 1
  print(W)
  print(S)
  # top = S.pop()
  # W[top], W[n] = W[n], W[top]
  if len(S) > 0:
    peek = S[0]
    while len(S) > 1:
      front = S.popleft()
      rear = S.pop()
      W[rear], W[front] = W[front], W[rear]
  return ''.join(map(lambda x: str(x), W))
  

def main():
  num_cases = int(sys.stdin.readline().strip())
  for _ in range(num_cases):
    n = sys.stdin.readline().strip()
    W = list(map(int, sys.stdin.readline().strip().split(' ')))
    print(next_greater(n, W))

if __name__ == "__main__":
  main()