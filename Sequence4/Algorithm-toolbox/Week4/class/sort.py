def selection_sort(A):
  n = len(A)
  for i in range(n):
    _min = i
    for j in range(i+1, n):
      if A[_min] > A[j]:
        _min = j
    A[_min], A[i] = A[i], A[_min]


A = [4, 7, 1, 3, 8, 9, 2]
selection_sort(A)
print(A)


def counting_sort(A):
  n = len(A)
  d = dict()
  for i in range(n):
    try:
      d[A[i]] += 1
    except:
      d[A[i]] = 0
  m = len(d)
  # count[]
  for i in range(n):
    pass

def count_sort(A):
  n = len(A)
  output = [0 for i in range(256)]
  count = [0 for i in range(256)]
  ans = ["" for _ in range(n)]
  for i in A:
    count[ord(str(i))] += 1
  
  

  for i in range(256):
    count[i] += count[i - 1]
  
  print(count)

  for i in range(n):
    print(count[ord(str(A[i]))]-1)
    output[count[ord(str(A[i]))] - 1] = A[i]
    count[ord(str(A[i]))] -= 1
  
  for i in range(n):
    ans[i] = output[i]
  
  print(ans)

A = [2, 3, 2, 1, 3, 2, 2, 3, 2, 2, 2, 1]
count_sort(A)