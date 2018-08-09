# python3
from sys import stdin

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

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
      if abs(a[i][pivot_element.column]) > abs(_max):
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
    for i in range(pivot_element.row + 1, size):
      multiple = a[i][pivot_element.column]
      for j in range(pivot_element.column, size):
        a[i][j] -= (a[pivot_element.row][j] * multiple)
      b[i] -= b[pivot_element.row] * multiple


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    back_substitution(a, b)

    return b

def back_substitution(a, b):
  size = len(a)
  for i in range(size - 1, -1, -1):
    v = b[i]
    for j in range(i+1, size):
      b[j] -= a[j][i] * v
      a[j][i] = 0



def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

class LinearEquationSolver:
    def __init__(self, A, b, c):
        self.n = A.length
        self.m = c.length
        self.A = A
        self.b = b
        self.c = c
        total = n + m + 1
    
    def compute(self, total):
        arr = [None] * total
        for i in range(total):
            arr[i] = i
        gen_process_combinators(arr, total, )

def ReadEquation():
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    print(A)
    print(b, c)


if __name__ == "__main__":
    equation = ReadEquation()
    # print(equation.a)
    # print(equation.b)
    # solution = SolveEquation(equation)
    # PrintColumn(solution)
    # exit(0)
