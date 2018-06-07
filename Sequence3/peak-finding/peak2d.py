def peak_finder(matrix, r, c):
  best_till_now = float('-inf')
  for i in range(r):
    for j in range(c):
      if i == 0 and j == 0 \
        and matrix[i][j] >= matrix[i][j + 1] \
        and matrix[i][j] >= matrix[i + 1][j]:
        best_till_now = matrix[i][j]
      
      if i == r - 1 and j == c - 1 \
        and matrix[i][j] >= matrix[i][j - 1] \
        and matrix[i][j] >= matrix[i - 1][j]:
        best_till_now = matrix[i][j]

      if i == 0 and j > 0:
        pass
  print(best_till_now)


def find_peak(matrix, rows, cols):
  return peak_finder_rec(matrix, rows, cols, cols // 2)

def peak_finder_rec(matrix, rows, cols, mid):
  max_found = [0] * 1
  max_index = find_max(matrix, rows, mid, max_found)

  if mid == 0 or mid == cols - 1:
    return max_found[0]
  
  if (max_found[0] >= matrix[max_index][mid - 1] and max_found [0] >= matrix[max_index][mid + 1]):
      return max_found[0]
  
  if max_found[0] < matrix[max_index][mid - 1]:
    return peak_finder_rec(matrix, rows, cols, mid - mid // 2)
  #print(max_found[0])
  return peak_finder_rec(matrix, rows, cols, mid + mid//2)

def find_max(matrix, rows, mid, max_found):
  max_index = 0
  for i in range(rows):
    if max_found[0] < matrix[i][mid]:
      max_found[0] = matrix[i][mid]
      max_index = i
  return max_index

problemMatrix = [
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 8,  9, 10, 11, 12, 11, 10,  9,  8,  7,  6],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
	[ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
]
find_peak(problemMatrix, len(problemMatrix), len(problemMatrix[0]))