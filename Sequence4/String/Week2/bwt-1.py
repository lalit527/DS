# python3
import sys

def cyclic_rotation(text):
  n = len(text)
  _text = text + text
  result = [_text[i:i + n] for i in range(n)]
  return result

def bwt_matrix(text):
  rotated = cyclic_rotation(text)
  return sorted(rotated)

def BWT(text):
  n = len(text)
  burrow_wheeler_matrix = bwt_matrix(text)
  return ''.join([burrow_wheeler_matrix[i][n - 1] for i in range(n)])

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(BWT(text))