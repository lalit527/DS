# Uses python3
import sys
from random import randint
from collections import defaultdict

def partition(data, left, right):
  pivot, _ = data[left]
  i = left
  lt = left
  gt = right
  while i <= gt:
    d, _ = data[i]
    # print(d, pivot)
    if d < pivot:
      data[lt], data[i] = data[i], data[lt]
      i += 1
      lt += 1
    elif d > pivot:
      data[i], data[gt] = data[gt], data[i]
      gt -= 1
    else:
      i += 1
  return lt, gt

def quick_sort(data, s, e):
  if e > s:
    k = randint(s, e)
    data[s], data[k] = data[k], data[s]

    lo, hi = partition(data, s, e)
    quick_sort(data, s, lo - 1)
    quick_sort(data, hi + 1, e)



def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    data = []
    points_map = defaultdict(set)
    for start in starts:
      data.append((start, 'l'))
    for end in ends:
      data.append((end, 'r'))
    for i in range(len(points)):
      point = points[i]
      data.append((point, 'p'))
      points_map[point].add(i)
    # print(data)
    # quick_sort(data, 0, len(data) - 1)
    data = sorted(data, key = lambda d: (d[0], d[1]))
    coverage = 0
    for d in data:
      x, l = d
      if l == 'l':
        coverage += 1
      elif l == 'r':
        coverage -= 1
      elif l == 'p':
        index = points_map[x]
        for i in index:
          cnt[i] = coverage    

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
      print(x, end=' ')
