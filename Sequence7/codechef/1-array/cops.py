import sys
from collections import defaultdict

def check_safe_house(data, x, y):
  houses = [-1] * 101
  coverage = x * y
  result = 0
  for i in data:
    l = max(1, i - coverage)
    u = min(100, i + coverage)
    for i in range(l, u + 1):
      houses[i] = 1
  
  count = 0 
  for i in range(1, 101):
    if houses[i] == -1:
      count += 1
  return count

# def check_safe_house(data, x, y):
#   lower = float('inf')
#   upper = float('-inf')
#   coverage = x * y
#   result = 0
#   for i in data:
#     l = max(1, i - coverage)
#     u = min(1, i + coverage)

#     if lower > l:
#       lower = l
    
#     if upper < u:
#       upper = u
  
#   if lower == 1 and upper == 100:
#     result = 0
#   else:
#     result = () 


def main():
  D = defaultdict(lambda: 'NO')
  num_cases = int(sys.stdin.readline())
  for _ in range(num_cases):
    M, x, y = sys.stdin.readline().split()
    data = sys.stdin.readline().split()
    data = list(map(lambda x: int(x), data))
    print(check_safe_house(data, int(x), int(y)))
    
if __name__ == "__main__":
  main()