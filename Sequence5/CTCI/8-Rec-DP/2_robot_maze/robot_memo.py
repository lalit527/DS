from collections import defaultdict

class Points:
  def __init__(self, row, col):
    self.row = row
    self.col = col

  def __str__(self):
    return "Points: row:- {} and col:- {}".format(self.row, self.col)

def path_maze(grid):
  if grid is None or len(grid) == 0:
    return None
  path = []
  row = len(grid) - 1
  col = len(grid[0]) - 1
  memo = defaultdict(lambda: -1)
  if get_path(grid, row, col, path, memo):
    return path
  
  return None

def get_path(grid, row, col, path, memo):
  if row < 0 or col < 0 or grid[row][col] == 1:
    return False

 
  for p, s in memo.items():
    if p.row == row and p.col == col:
      print('cached')
      return s

  point = Points(row, col)
  success = False
  
  if (row == 0 and col == 0) or (get_path(grid, row - 1, col, path, memo) or get_path(grid, row, col - 1, path, memo)):
    path.append(point)
    success = True
    return True
  key = point
  memo[point] = success
  return False

  

grid = [[0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0]]

path = path_maze(grid)
if path and len(path) > 0:
  for p in path:
    print(p)