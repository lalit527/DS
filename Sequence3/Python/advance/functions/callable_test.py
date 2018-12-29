def is_even(num):
  return num % 2 == 0

print(callable(is_even))

is_odd = lambda num: num % 2 == 1

print(callable(is_odd))

print(callable(list))

print(callable(list.append))

class NoCall:
  def __init__(self):
    pass

class Call:
  def __init__(self):
    pass
  
  def __call__(self):
    pass

print(callable(NoCall))
print(callable(Call))

print(callable('Call'))