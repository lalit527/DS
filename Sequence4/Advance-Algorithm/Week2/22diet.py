from sys import stdin
from bitarray import bitarray
EPS = 1e-6
PRECISION = 20
INF = float('-inf')


def ReadEquation():
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    # print(A, '--', b, '--', c)
    return (n, m, A, b, c)

def prepare(n, m, A, b):
  while n < m:
    A.append([0 for _ in range(m)])
    b.append(0)
    n += 1
  A.append([1 for _ in range(m)])
  b.append(INF)
  n += 1

  for k in range(m):
    tmp = [0.0 for _ in range(m)]
    tmp[k] = -1
    A.append(tmp)
    b.append(-0.0)
    n += 1
  return n

def get_subsets(set, m):
  n = pow(2, len(set))
  subsets = []
  bset = None
  count = 0
  for i in range(n):
    count += 1
    bset = "{0:b}".format(count).zfill(32)
    subset = []
    cnt = 0
    s_n = len(set)
    for j in range(s_n):
      if bset[32 - 1 - (s_n - 1 - j)] == '1':
        print('Fuck', bset[s_n - 1 - j])
        subset.append(set[j])
        cnt += 1
        if cnt > m:
          # print(i, j, cnt, m)
          break
    if cnt == m:
      subsets.append(subset[:])
  print(subsets)
  return subsets
      

def solve_all_equations(m, A, b):
  solutions = []
  nums = [i for i in range(len(A))]
  subsets = get_subsets(nums, m)


def solve_diet(n, m, A, b, c):
  n = prepare(n, m, A, b)
  solutions = solve_all_equations(m, A, b)
  pass

if __name__ == "__main__":
  n, m, A, b, c = ReadEquation()
  solve_diet(n, m, A, b, c)

