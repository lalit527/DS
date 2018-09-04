def min_refill(x, n, L):
  numRefills = 0
  curRefill = 0
  while curRefill < n:
    lastRefill = curRefill
    while curRefill < n and (x[curRefill + 1] - x[lastRefill] <= L):
      print(curRefill, lastRefill)
      curRefill += 1
    if curRefill == lastRefill:
      raise Exception("No Solution")
    if curRefill <= n:
      numRefills += 1

  return numRefills

x = [0, 30, 32, 33, 37, 49, 53, 59, 61]
n = len(x) - 1
L = 16

print(min_refill(x, n, L))