# Uses python3
import sys

def merge_all_inversions(a, b, left, mid, right):
  l = mid - left + 1
  r = right - mid
  l_a = [None] * l
  r_a = [None] * r
  count = 0
  for i in range(0, l):
    l_a[i] = a[i + left]

  for j in range(0, r):
    r_a[j] = a[mid + 1 + j]

  i = 0
  j = 0
  
  i = 0
  j = 0
  k = left
  while i < l and j < r:
    if l_a[i] <= r_a[j]:
      a[k] = l_a[i]
      i += 1
      k += 1
    elif l_a[i] > r_a[j]:
      count += l - i
      a[k] = r_a[j]
      k += 1
      j += 1

  while i < l:
    a[k] = l_a[i]
    i += 1
    k += 1

  while j < r:
    a[k] = r_a[j]
    j += 1
    k += 1
  return count
      

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left < 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave + 1, right)
    #write your code here

    number_of_inversions += merge_all_inversions(a, b, left, ave, right)

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))
