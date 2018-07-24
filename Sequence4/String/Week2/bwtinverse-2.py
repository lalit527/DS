# python3
import sys

def InverseBWT(bwt):
  last = [(key, index) for key, index in enumerate(bwt)]
  print(last)
  return ""


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  print(InverseBWT(bwt))