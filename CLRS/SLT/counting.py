def countSort(A, B, k):
  C = [0] * (k + 1)
  for j in A:
    C[j] = C[j] + 1
  print(C)

  for i in range(1, k + 1):
    C[i] = C[i] + C[i - 1]
  
  print(C)

  for j in range(len(A)-1, -1, -1):
    # B[C[A[j]]] = A[j]
    B[C[A[j]] - 1] = A[j]
    C[A[j]] = C[A[j]] - 1
  
  print(C)
  print(B)

arr = [2,5,3,0,2,3,0,3]
b = [None] * len(arr)
k = 5
countSort(arr, b, k)
