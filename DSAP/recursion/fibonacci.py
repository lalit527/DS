def bad_fibo(n):
  if n <= 1:
    return n
  return bad_fibo(n - 2) + bad_fibo(n - 1)

def good_fibo(n):
  if n <= 1:
    return (n, 0)
  (a, b) = good_fibo(n - 1)
  return (a+b, a)

print(bad_fibo(5))