def isSafe( maze, x, y ):  
    N = len(maze)    
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
        return True  
    return False

def solve_maze(maze):
  n = len(maze)
  m = len(maze[0])
  result = [[0 for _ in range(m)] for _ in range(n)]
  if _solve_maze(maze, result, 0, 0, n - 1, m - 1):
    return result
  return []

def _solve_maze(maze, result, cur_x, cur_y, dest_x, dest_y):
  if cur_x == dest_x and cur_y == dest_y:
    result[cur_x][cur_y] = 1
    return True
  if isSafe(maze, cur_x, cur_y) == 1:
    result[cur_x][cur_y] = 1
    if _solve_maze(maze, result, cur_x + 1, cur_y, dest_x, dest_y):
      return True
    if _solve_maze(maze, result, cur_x, cur_y + 1, dest_x, dest_y):
      return True
    result[cur_x][cur_y] = 0
    return False


if __name__ == "__main__":
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ] 
    print(solve_maze(maze))