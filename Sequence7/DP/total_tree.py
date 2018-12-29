def get_tree_count(num):
  if num == 0 or num == 1:
    return 1
  total = 0
  for i in range(1, num + 1):
    total += get_tree_count(i-1) * get_tree_count(num - i)
  return total

def get_tree_count_dp(num):
  T = [0] * (num+1)
  T[0] = 1
  T[1] = 1
  import pdb; pdb.set_trace()
  for i in range(2, num+1):
    total = 0
    for k in range(i):
      total += T[k] * T[i - k -1]
    T[i] = total
  return T[num]


def main():
  print(get_tree_count_dp(5))

if __name__ == "__main__":
  main()