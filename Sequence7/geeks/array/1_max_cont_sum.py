import sys

def kadane_sum(arr):
  max_so_far = max_ending_here = arr[0]

  for i, ele in enumerate(arr[1:]):
    max_ending_here = max(ele, max_ending_here + ele)
    max_so_far = max(max_ending_here, max_so_far)
  
  return max_so_far

def kadane_sum_indx(arr):
  start_index = end_index = 0
  max_so_far = max_ending_here = arr[0]

  for i, ele in enumerate(arr[1:]):
    if ele > max_ending_here + ele:
      max_ending_here = ele
      max_so_far = ele
      start_index = end_index = (i + 1)
    else:
      max_ending_here += ele
      end_index = (i + 1)
      max_so_far = max(max_ending_here, max_so_far)
  print(start_index, end_index)
  print(max_so_far)


def main():
  n = int(sys.stdin.readline())
  data = []
  for _ in range(n):
    c = int(sys.stdin.readline())
    tmp = []
    tmp.extend(sys.stdin.readline().split())
    tmp = list(map(lambda x: int(x), tmp))
    data.append(tmp)
    kadane_sum_indx(tmp)
  print(data)
  
if __name__ == "__main__":
  main()
