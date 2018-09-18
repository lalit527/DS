def add_paren(result, left_rem, right_rem, string, index):
  if left_rem < 0 or right_rem < left_rem:
    return
  
  if left_rem == 0 and right_rem == 0:
    result.append(''.join(string))
  else:
    string[index] = '('
    add_paren(result, left_rem - 1, right_rem, string, index + 1)

    string[index] = ')'
    add_paren(result, left_rem, right_rem - 1, string, index + 1)



def generate_paren(count):
  string = [''] * (count * 2)
  arr = []
  add_paren(arr, count, count, string, 0)
  return arr

result = generate_paren(2)
print(result)