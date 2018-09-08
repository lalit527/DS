import sys
from math import sqrt

def distance(p1, p2):
  return sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

def brute_force(Px, n):
  _min = float('inf')
  for i in range(n):
    for j in range(i+1, n):
      dist = distance(Px[i], Px[j])
      if dist < _min:
        _min = dist
  return _min

def closest_util(Px, Py, n):
  if n <= 3:
    return brute_force(Px, n)

  mid = n // 2
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
  mid2 = closest_util(Rx, Ry, n - mid)
  
  d = min(mid1, mid2)
  strip = []
  for i in range(len(Py)):
    if abs(Py[i][0] - mid_point) < d:
      strip.append(Py[i])
  
  return min(d, strip_closest(strip, len(strip), d))

def strip_closest(strip, size, delta):
  _min = delta
  for i in range(size):
    for j in range(i + 1, min(i+5, size)):
      d = distance(strip[i], strip[j])
      if d < _min:
        _min = d
  return _min

def closest(a, n):
  Px = sorted(a, key = lambda x: x[0])
  Py = sorted(a, key = lambda y: y[1])
  mid = closest_util(Px, Py, n)
  return mid

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = []
    i = 1
    a = list(zip(data[1::2], data[2::2]))
    p = closest(a, n)
    print("{0:.9f}".format(p))