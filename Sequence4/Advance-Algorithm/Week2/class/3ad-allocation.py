# python3
import sys

EPS = 1e-6
PRECISION = 20

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
    return (n, m, A, b, c)

def augmented(table):
  n = len(table) - 1
  m = len(table[0]) - 1
  augmented = [None] * (len(table) - 1)
  column_count = [None] * n
  for r_idx, row in enumerate(table):
    for c_idx, e in enumerate(row[:-1]):
      cc = column_count[c_idx]
      if e != 0 and e != 1:
        column_count[c_idx] = -1
      elif e > 0 and (cc is not None and cc >= 0):
        column_count[c_idx] -= 1
        

def initial_table(A, b, c):
  table = [row.copy() for row in a]
  n = len(table)
  for idx, row in enumerate(table):
    basic_row = [0] * n
    b_val = b[idx]
    if b_val < 0:
      basic_row[idx] = -1
      new_row = [-e for e in row] + basic_row + [-b_val]
    else:
      basic_row[idx] = 1
      new_row = row + basic_row + [b_val]
    table[idx] = new_row
  table.append([-i for i in c] + [0] * (n + 1))
  return table

def allocate_ads(n, m, A, b, c):
  table = initial_table(A, b, c)
  n_initial = len(table[0]) - 1
  (basic, augmented) = augmented(table)

if __name__ == "__main__":
  n, m, A, b, c = ReadEquation()
  ans_t, ans_x = allocate_ads(n, m, A, b, c)
  