# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def optimal_sequence_memo(n):
  sequence = []
  T = [0] * (n + 1)
  T[0] = 0
  for i in range(1, n + 1):
    T[i] = T[i - 1] + 1
    if i % 2 == 0:
      T[i] = min(1 + T[i//2], T[i])
    if i % 3 == 0:
      T[i] = min(1 + T[i // 3], T[i])
  sequence.append(n)
  while n > 1:
    if T[n - 1] == T[n]-1:
      n = n - 1
    elif (n % 2 == 0 and (T[n//2] == T[n] - 1)):
      n = n // 2
    elif (n % 3 == 0 and (T[n//3] == T[n] - 1)): 
      n = n // 3
    sequence.append(n)
  return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_memo(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
