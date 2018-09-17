def num_steps(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  
  return num_steps(n - 1) + num_steps(n - 2) + num_steps(n - 3)

def num_steps_memo(n):
  memo = [-1] * (n + 1)
  return _num_steps_memo(n, memo)


def _num_steps_memo(n, memo):
  if n < 0:
    return 0
  
  if n == 0:
    return 1
  
  if memo[n] > -1:
    return memo[n]

  memo[n] = _num_steps_memo(n - 1, memo) + _num_steps_memo(n - 2, memo) + _num_steps_memo(n - 3, memo)
  return memo[n]

def num_steps_itr(n):
  if n < 0:
    return 0
  
  memo = [-1] * (n)
  memo[0] = 1
  memo[1] = 1 + memo[0]
  memo[2] = 1 + memo[1] + memo[0]
  for i in range(3, n):
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
  print(memo)
  return memo[n - 1] 

## Minimum steps
def min_num_steps(n):
  if n <= 0:
    return 0
  if n == 1 or n == 2 or n == 3:
    return 1
  return 1 + min(min_num_steps(n - 1), min_num_steps(n - 2), min_num_steps(n - 3))

def min_num_steps_memo(n):
  memo = [-1] * (n + 1)
  return _min_num_steps_memo(n, memo)

def _min_num_steps_memo(n, memo):
  if n <= 0:
    return 0
  if n == 1 or n == 2 or n == 3:
    return 1
  
  if memo[n] > -1:
    return memo[n]
  
  return 1 + min(_min_num_steps_memo(n - 1, memo), _min_num_steps_memo(n - 2, memo), _min_num_steps_memo(n - 3, memo))

if __name__ == "__main__":
  n = 10
  print(min_num_steps(n))
  print(min_num_steps_memo(n))
  # print(num_steps_memo(n))
  # print(num_steps_itr(n))