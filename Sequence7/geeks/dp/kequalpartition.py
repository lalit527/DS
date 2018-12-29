def _can_partion(arr, subset_sum, taken, subset, k, n, cur_idx, lmt_idx):
  if subset_sum[cur_idx] == subset:
    if cur_idx == k - 2:
      return True

    return _can_partion(arr, subset_sum, taken, subset, k, n, cur_idx + 1, n - 1)
  
  for i in range(lmt_idx, -1, -1):
    if taken[i]:
      continue
    tmp = subset_sum[cur_idx] + arr[i]

    if tmp <= subset:
      taken[i] = True
      subset_sum[cur_idx] += arr[i]
      nxt = _can_partion(arr, subset_sum, taken, subset, k, n, cur_idx, i - 1)

      taken[i] = False
      subset_sum[cur_idx] -= arr[i]
      if nxt:
        return True
  return False

def can_partition(arr, n, k):
  if k == 1:
    return True
  if n < k:
    return False

  sum = 0
  for ele in arr:
    sum += ele
  
  if sum % k != 0:
    return False
  
  subset = sum // k
  subset_sum = [0] * k
  taken = [False] * n
  subset_sum[0] = arr[n - 1]
  taken[n - 1] = True
  return _can_partion(arr, subset_sum, taken, subset, k, n, 0, n - 1)

def can_partition_2(arr, n, k):
  target, rem = divmod(sum(arr), k)
  if rem or max(arr) > target:
    return False
  memo = [None] * (1 << n)
  memo[-1] = True
  def search(used, todo):
    if memo[used] is None:
      targ = (todo - 1) % target + 1
      for i, a in enumerate(arr):
        if (used >> i) & 1 == 0 and a <= targ:
          memo[used] = any(search(used | (1<<i), todo - a))              
    return memo[used]
  return search(0, target * k)
  
  
  
 
if __name__ == "__main__":
  arr = [2, 1, 4, 5, 3, 3]
  n = len(arr)
  k = 3
  print(can_partition_2(arr, n, k))