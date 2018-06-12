# Uses python3

def edit_distance_memo(s, t):
  m = len(s) + 1
  n = len(t) + 1
  T = [[0 for i in range(n)] for j in range(m)]
  
  for i in range(m):
    for j in range(n):
      if i == 0:
        T[i][j] = j
      elif j == 0:
        T[i][j] = i
      elif s[i - 1] == t[j - 1]:
        T[i][j] = T[i-1][j-1]
      else:
        T[i][j] = 1 + min(T[i-1][j], T[i][j-1], T[i-1][j-1])
  return T[m-1][n-1]

if __name__ == "__main__":
    print(edit_distance_memo(input(), input()))
