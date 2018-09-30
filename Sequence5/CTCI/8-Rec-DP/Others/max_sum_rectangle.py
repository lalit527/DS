from collections import namedtuple

Result = namedtuple("Result","maxSum leftBound rightBound upBound lowBound")

KadanesResult = namedtuple("KadanesResult","maxSum start end")

def kadanes(temp):
  _max = 0
  max_start = -1
  max_end = -1
  current_start = 0
  max_so_far = 0
  for i in range(len(temp)):
    max_so_far += temp[i]
    if max_so_far < 0:
      max_so_far = 0
      current_start = i + 1
    if max_so_far > _max:
      max_start = current_start
      max_end = i
      _max = max_so_far
  return KadanesResult(_max, max_start, max_end)
    


def max_sum_rectangle(rectangle):
  rows = len(rectangle)
  cols = len(rectangle[0])
  result = Result(float("-inf"), -1, -1, -1, -1)
  for left in range(cols):
    temp = [0 for _ in range(rows)]
    for right in range(left, cols):
      for i in range(rows):
        temp[i] += rectangle[i][right]

      kadanes_result = kadanes(temp)
      if kadanes_result.maxSum >  result.maxSum:
        result = Result(kadanes_result.maxSum, left, right, kadanes_result.start, kadanes_result.end)
  return result

M = [
  [2, 1, -3, -4, 5], 
  [0, 6, 3, 4, 1], 
  [2, -2, -1, 4, -5], 
  [-3, 3, 1, 0, 3]
]

result = max_sum_rectangle(M)
print(result)