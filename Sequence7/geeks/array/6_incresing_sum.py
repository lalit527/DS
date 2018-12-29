def longest_subseq(arr):
  n = len(arr)
  longest = 0
  for i in range(n - 1):
    longest_till_now = longest_subseq_helper(arr, i + 1, arr[i])
    if longest_till_now > longest:
      longest = longest_till_now
  return longest + 1

def longest_subseq_helper(arr, next_idx, curr_ele):
  if next_idx == len(arr):
    return 0
  
  tmp1 = 0
  if arr[next_idx] > curr_ele:
    tmp1 = 1 + longest_subseq_helper(arr, next_idx + 1, arr[next_idx])
  
  tmp2 = longest_subseq_helper(arr, next_idx + 1, curr_ele)

  return max(tmp1, tmp2)

def longest_inc_sub(arr):
  n = len(arr)
  T = [1 for _ in range(n)]
  sol = [i for i in range(n)]

  for i in range(1, n):
    for j in range(i):
      if arr[i] > arr[j] and T[i] < T[j] + 1:
        T[i] = T[j] + 1
        sol[i] = j

  max_val = max(T)
  max_idx = T.index(max_val)

  next_idx = max_idx
  while True:
    print(arr[next_idx])
    old_idx = next_idx
    next_idx = sol[next_idx]
    if next_idx == old_idx:
      break
  return T[max_idx]

def max_inc_sub(arr):
  n = len(arr)
  T = [0 for x in range(n)]
  for i in range(n):
    T[i] = arr[i]
  
  for i in range(1, n):
    for j in range(i):
      if arr[i] > arr[j] and T[i] < T[j] + arr[i]:
        T[i] = T[j] + arr[i]
  tmp = 0
  for i in range(n):
    if tmp < T[i]:
      tmp = T[i]
  return tmp

def main():
  # n = int(sys.stdin.readline())
  # data = []
  arr = [1, 101, 2, 3, 100, 4, 5] 
  print (max_inc_sub(arr))
  # for _ in range(n):
  #   c = sys.stdin.readline()
  #   tmp = []
  #   tmp.extend(sys.stdin.readline().split())
  #   tmp = list(map(lambda x: int(x), tmp))
  #   data.append(tmp)
  #   print(equilibrium(tmp))
  
if __name__ == "__main__":
  main()
