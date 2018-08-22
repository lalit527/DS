def rotate_matrix(mat):
  n = len(mat)
  if n == 0 or n != len(mat[0]):
    return False
  for layer in range(n//2):
    first = layer
    last = n - 1 - layer
    for i in range(first, last):
      offset = i - first
      top = mat[first][i]
      mat[first][i] = mat[last - offset][first]
      mat[last - offset][first] = mat[last][last - offset]
      mat[last][last - offset] = mat[i][last]
      mat[i][last] = top

def print_matrix(mat):
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      print(mat[i][j], end = " ")
    print("")



mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

rotate_matrix(mat)
print_matrix(mat)