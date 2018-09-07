def edit_distance(s1, s2):
  n = len(s1)
  m = len(s2)
  if m == 0:
    return n
  
  if n == 0:
    return m

  if s1[n-1] == s2[m-1]:
    return edit_distance(s1[:n-1], s2[:m-1])
  
  return 1 +  min(edit_distance(s1[:n-1], s2[:m-1]),
                  edit_distance(s1[:n], s2[:m-1]),
                  edit_distance(s1[:n-1], s2[:m]))



def edit_distance_memo(s1, s2):
  n = len(s1)
  m = len(s2)
  if m == 0:
    return n
  
  if n == 0:
    return m

  memo = [[0 for i in range(n+1)] for j in range(m+1)]
  print(memo)
  for i in range(n+1):
    for j in range(m+1):
      if i == 0:
        memo[i][j] = j
      elif j == 0:
        memo[i][j] = i
      elif s1[i - 1] == s2[j - 1]:
        memo[i][j] = memo[i-1][j-1]
      else:
        memo[i][j] = 1 + min(memo[i-1][j-1], memo[i-1][j], memo[i][j-1])

  print(memo)
  return memo[m][n]


if __name__ == "__main__":
    print(edit_distance_memo(input(), input()))
