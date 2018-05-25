from counting import countSort

def radix(arr):
  mx = max(arr)
  b = [None] * len(arr)
  exp = 1
  while mx/exp > 0:
      countSort(arr,b, exp)
      exp *= 10

  print(exp)


def main():
  arr = [2,5,3,0,2,3,0,3]
  radix(arr)

if __name__ == '__main__':
  main()