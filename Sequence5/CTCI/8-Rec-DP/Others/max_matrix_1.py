def maximum_histogram(rectangle):
  stack = []
  max_area = 0
  area = 0
  i = 0
  n = len(rectangle)
  while i < n:
    if len(stack) == 0 or rectangle[stack[-1]] <= rectangle[i]:
      stack.append(i)
      i += 1
    else:
      top = stack.pop()
      if len(stack) == 0:
        area = rectangle[top] * i
      else:
        area = rectangle[top] * (i - stack[-1] - 1)
    if area > max_area:
      max_area = area
  while len(stack) > 0:
    top = stack.pop()
    if len(stack) == 0:
      area = rectangle[top] * i
    else:
      area = rectangle[top] * (i - stack[-1] - 1)
    if area > max_area:
      max_area = area
  return max_area

def maximum_size_submatrix(rectangle):
  n = len(rectangle)
  m = len(rectangle[0])
  temp = [0 for i in range(m)]
  max_area = 0
  area = 0
  for i in range(n):
    for j in range(m):
      if rectangle[i][j] == 0:
        temp[j] = 0
      else:
        temp[j] += rectangle[i][j]
    area = maximum_histogram(temp)
    if area > max_area:
      max_area = area
  return max_area



if __name__ == "__main__":
  input = [[1,1,1,0],
            [1,1,1,1],
            [0,1,1,0],
            [0,1,1,1],
            [1,0,0,1],
            [1,1,1,1]]
  max_area = maximum_size_submatrix(input)
  print(max_area)