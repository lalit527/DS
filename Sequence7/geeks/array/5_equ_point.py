def equilibrium(arr):
  n = len(arr)
  if n == 0:
    return -1
  if n == 1:
    return arr[0]
  lsum = 0
  rsum = 0
  for i in range(n):
    lsum = 0
    rsum = 0
    for j in range(i):
      lsum += arr[j]
    for j in range(i + 1, n):
      rsum += arr[j]
    if lsum == rsum:
      return i
  return -1

def equilibrium_better(arr):
  n = len(arr)
  total_sum = 0
  left_sum = 0
  for i in range(n):
    total_sum += arr[i]
  for i in range(n):
    total_sum -= arr[i]
    if total_sum == left_sum:
      return i 
    left_sum += arr[i]
  return -1

def main():
  # n = int(sys.stdin.readline())
  # data = []
  arr = [-7, 1, 5, 2, -4, 3, 0] 
  print (equilibrium_better(arr))
  # for _ in range(n):
  #   c = sys.stdin.readline()
  #   tmp = []
  #   tmp.extend(sys.stdin.readline().split())
  #   tmp = list(map(lambda x: int(x), tmp))
  #   data.append(tmp)
  #   print(equilibrium(tmp))
  
if __name__ == "__main__":
  main()
