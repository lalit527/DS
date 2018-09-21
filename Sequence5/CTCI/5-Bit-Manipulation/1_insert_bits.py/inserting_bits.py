def num_to_binary(num):
  binary = []
  i = 0
  while num > 0:
    binary.append(num % 2)
    num = num // 2
    i += 1
  return ' '.join([i for i in map(lambda x: str(x), binary[::-1])])


def binary_to_dec(binary):
  num = 0
  n = binary
  base = 1
  tmp = n
  while tmp:
    last_digit = tmp % 10
    tmp = tmp // 10
    num += last_digit * base
    base = base * 2
  
  return num
  
def update_bits(n, m, i, j):
  if i >= 32 or j < i:
    return 0
  all_ones = ~0
  left = all_ones << (j + 1)
  right = ((1 << i) - 1)
  mask = left | right
  n_cleared = n & mask
  m_shifted = m << i
  return bin(n_cleared | m_shifted)

	

a= num_to_binary(103217)
b = num_to_binary(13)
update_bits(int(a), int(b), 4, 12)