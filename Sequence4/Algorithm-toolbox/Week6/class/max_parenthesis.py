
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return -1

def min_and_max(i, j, M, m, op):
  _min = float('inf')
  _max = float('-inf')
  for k in range(i, j):
    a = evalt(M[i][k], M[k+1][j], op[k])
    b = evalt(M[i][k], m[k+1][j], op[k])
    c = evalt(m[i][k], M[k+1][j], op[k])
    d = evalt(m[i][k], m[k+1][j], op[k])
    _min = min(_min, a, b, c, d)
    _max = max(_max, a, b, c, d)
  return _min, _max


def get_max_parenthesis(dataset):
    operands = dataset[1:len(dataset):2]
    data = dataset[0:len(dataset)+1:2]
    n = len(data)
    m = [[0 for i in range(n)] for j in range(n)]
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
      m[i][i] = int(data[i])
      M[i][i] = int(data[i])
    for s in range(1, n):
      for i in range(n - s):
        j = i + s
        m[i][j], M[i][j] = min_and_max(i, j, M, m, operands)
    return M[0][n-1]  




D = [5, '-', 8, '+', 7, '*', 4, '-', 8, '+', 9]
val = get_max_parenthesis(D)
print(val)