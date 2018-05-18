def fibo_rec(n):
  if n == 1 or n == 0:
    return 1
  fib = fibo_rec(n-1) + fibo_rec(n-2)
  return fib

def fibo_memo(n):
  lookup = [None] * (n+1)
  return _fibo_memo(n, lookup)

def _fibo_memo(n, lookup):
  if lookup[n] is None:
    if n <= 1:
      lookup[n] = 1
    else:
      lookup[n] = _fibo_memo(n-1, lookup) + _fibo_memo(n-2, lookup)
  
  return lookup[n]

print(fibo_memo(4))
print(fibo_rec(4))