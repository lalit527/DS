# Uses python3
import sys

def get_change(m):
    #write your code here
    changes = [1, 3, 4]
    cols = m + 1
    rows = len(changes)
    table = [[0 if col == 0 else float("inf") for col in range(cols)] for j in range(rows)]
    
    for i in range(rows):
      for j in range(1, cols):
        if j < changes[i]:
          table[i][j] = table[i-1][j]
        else:
          table[i][j] = min(table[i - 1][j], 1 + table[i][j - changes[i]])
    # print(table)
    return table[rows-1][cols - 1]
    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
