import sys

def optimal_sequence(n):
  sequence = []
  while n > 0:
    sequence.append(n)
    if n % 3 == 0:
      n = n // 3
    elif n % 2 == 0:
      n = n // 2
    else:
      n = n - 1
  print(sequence)
  return sequence

def optimal_sequence_memo(n):
  sequence = []
  memo = [0] * (n + 1)
  for i in range(1, n+1):
    memo[i] = memo[i - 1] + 1
    if i % 2 == 0:
      memo[i] = min(memo[i], 1 + memo[i // 2])
    elif i % 3 == 0:
      memo[i] = min(memo[i], 1 + memo[i // 3])
  print(memo)
  sequence.append(n)
  while n > 1:
    print(n)
    if memo[n - 1] == memo[n] - 1:
      n = n - 1
    elif (n % 2 == 0 and memo[n // 2] == memo[n] - 1):
      n = n // 2
    elif (n % 3 == 0 and memo[n // 3] == memo[n] - 1):
      n = n // 3
    sequence.append(n)
  print(sequence)
  return(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_memo(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')