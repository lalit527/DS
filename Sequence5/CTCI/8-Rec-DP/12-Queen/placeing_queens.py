def solve_nqueen(board):
  n = len(board)
  return _solve_nqueen(board, 0, n)

def is_safe(board, row, col, n):
  for i in range(col):
    if board[row][i] == 1:
      return False
  for i, j in zip(range(row, n), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  return True

def _solve_nqueen(board, col, n):
  if col >= n:
    return True
  for i in range(n):
    if is_safe(board, i, col, n):
      board[i][col] = 1
      if _solve_nqueen(board, col + 1, n):
        return True
      board[i][col] = 0
  return False

board = [ [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]
        ]

board_8 = [ [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
        ]

print(solve_nqueen(board_8))
print(board_8)