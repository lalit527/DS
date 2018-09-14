def repeated_arithmetic_shift(x, count):
  for i in range(count):
    x >>= 1
  return x


def repeated_logical_shift(x, count):
  for i in range(count):
    x = lrs(x, 1)
  return x

def lrs(val, n): 
  return (val % 0x100000000) >> n


print(repeated_arithmetic_shift(-93242, 40))
print(repeated_logical_shift(-93242, 40))