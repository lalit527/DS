from sys import stdin
from bitarray import bitarray
from functools import reduce
import sys

EPS = 1e-3
INF = 1.0e+9

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

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    
    _max = 0.0
    size = len(a)
    for i in range(pivot_element.row, size):
      if abs(_max) - abs(a[i][pivot_element.column]) < EPS:
        _max = abs(a[i][pivot_element.column])
        pivot_element.row = i
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column

def scale_pivot(a, b, pivot_element):
  size = len(a)
  divisor = a[pivot_element.row][pivot_element.column]
  for j in range(pivot_element.column, size):
    a[pivot_element.row][j] /= divisor
  
  b[pivot_element.row] /= divisor


def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    size = len(a)
    multiple = 0.0
    scale_pivot(a, b, pivot_element)
    print('SP', b, 'PE', pivot_element.row, pivot_element.column)
    for i in range(pivot_element.row + 1, size):
      multiple = a[i][pivot_element.column]
      for j in range(pivot_element.column, size):
        a[i][j] -= (a[pivot_element.row][j] * multiple)
      print('Check1', multiple, b[i], pivot_element.row, pivot_element.column, b[pivot_element.row], multiple) 
      b[i] -= (b[pivot_element.row] * multiple)
    print('SPE', b)
    


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    print('SE', equation.a, equation.b)
    a = equation.a
    b = equation.b
    size = len(a)
    if size <= 0:
      return {}

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if a[pivot_element.row][pivot_element.column] == 0:
          break
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    code = back_substitution(a, b)
    
    return (code, b)

def back_substitution(a, b):
  size = len(a)
  # print('BEGIN', a, b)
  for i in range(size - 1, -1, -1):
    v = b[i]
    for j in range(0, i):
      # print('bj', b[j], 'a', a[j][i], 'v', v)
      b[j] -= a[j][i] * v
      a[j][i] = 0
  # print('END', a, b)
  return 0


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
        subset.append(set[j])
        cnt += 1
        if cnt > m:
          # print(i, j, cnt, m)
          break
    if cnt == m:
      subsets.append(subset)
  return subsets
      

def solve_all_equations(m, A, b):
  solutions = []
  nums = [i for i in range(len(A))]
  subsets = get_subsets(nums, m)
  if len(A) == 1:
    subsets.append[0]
  
  for sub in subsets:
    mat = []
    col = []
    for i in sub:
      mat.append(A[i])
      col.append(b[i])
    eq = Equation(mat, col)
    code_sol = SolveEquation(eq)
    # print('code_sol', code_sol)
    if code_sol[0] == 0 and len(code_sol[1]) > 0:
      solutions.append(code_sol[1])    
  return solutions

def solve_diet(n, m, A, b, c):
  n = prepare(n, m, A, b)
  solutions = solve_all_equations(m, A, b)
  print(solutions)
  if len(solutions) == 0:
    print("1")
    return (-1, {})
  
  sol_index = -1
  largest_pleasure = float('-inf')

  for i in range(len(solutions)):
    # print('i', solutions[i])
    sol = solutions[i]
    satisfied = True
    for j in range(n):
      constraint = b[j]
      sum = 0.0

      for k in range(m):
        sum += A[j][k] * sol[k]
      print('SC', sum, constraint)
      if sum - constraint > EPS:
        satisfied = False
        break
    pleasure = 0.0
    for k in range(m):
      # print('k', sol[k], c[k])
      pleasure += sol[k] * c[k]
    print('F', pleasure, largest_pleasure)
    if satisfied and pleasure > largest_pleasure:
      largest_pleasure = pleasure
      sol_index = i
    
  if sol_index == -1:
    print("2")
    return (-1, {})
  
  

  sol = solutions[sol_index]
  print(reduce((lambda x, y: x + y), sol))
  if reduce((lambda x, y: x + y), sol) + EPS >= INF:
    print("fuck")
  print(sol, 'ok')


if __name__ == "__main__":
  n, m, A, b, c = ReadEquation()
  sol = solve_diet(n, m, A, b, c)
  print(sol)

