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
  m = (2 * n - 1)
  R = [0] * m
  if n == 1:
    R[0] = A[a1] * B[b1]
    return R
  R[0: n - 2] = _mult_poly_dnc(A, B, (n//2), a1, b1)
  R[n: m] = _mult_poly_dnc(A, B, (n//2), a1 + (n//2), b1 + (n//2))
  D0E1 = _mult_poly_dnc(A, B, (n//2), a1, b1 + (n//2))
  D1E0 = _mult_poly_dnc(A, B, (n//2), a1 + (n//2), b1)
  R[(n//2): (n + (n//2) - 2)] += D0E1 + D1E0
  return R

def karatsuba_mult(A, B, n):
  print(_karatsuba_mult(A, B, n))

def _karatsuba_mult(A, B, n):
  product = [0.0] * (2*n)
  if n == 1:
    product[0] = A[0] * B[0]
    return product
  
  half_array_size = n // 2

  Alow = [0.0] * half_array_size
  Ahigh = [0.0] * half_array_size
  Blow = [0.0] * half_array_size
  Bhigh = [0.0] * half_array_size

  Alow_high = [0.0] * half_array_size
  Blow_high = [0.0] * half_array_size

  for index in range(half_array_size):
    Alow[index] = A[index]
    Ahigh[index] = A[index + half_array_size]
    Alow_high[index] = Alow[index] + Ahigh[index]

    Blow[index] = B[index]
    Bhigh[index] = B[index + half_array_size]
    Blow_high[index] = Blow[index] + Bhigh[index] 
  
  productLow = _karatsuba_mult(Alow, Blow, half_array_size)
  productHigh = _karatsuba_mult(Ahigh, Bhigh, half_array_size)
  productLowHigh = _karatsuba_mult(Alow_high, Blow_high, half_array_size)

  productMiddle = [0.0] * n
  for index in range(n):
    productMiddle[index] = productLowHigh[index] - productLow[index] - productHigh[index]

  middle_offset = n // 2
  for index in range(n):
    product[index] += productLow[index]
    product[index + n] += productHigh[index]
    product[index + middle_offset] += productMiddle[index]

  return product 


A = [0, 5, 3, 0, 0, 4, 0, 1]
B = [0, 0, 6, 0, 0, 0, 0, 5]
n = 8
karatsuba_mult(A, B, n)