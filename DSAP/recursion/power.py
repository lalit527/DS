def power(x, n):
  if n == 0:
    return 1
  return x * power(x, n-1)

def power_opt(x, n):
  if n == 0:
    return 1
  partial = power_opt(x, n // 2)
  result = partial * partial
  if n % 2 == 1:
    result *= x
  return result

print(power_opt(2, 4))