#Uses python3
import sys
import math

def dist(p1, p2):
  return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))

def brute_force(P, n):
  _min = float('inf')
  for i in range(n):
    for j in range(i+1, n):
      
      distance = dist(P[i], P[j])
      print(P[i], P[j], distance)
      if distance < _min:
        _min = distance
  return _min


def strip_closest(strip, size, d):
  _min = d

  for i in range(size):
    for j in range(i + 1, size):
      if strip[j].y - strip[i].y <  min:
        if dist(strip[i], strip[j]) < min:
          min = dist(strip[i], strip[j])

  return min

def closest_util(Px, Py, n):
  if n <= 3:
    return brute_force(Px, n)
  
  mid = n // 2
  mid_point = Px[mid]

  Pyl = [None] * (mid)  
  Pyr = [None] * (n-mid)
  li = 0
  ri = 0
  print(Pyl, Pyr)
  for i in range(n):
    print(li, i)
    if Py[i][0] <= mid_point[0]:
      Pyl[li] = Py[i]
      li += 1
    else:
      Pyr[ri] = Py[i]
      ri += 1

  dl = closest_util(Px, Pyl, mid)
  dr = closest_util(Px + mid, Pyr, n - mid)

  d = min(dl, dr)

  strip = [None] * n
  j = 0
  for i in range(n):
    if abs(Py[i][0] - mid_point[0]) < d:
      strip[j] = P[j]
      j += 1

  return min(d, strip_closest(strip, j, d))

def closest(P, n):
  Px = sorted(P, key= lambda d: d[0])
  Py = sorted(P, key= lambda d: d[1])
  return closest_util(Px, Py, n)

def minimum_distance(x, y):
    #write your code here
    print(x , y)
    return 10 ** 18

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    z = list(zip(x, y))
    print("{0:.9f}".format(closest(z, n)))
