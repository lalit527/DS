def replace(str1, str2):
  m = len(str1)
  n = len(str2)
  return _replace(str1, str2, m, n)

def _replace(str1, str2, m, n):
  if m == 0:
    return n
  if n == 0:
    return m
  
  if str1[m-1] == str2[n-1]:
    return _replace(str1, str2, m-1, n-1)
  else:
    return 1 + min(_replace(str1, str2, m-1, n),
                   _replace(str1, str2, m, n-1),
                   _replace(str1, str2, m-1, n-1))

def replace_memo(str1, str2):
  m = len(str1)
  n = len(str2)
  result = [[0 for i in range(n)] for j in range(m)]
  for i in range(m):
    for j in range(n):
      if i == 0:
        result[i][j] = j
      elif j == 0:
        result[i][j] = i
      elif str1[i] == str2[j]:
        result[i][j] = result[i-1][j-1]
      else:
        result[i][j] = 1 + min(result[i][j-1],
                           result[i][j-1],
                           result[i-1][j-1])
  print(result)
  return result[i][j]  


s = "data"
r = "dataaaaaaa"
print(replace_memo(s, r))