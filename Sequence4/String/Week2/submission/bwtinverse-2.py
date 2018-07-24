# python3
import sys

def InverseBWT(bwt):
  n = len(bwt)
  v = [(value, index) for index, value in enumerate(bwt)]
  v_s = sorted(v)
  map_data = {first: second for first, second in zip(v_s, v)}
  current = v_s[0]
  result = ''
  for i in range(n):
    result += current[0]
    current = map_data[current]
  return result[::-1]

if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  print(InverseBWT(bwt))