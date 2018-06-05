# python3

def get_pisano_period(m):
  a = 0
  b = 1
  for i in range(m * m):
    c = (a + b) % m
    a = b
    b = c
    if a == 0 and b == 1:
      return i + 1
  return m

def get_fibo_huge_better(n, m):
  if n <= 1:
    return n

  previous = 0
  current = 1
  new_fibo = get_pisano_period(m)
  for _ in range(new_fibo - 1):
    previous, current = current, (previous + current) % m

  return current % m


if __name__ == '__main__':
  input = sys.stdin.read();
  n, m = map(int, input.split())
  print(get_fibo_huge_better(n, m))
