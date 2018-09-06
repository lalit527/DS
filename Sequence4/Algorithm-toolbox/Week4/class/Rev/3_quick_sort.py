# Uses python3
import sys
import random

def partition_3way(a, s, e):
  pivot = a[s]
  i = s
  lt = s
  gt = e
  while i <= gt:
    if a[i] < pivot:
      a[lt], a[i] = a[i], a[lt]
      lt += 1
      i += 1
    elif a[i] > pivot:
      a[gt], a[i] = a[i], a[gt]
      gt -= 1
    else:
      i += 1

  return lt, gt

def partition_2way(a, s, e):
  pivot = a[s]
  j = s
  for i in range(s+1, e + 1):
    if a[i] <= pivot:
      j += 1
      a[i], a[j] = a[j], a[i]
    a[s], a[j] = a[j], a[s]
  return j

def partition(a, s, e):
  i = s
  j = e - 1
  pivot = a[e]
  while True:
    while i <= e and a[i] <= pivot:
      i += 1
    while j >= 0 and a[j] >= pivot:
      j -= 1
    if i < j:
      a[i], a[j] = a[j], a[i]
    else:
      print(j)
      return j
    



# def randomized_quick_sort(a, s, e):
#   if s <= e:
#     k = random.randint(s, e)
#     a[e], a[k] = a[k], a[e]
#     lt, gt = partition_3way(a, s, e)
#     randomized_quick_sort(a, s, lt - 1)
#     randomized_quick_sort(a, gt + 1, e)

def randomized_quick_sort(a, s, e):
  if s <= e:
    k = random.randint(s, e)
    a[e], a[k] = a[k], a[e]
    lt = partition(a, s, e)
    randomized_quick_sort(a, s, lt - 1)
    randomized_quick_sort(a, lt + 1, e)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
