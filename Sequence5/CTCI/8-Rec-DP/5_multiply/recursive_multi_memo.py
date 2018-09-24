def rec_mult_memo(a, b):
  smaller = a if a < b else b
  bigger = a if a > b else b
  memo = [0] * (smaller + 1)
  return _rec_mult_memo(smaller, bigger, memo)

def _rec_mult_memo(smaller, bigger, memo):
  if smaller == 0:
    return 0
  elif smaller == 1:
    return bigger
  elif memo[smaller] > 0:
    return memo[smaller]
  
  s = smaller >> 1
  side1 = rec_mult_memo(s, bigger) 
  side2 = side1
  if smaller % 2 == 1:
    side2 = _rec_mult_memo(smaller - s, bigger, memo)
  memo[smaller] = side1 + side2
  return memo[smaller]

if __name__ == "__main__":
  print(rec_mult_memo(9, 10))