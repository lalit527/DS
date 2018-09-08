import sys
from collections import defaultdict

def fast_count_segments(starts, ends, points):
  cnt = [0] * len(points)
  data = starts + ends + points
  points_map = defaultdict(set)
  for i in range(len(points)):
    point, _ = points[i]
    points_map[point].add(i)
  data.sort(key = lambda d: (d[0], d[1]))
  coverage = 0
  for d in data:
    p, l = d
    if l == 'l':
      coverage += 1
    elif l == 'r':
      coverage -= 1
    elif l == 'p':
      index = points_map[p]
      for i in index:
        cnt[i] = coverage
  return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = [(i, 'l') for i in data[2:2 * n + 2:2]] #data[2:2 * n + 2:2]
    ends   = [(i, 'r') for i in data[3:2 * n + 2:2]] #data[3:2 * n + 2:2]
    points = [(i, 'p') for i in data[2 * n + 2:]] #data[2 * n + 2:]
    cnt = []
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
      print(x, end=' ')