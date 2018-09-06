def mult_poly_naive(A, B, n):
  pair = [[None for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      pair[i][j] = A[i] * B[j]
  m = 2 * n - 1
  product = [0] * m
  for i in range(n):
    for j in range(n):
      product[i + j] = product[i + j] + pair[i][j]

  print(product)


def mult_poly_dnc(A, B, n):
  print(_mult_poly_dnc(A, B, n, 0, 0))

def _mult_poly_dnc(A, B, n, a1, b1):
  m = (2 * n - 2)
  R = [None] * m
  if n == 1:
    print(a1, b1)
    R[0] = A[a1] * B[b1]
    return R
  R[0: n - 2] = _mult_poly_dnc(A, B, (n//2), a1, b1)
  R[n: m] = _mult_poly_dnc(A, B, (n//2), a1 + (n//2), b1 + (n//2))
  D0E1 = _mult_poly_dnc(A, B, (n//2), a1, b1 + (n//2))
  D1E0 = _mult_poly_dnc(A, B, (n//2), a1 + (n//2), b1)
  R[(n//2): (n + (n//2) - 2)] += D0E1 + D1E0
  return R

A = [3, 2, 5]
B = [5, 1, 2]
n = 3
mult_poly_dnc(A, B, n)