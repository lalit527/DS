def get_subset(set, index):
  if len(set) == index:
    all_subset = []
    all_subset.append([])
  else:
    all_subset = get_subset(set, index + 1)
    item = set[index]
    more_subset = []
    for subset in all_subset:
      new_subset = []
      new_subset.extend(subset)
      new_subset.append(item)
      more_subset.append(new_subset)
    all_subset.extend(more_subset)
  
  return all_subset

def get_subset_2(set):
  all_subset = []
  _max = 1 << len(set) # Computes 2^n
  for k in range(_max):
    subset = convert_int_set(k, set)
    all_subset.append(subset)
  return all_subset

def convert_int_set(x, set):
  subset = []
  index = 0
  k = x
  while k > 0:
    if ((k & 1) == 1):
      subset.append(set[index])
    index += 1
    k >>= 1
  return subset

if __name__ == "__main__":
  A = [0, 1, 2]
  subset = get_subset_2(A)
  print(subset)