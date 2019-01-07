def arrayManipulation(n, queries):
  A = [0] * (n + 1)
  tmp = 0
  x = 0
  for start, end, fact in queries:
    A[start] += fact
    if (end + 1) <= n:
      A[end + 1] -= fact

  for i in range(1, n+1):
    x += A[i]
    tmp = max(tmp, x)
  return tmp


def main():
  line = nm = input().split()
  n = int(nm[0])
  m = int(nm[1])
  queries = []
  for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
  result = arrayManipulation(n, queries)
  print(result)

if __name__ == "__main__":
  main()