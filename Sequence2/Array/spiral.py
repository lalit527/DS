def printSpiral(matrix):
    row = len(matrix)
    col = len(matrix[0])
    curRow = 0
    curCol = 0
    while curRow < row and curCol < col:
        for i in range(curCol, col, 1):
            print(matrix[curRow][i])
        curRow += 1

        for i in range(curRow, row, 1):
            print(matrix[i][col-1])
        col -= 1

        for i in range(col-1, curCol-1, -1):
            print(matrix[row-1][i])
        row -= 1

        for i in range(row-1, curRow-1, -1):
            print(matrix[i][curCol])
        curCol += 1


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

printSpiral(matrix)