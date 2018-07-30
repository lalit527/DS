# Uses python3
import sys
from random import randint
from collections import defaultdict

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    data = starts + ends + points
    points_map = defaultdict(set)
    for i in range(len(points)):
      point, _ = points[i]
      data.append((point, 'p'))
      points_map[point].add(i)
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
    starts = [(i, 'l') for i in data[2:2 * n + 2:2]] #data[2:2 * n + 2:2]
    ends   = [(i, 'r') for i in data[3:2 * n + 2:2]] #data[3:2 * n + 2:2]
    points = [(i, 'p') for i in data[2 * n + 2:]] #data[2 * n + 2:]
    cnt = []
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
      print(x, end=' ')
