def zero_matrix(mat):
  n = len(mat)
  m = len(mat[0])
  row = [False] * n
  column = [False] * m

  def make_row_null(r):
    for i in range(len(mat[r])):
      mat[r][i] = 0
  
  def make_column_null(c):
    for j in range(len(mat)):
      mat[j][c] = 0

  for i in range(n):
    for j in range(m):
      if mat[i][j] == 0:
        row[i] = True
        column[j] = True

  for i in range(n):
    if row[i]:
      make_row_null(i)
  
  for j in range(m):
    if column[j]:
      make_column_null(j)
  
  
  
def print_matrix(mat):
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      print(mat[i][j], end = " ")
    print("")


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 0, 11, 12],
       [13, 14, 15, 16]]

zero_matrix(mat)
print_matrix(mat)