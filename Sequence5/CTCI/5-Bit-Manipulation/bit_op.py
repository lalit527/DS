from right_shift import *
from main import *

def get_bit(num, i):
  return ((num & (1 << i)) != 0)

def set_bit(num, i):
  return num | (1 << i)


b = num_to_binary(10)
print(b)
b = num_to_binary(14)
print(b)

print(set_bit(10, 2))