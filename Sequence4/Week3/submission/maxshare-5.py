# Uses python3
import sys

def optimal_summands(n):
  summands = []
  #write your code here
  sum = 0
  i = 1
  while True:
    if (n - sum - i) > i:
      summands.append(i)
      sum += i
      i += 1
    else:
      summands.append(n - sum)
      break

  return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
