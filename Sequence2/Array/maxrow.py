def maxRow(matrix):
    r = len(matrix)
    c = len(matrix[0])
    max_row_index = 0
    j = c - 1
    for i in range(0, r):
        print('for', i, j)
        while j >= 0 and matrix[i][j] == 1:
            print('while', i, j)
            j -= 1
            max_row_index = i
    return max_row_index

matrix = [[1, 0, 1, 0],
          [0, 0, 1, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]]

print(maxRow(matrix))