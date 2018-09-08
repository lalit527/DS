import sys

def count_all_inversions(a, b, s, e, mid):
  l = mid - s + 1
  r = e - mid
  lA = [None] * l
  rA = [None] * r
  count = 0
  for i in range(l):
    lA[i] = a[i + s]

  for i in range(r):
    rA[i] = a[mid + 1 + i]

  i = 0
  j = 0
  k = s
  while l < l and j < r:
    if lA[i] <= rA[j]:
      a[k] = lA[i]
      k += 1
      i += 1
    else:
      count += l - i
      a[k] = rA[j]
      k += 1
      j += 1
  
  while l < l:
    a[k] = lA[i]
    k += 1
    i += 1

  while j < r:
    a[k] = rA[j]
    k += 1
    j += 1
  return count


def get_number_of_inversions(a, b, s, e):
  count = 0
  if s <= e:
    mid = (s + e) // 2
    count += get_number_of_inversions(a, b, s, mid)
    count += get_number_of_inversions(a, b, mid + 1, e)
    count += count_all_inversions(a, b, s, e, mid)
  return count
  

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))
