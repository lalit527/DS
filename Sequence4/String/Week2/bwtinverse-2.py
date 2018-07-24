# python3
import sys

def InverseBWT(bwt):
  n = len(bwt)
  all = [(value, index) for index, value in enumerate(bwt)]
  # print(all)
  sorted_all = sorted(all)
  # print(sorted_all)
  matrix_val = {a: s for a, s in zip(sorted_all, all)}
  # print(matrix_val)
  current = sorted_all[0]
  result = ''
  for i in range(n):
    result += current[0]
    current = matrix_val[current]
  return result[::-1]


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  print(InverseBWT(bwt))