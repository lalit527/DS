def compute_prefix(S):
  n = len(S)
  s = [None] * (n)
  s[0] = 0
  border = 0
  for i in range(1, n):
    while border > 0 and S[i] != S[border]:
      border = s[border - 1]
    if S[i] == S[border]:
      border += 1
    else:
      border = 0
    s[i] = border
  print(s)
  return s




def find_all_occurence(t, p):
  S = p + '$' + t
  s = compute_prefix(S)
  result = []
  for i in range(len(p) + 1, len(S)):
    if s[i] == len(p):
      result.append(i - 2 * len(p))
  print(result)

pattern = "abra"
text = "abracadabra"
find_all_occurence(text, pattern)