# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s)
    n = len(t)

    if m == 0:
      return n
    
    if n == 0:
      return m

    if s[m-1] == t[n-1]:
      return edit_distance(s[:m-1], t[:n-1])
    
    return 1 + min(edit_distance(s[:m], t[:n-1]), 
                    edit_distance(s[:m-1], t[:n]),
                    edit_distance(s[:m-1], t[:n-1]))

def edit_distance_memo(s, t):
  m = len(s) + 1
  n = len(t) + 1
  T = [[0 for i in range(n)] for j in range(m)]
  print(T)

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
  print(T)
  print(i, j)
  return T[m-1][n-1]

if __name__ == "__main__":
    print(edit_distance_memo(input(), input()))
