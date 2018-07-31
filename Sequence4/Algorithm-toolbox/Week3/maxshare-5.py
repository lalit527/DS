# Uses python3
import sys
from random import randint

def optimal_summands(n):
    summands = []
    #write your code here
    for i in range(1, n + 1):
      if i == n:
        summands.append(i)
        n = 0
      else:
        if (2 * i) < n:
          summands.append(i)
          n -= i
    return summands

def optimal_summands_better(n):
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

def main():
  count = 0
  while True:
    n = randint(1, 100)
    result1 = optimal_summands(n)
    result2 = optimal_summands_better(n)
    print(n, len(result1), len(result2))
    if len(result1) != len(result2):
      print(n, len(result1), len(result2))
      break
    count += 1
    if count == 100:
      break


if __name__ == '__main__':
  main()
    # input = sys.stdin.read()
    # n = int(input)
    # summands = optimal_summands_better(n)
    # print(len(summands))
    # for x in summands:
    #     print(x, end=' ')
