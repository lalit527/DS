#Uses python3
import sys
from math import sqrt

def closest_util(Px, Py, ln):
  if ln <= 3:
    return brute_force(Px, ln)
  
  mid = ln // 2
  Qx = Px[:mid]
  Rx = Px[mid:]

  mid_point = Px[mid][0]
  Qy = []
  Ry = []
  for x in Py:
    if x[0] <= mid_point:
      Qy.append(x)
    else:
      Ry.append(x)

  mid1 = closest_util(Qx, Qy, mid)
  mid2 = closest_util(Rx, Ry, ln - mid)

  d = min(mid1, mid2)
  strip = []
  for i in range(len(Py)):
    if abs(Py[i][0] - mid_point) < d:
      strip.append(Py[i])
  
  return min(d, strip_closest(strip, len(strip), d))


def brute_force(Px, ln):
  mi = float('inf')
  for i in range(ln):
    for j in range(i+1, ln):
      d = dist(Px[i], Px[j])
      if d < mi:
        mi = d
  return mi

def dist(p1, p2):
  return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def strip_closest(strip, size, delta):
  _min = delta
  for i in range(size):
    for j in range(i+1, min(i + 5, size)):
        dst = dist(strip[i], strip[j])
        if dst < _min:
          _min = dst
  return _min

def closest(P, n):
  Px = sorted(P, key= lambda d: d[0])
  Py = sorted(P, key= lambda d: d[1])
  mi = closest_util(Px, Py, n)
  return mi



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = []
    i = 1
    a = list(zip(data[1::2], data[2::2]))
    p = closest(a, n)
    print("{0:.9f}".format(p))