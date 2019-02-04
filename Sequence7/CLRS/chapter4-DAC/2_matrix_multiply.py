def square_matrix_multiply(A, B):
  n = len(A)
  C = [[None for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      C[i][j] = 0
      for k in range(n):
        C[i][j] = C[i][j] + A[i][k] * B[k][j]
  return C


def square_matrix_multiply_rec(A, B):
  n = len(A)
  C = [[None for _ in range(n)] for _ in range(n)]
  if n == 1:
    C[1][1] = A[1][1] * B[1][1]
  else:
    mid = n // 2
    A11 = A[:]


def main():
  A = [[1, 2], [3, 4]]
  B = [[5, 6], [7, 8]]
  print(square_matrix_multiply(A, B))

if __name__ == "__main__":
  main()