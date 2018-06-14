#Uses python3
import sys
import math

def closest_util(Px, Py):
  ln = len(Px)
  if ln <= 3:
    return brute_force(Px)
  
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

  (p1, q1, mid1) = closest_util(Qx, Qy)
  (p2, q2, mid2) = closest_util(Rx, Ry)

  if mid1 <= mid2:
    d = mid1
    _min = (p1, q1)
  else:
    d = mid2
    _min = (p2, q2)
  
  (p3, q3, mid3) = strip_closest(Px, Py, d, _min)

  if d <= mid3:
    return _min[0], _min[1], d
  else:
    return p3, q3, mid3

def brute_force(Px):
  mi = dist(Px[0], Px[1])
  p1 = Px[0]
  p2 = Px[1]
  ln = len(Px)
  if ln == 2:
    return p1, p2, mi
  for i in range(ln - 1):
    for j in range(i+1, ln):
      if i != 0 and j != 1:
        d = dist(Px[i], Px[j])
        if d < mi:
          mi = d
          p1, p2 = Px[i], Px[j]
  return p1, p2, mi

def dist(p1, p2):
  return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def strip_closest(Px, Py, delta, best_pair):
  ln = len(Px)
  mx_x = Px[ln // 2][0]
  s_y = [x for x in Py if mx_x - delta <= x[0] <= mx_x + delta]
  best = delta 
  ly = len(s_y)
  for i in range(ly - 1):
    for j in range(i+1, min(i + 7, ly)):
      p, q = s_y[i], s_y[j]
      dst = dist(p, q)
      if dst < best:
        best_pair = p, q
        best = dst
  return best_pair[0], best_pair[1], best

def closest(P, n):
  Px = sorted(P, key= lambda d: d[0])
  Py = sorted(P, key= lambda d: d[1])
  p1, p2, mi = closest_util(Px, Py)
  return mi



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    z = list(zip(x, y))
    print("{0:.9f}".format(closest(z, n)))