# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
  segments.sort(key = lambda x: x[1])
  points = []
  while len(segments) > 0:
    end_point = segments[0].end
    points.append(end_point)
    del segments[0]
    while len(segments):
      if segments[0].start <= end_point <= segments[0].end:
         del segments[0]
      else:
        break
  return points


  print(segments)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(points)
    # print(len(points))
    # for p in points:
    #   print(p, end=' ')