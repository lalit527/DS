# Uses python3
import sys

def get_change(m):
  values = [10, 5, 1]
  changes = []
  for i in values:
    while m >= i:
      m -= i
      changes.append(i)

  return len(changes)

if __name__ == '__main__':
  m = int(sys.stdin.read())
  print(get_change(m))
