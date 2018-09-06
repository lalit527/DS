import sys

def binary_search(a, x):
  return _binary_search(a, 0, len(a) - 1, x)

def _binary_search(a, s, e, x):
  if e >= s:
    mid = (s + e) // 2
    if x < a[mid]:
     return _binary_search(a, s, mid-1, x)
    elif a[mid] < x:
     return _binary_search(a, mid+1, e, x)
    else:
      return True
  else: 
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
