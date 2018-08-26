from sys import stdin
from itertools import chain, combinations
import math

max_value = float('-inf')
result = None
INF = math.pow(10, 9)
bounded = True


class GaussianElimination:
  def __init__(self, A, b):
    self.A = A
    self.b = b
    self.has_solution = True
    self.calculate()
  
  def calculate(self):
    if self.A is None or self.b is None:
      self.has_solution = False
      return
    if len(self.A) == 0 or len(self.b) == 0:
      self.has_solution = False
      return
    self.copy_matrix(self.A)
    self.copy_vec(self.b)
    self.row_reduce()

  def row_reduce(self):
    row_len = len(self.A)
    for row in range(row_len):
      row_pivot = self.get_row_pivot(A, row)
      if row_pivot == -1:
        self.has_solution = False
        return
      if row_pivot != row:
        self.swap_row_mat(row, row_pivot)
        self.swap_index_vec(row, row_pivot)
      
      if self.A[row][row] != 1:
        self.rescale_pivot(row)
      
      for r in range(row_len):
        if row == r:
          continue
        self.make_col_zero(row, r)

  def make_col_zero(self, cur_row, row):
    scale_factor = self.A[row][cur_row]
    for col in range(len(self.A[0])):
      print(1, col, self.A[cur_row][col])
      print(2, col, self.A[row][col])
      self.A[row][col] = self.A[row][col] - scale_factor * self.A[cur_row][col]
    self.b[row] = self.b[row] - scale_factor * self.b[cur_row]

  def rescale_pivot(self, row):
    scale_factor = float(self.A[row][row])
    for col in range(len(self.A[0])):
      self.A[row][col] = self.A[row][col] / scale_factor
    self.b[row] = self.b[row] /scale_factor 
  
  def swap_row_mat(self, i, j):
    self.A[i], self.A[j] = self.A[j], self.A[i]

  def swap_index_vec(self, i, j):
    self.b[i], self.b[j] = self.b[j], self.b[i]
  
  def get_row_pivot(self, matrix, row):
    for r in range(row, len(matrix)):
      if matrix[r][row] != 0:
        return r
    return -1

  def copy_matrix(self, matrix):
    n = len(matrix)
    m = len(matrix[0])
    A = [[0.0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
      for j in range(m):
        self.A[i][j] = matrix[i][j]

  def copy_vec(self, vec):
    n = len(vec)
    b = [0.0] * n
    for i in range(n):
      b[i] = vec[i]

class LinearEquation:
  def __init__(self, A, b, c):
    self.n = len(A)
    self.m = len(c)
    self.A = A
    self.b = b
    self.c = c
    total = self.n + self.m + 1
    self.compute(total)

  def print_res(self):
    if max_value == float('-inf'):
      print("No Solution")
      return
    if not bounded:
      print("Infinity")
      return
    print("Bounded solution")
    for i in range(len(result)):
      print("%.18f", result[i] + " ")
  
  def compute(self, total):
    arr = [i for i in range(total)]
    self.gen_process_combinations(arr, total, self.m)

  def gen_process_combinations(self, arr, n, r):
    data = [0] * r
    self.combination_util(arr, n, r, 0, data, 0)
  
  def combination_util(self, arr, n, r, index, data, i):
    if index == r:
      _set = set()
      for j in range(r):
        _set.add(data[j])
      self.process_subset(_set)
      return
    
    if i >= n:
      return
    
    data[index] = arr[i]
    self.combination_util(arr, n, r, index+1, data, i+1)

    self.combination_util(arr, n, r, index, data, i+1)

  def process_subset(self, subset):
    A = [[0.0 for _ in range(self.m)] for _ in range(self.m)]
    b = [0.0] * m
    self.update_matrices(subset, A, b)
    g_elim = GaussianElimination(A, b)
    if not g_elim.has_solution:
      return
    temp_result = g_elim.b
    if not self.satisfies_all_eq(temp_result):
      return
    val = self.compute_val(temp_result)
    if val > max_value:
      max_value = temp_result
      if subset.contains(n + m):
        bounded = False
      else:
        bounded = True

  def satisfies_all_eq(self, result):
    staisfied = True
    for i in range(self.n):
      _sum = 0
      for j in range(self.m):
        _sum += result[j] * self.A[i][j]
      if _sum > b[i] + math.pow(10, -3):
        staisfied = False
        break
    for i in range(self.m):
      if result[i] * -1 > math.pow(10, -3):
        staisfied = False
        break
    
    return staisfied

  def compute_val(self, result):
    val = 0
    for i in range(len(result)):
      val += result[i] * self.c[i]
    return val

  def update_matrices(self, S, A, b):
    print('UM', S)
    index = 0
    for val in S:
      if val < self.n:
        A[index] = self.A[index]
        b[index] = self.b[index]
      elif val < self.n + self.m:
        diff = val - self.n
        A[index] = [0.0] * m
        A[index][diff] = -1
        b[index] = 0
      else:
        A[index] = [1] * m
        b[index] = INF
      index += 1
    

def ReadEquation():
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    # print(A, '--', b, '--', c)
    return (n, m, A, b, c)

if __name__ == "__main__":
  n, m, A, b, c = ReadEquation()
  ls = LinearEquation(A, b, c)
  ls.print_res()
