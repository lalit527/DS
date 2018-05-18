def minSteps(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  count = minSteps(n-1) + minSteps(n-2)
  return count

def minSteps_memo(n):
  result = [None] * (n+1)
  return _minSteps_memo(n, result)

def _minSteps_memo(n, result):
  if result[n] is None:
    if n == 1:
      result[n] = 1
    elif n ==2:
      result[n] = 2
    else:
      result[n] = _minSteps_memo(n-1, result) + _minSteps_memo(n-2, result)
  return result[n]

print(minSteps_memo(700))