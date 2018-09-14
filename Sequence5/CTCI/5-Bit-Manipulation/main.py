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

num = num_to_binary(89)
print(num)
num = int(num.replace(' ', ''))
print(binary_to_dec(num))