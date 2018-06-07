# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def get_min_right_point(segments):
  min_right_index = 0
  n = len(segments)
  for s in range(1, n):
    if segments[s].end < segments[min_right_index].end:
      min_right_index = s
  return min_right_index


def check_point_included(segment, value):
  if segment.start <= value <= segment.end:
    return True
  return False

def optimal_points(segments):
    points = []
    while len(segments) > 0:
      min_right = get_min_right_point(segments)
      end_point = segments[min_right].end
      points.append(end_point)
      del segments[min_right]
      i = 0
      while i < len(segments):
        if check_point_included(segments[i], end_point):
          del segments[i]
        else:
          i += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
      print(p, end=' ')
