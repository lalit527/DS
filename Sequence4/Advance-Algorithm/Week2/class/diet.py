# python3
from sys import stdin
import copy
import numpy as np

VeryBigNumber = 1e9

class Equation:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
class Position:
  def __init__(self, column, row):
    self.column = column
    self.row = row

def ReadEquation():
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    # print(A, '--', b, '--', c)
    return (n, m, A, b, c)

def prime_element(a, used_rows, used_columns):
  m = len(a)
  pivot_element = Position(0, 0)
  while used_rows[pivot_element.row]:
    pivot_element.row += 1
  while used_columns[pivot_element.column]:
    pivot_element.column += 1
  while a[pivot_element.row][pivot_element.column] == 0 or used_rows[pivot_element.row]:
    pivot_element.row += 1
    if pivot_element.row > m - 1:
      return False, None
  return True, pivot_element

def process_pivot_element(a, b, pivot_element):
  n = len(a)
  m = len(a[pivot_element.row])
  scale = a[pivot_element.row][pivot_element.column]
  for j in range(m):
    a[pivot_element.row][j] /= scale
  b[pivot_element.row] /= scale
  for i in range(n):
    if i != pivot_element.row:
      scale = a[i][pivot_element.column]
      for j in range(pivot_element.column, n):
        a[i][j] -= a[pivot_element.row][j] * scale
      b[i] -= b[pivot_element.row] * scale

def swap_lines(a, b, used_rows, pivot_element):
  a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
  b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
  used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
  pivot_element.row = pivot_element.column

def mark_pivot_element_used(pivot_element, used_rows, used_columns):
  used_rows[pivot_element.row] = True
  used_columns[pivot_element.column] = True

def solve_equation(equation):
  a = equation.a
  b = equation.b
  size = len(a)
  used_columns = [False] * size
  used_rows = [False] * size
  for step in range(size):
    solved, pivot_element = prime_element(a, used_rows, used_columns)
    if not solved:
      return False, None
    swap_lines(a, b, used_rows, pivot_element)
    process_pivot_element(a, b, pivot_element)
    mark_pivot_element_used(pivot_element, used_rows, used_columns)
  return True, b

def add_equations(n, m, A, b):
  for i in range(m):
    e = [0.0] * m
    e[i] = -1.0
    A.append(e)
    b.append(0.0)
  A.append([1.0] * m)
  b.append(VeryBigNumber)


def solve_diet_problem(n, m, A, b, c):
  add_equations(n, m, A, b)
  l = n + m + 1
  ans = -1
  best_score = float('-inf')
  best_result = None
  for x in range(2 ** l):
    used_index = [i for i in rnge(l) if ((x / 2 ** i) % 2) // 1 == 1]
    if len(used_index) != m:
      continue
    last_equation = False
    if used_index[-1] == l - 1:
      last_equation = True
    _A = [A[i] for i in used_index]
    _b = [b[i] for i in used_index]
    solved, result = solve_equation(copy.deepcopy(Equation(_A, _b)))
    if solved:
      isAccepted, ans, bestScore = checkResult(n, mm, A, b, c, result, lastEquation, ans, bestScore)
      if isAccepted:
        bestResult = result
    return [ans, bestResult]

def _solve_diet_problem(n, m, A, b, c):
  res = linprog(-np.array(c), A, b)
  pass

if __name__ == "__main__":
  n, m, A, b, c = ReadEquation()
  t, x = solve_diet_problem(n, m, A, b, c)
  print(t, x)