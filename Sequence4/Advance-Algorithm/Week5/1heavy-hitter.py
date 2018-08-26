# python3

import sys
import math
import numpy as np
import statistics as stats

class Hash:
  def __init__(self, a, b, p, m):
    self.a = a
    self.b = b
    self.p = p
    self.m = m

  def value(self, x):
    return int(((self.a * x + self.b) % self.p) % self.m)

class Sign:
  def __init__(self):
    self.h = Hash(np.random.uniform(10, 50), np.random.uniform(50, 100), 10e5 + 19, 1000)
  
  def value(self, x):
    return 1 if self.h.value(x) > 500 else -1


class Sketch:
  def __init__(self, n):
    self.b = int(math.log(n) * 1500)
    self.t = int(math.log(n) + 1)
    self.data = [[0] * self.b] * self.t
    self.ith_data = [0] * self.t
    self.funcs = [(Hash(np.random.uniform(50, 100), np.random.uniform(10, 50), 10e8 + 19, self.b), 
                   Sign()) for i in range(0, self.t)]
  
  def update(self, i, freq = 1):
    for j in range(self.t):
      self.data[j][self.funcs[j][0].value(i)] += self.funcs[j][1].value(i) * freq
  
  def estimate(self, i):
    for j in range(self.t):
      self.ith_data[j] = self.data[j][self.funcs[j][0].value(i)] * self.funcs[j][1].value(i)
    return stats.median(sorted(self.ith_data))


n = int(sys.stdin.readline().strip())
t = int(sys.stdin.readline().strip())

al = Sketch(n)

for _ in range(n):
    id, value = [int(i) for i in sys.stdin.readline().strip().split()]
    al.update(id, value)
    # assert(id not in D)
    # D[id] = value

for _ in range(n):
    id, value = [int(i) for i in sys.stdin.readline().strip().split()]
    al.update(id, value)


num_queries = int(sys.stdin.readline().strip())
queries = list(map(int, sys.stdin.readline().strip().split()))
assert(len(queries) == num_queries)

for query in queries:
    if al.estimate(query) >= t:
        print("1 ", end="")
    else:
        print("0 ", end="")
