def match_regex_rec(text, expr):
  return _match_regex_rec(text, expr, 0, 0)

def _match_regex_rec(text, expr, pos1, pos2):
  if pos2 == len(expr):
    return pos1 == len(text)
  
  if pos2 == len(expr) - 1 or expr[pos2 + 1] != '*':
    return (pos1 < len(text) and (text[pos1] == expr[pos2] or expr[pos2] == '.')) and _match_regex_rec(text, expr, pos1+1, pos2+1)
  if _match_regex_rec(text, expr, pos1, pos2+2):
    return True
  while pos1 < len(text) and (text[pos1] == expr[pos2] or expr[pos2] == '.'):
    if _match_regex_rec(text, expr, pos1+1, pos2+2):
      return True

    pos1 += 1
  return False

def _match_regex_dp(text, expr):
  rows = len(text)
  cols = len(expr)
  T = [[False for _ in range(cols + 1)]for _ in range(rows + 1)]
  T[0][0] = True

  for i in range(1, cols):
    if expr[i-1] == '*':
      T[0][i] = T[0][i - 2]
  
  for i in range(1, rows):
    for j in range(1, cols):
      if expr[j - 1] == '.' or expr[j - 1] == text[i - 1]:
        T[i][j] = T[i-1][j-1]
      elif expr[j - 1] == '*':
        T[i][j] = T[i][j - 2]
        if expr[j - 2] == '.' or expr[j - 2] == text[i - 1]:
          T[i][j] = T[i][j] or T[i - 1][j]
      else:
        T[i][j] = False
  return T[rows][cols]

def main():
  text = "abc"
  expr = "acb."
  print(match_regex_rec(text, expr))


if __name__ == '__main__':
  main()