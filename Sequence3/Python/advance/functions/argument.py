def test(*args):
  print(args)

def key_test(**kwarg):
  print(args)

def print_args(arg1, arg2, *args, kwarg1, kwarg2):
  print(arg1)
  print(arg2)
  print(args)
  print(kwarg1)
  print(kwarg2)

print_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7)


def print_args2(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
  print(arg1)
  print(arg2)
  print(args)
  print(kwarg1)
  print(kwarg2)
  print(kwargs)

print_args2(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwarg3=8, kwarg4=9)


"""
Extended Args
"""

def print_ext_arg(arg1, arg2, *args):
  print(arg1)
  print(arg2)
  print(args)

t = (11, 12, 13, 14)
print_ext_arg(*t)


def print_ext_kwarg(red, green, blue, **kwargs):
  print("r = ", red)
  print("g = ", green)
  print("b = ", blue)
  print(kwargs)

t = {'red': 21, 'green': 31, 'blue': 41, 'alpha': 51, 'beta': 61}
print_ext_kwarg(**t)

"""
Forwarding Arguments
"""

def trace(f, *args, **kwargs):
  print("args = ", args)
  print("kwargs = ", kwargs)
  result = f(*args, **kwargs)
  print("result = ", result)
  return result

print(int('ff', base=16))
print(trace(int, 'ff', base=16))
