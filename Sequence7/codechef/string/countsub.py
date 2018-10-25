import sys

def count_sub_string(n, W):
  count = 0
  for c in W:
    if c == '1':
      count += 1
  return (count * (count + 1)) // 2

def main():
  num_cases = int(sys.stdin.readline().strip())
  for _ in range(num_cases):
    n = sys.stdin.readline().strip()
    W = sys.stdin.readline().strip()
    print(count_sub_string(n, W))

if __name__ == "__main__":
  main()