# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    print(W, w)
    cols = W + 1
    rows = len(w) + 1
    T = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(1, rows):
      for j in range(1, cols):
        if w[i - 1] <= j:
          T[i][j] = max(w[i-1] + T[i-1][j - w[i-1]], T[i-1][j])
        else:
          T[i][j] = T[i-1][j]
    print(T)
    return T[row-1][cols-1]

def optimal_weight_dup(W, w):
    # write your code here
    result = 0
    print(W, w)
    cols = W + 1
    rows = len(w) + 1
    T = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(1, rows):
      for j in range(1, cols):
        if w[i - 1] <= j:
          T[i][j] = max(w[i-1] + T[i-1][j - w[i-1]], T[i-1][j])
        else:
          T[i][j] = T[i-1][j]
    print(T)
    return T[row-1][cols-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
