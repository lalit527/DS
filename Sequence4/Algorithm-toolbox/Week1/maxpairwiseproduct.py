from random import randint

def max_pairwise_product_naive(numbers):
  n = len(numbers)
  max_product = 0
  for i in range(n):
    for j in range(i + 1, n):
      max_product = max(max_product, numbers[i] * numbers[j])
  return max_product


def max_pairwise_product_fast(numbers):
  n = len(numbers)
  max1 = 0
  for i in range(1, n):
    if numbers[i] > numbers[max1]:
      max1 = i
  if max1 == 0:
    max2 = 1
  else:
    max2 = 0
  for j in range(1, n):
    if j != max1 and numbers[j] > numbers[max2]:
      max2 = j
  return numbers[max1] * numbers[max2]

def max_pairwise_product_single(numbers):
  n = len(numbers)
  max1 = numbers[0]
  max2 = float('-inf')
  for i in range(1, n):
    if max1 < numbers[i]:
      max2 = max1
      max1 = numbers[i]
    elif numbers[i] > max2:
      max2 = numbers[i]
      
  return max1 * max2


def main():
  while(True):
    n = randint(1, 1000000)
    for j in range(n):
      arr = [None] * n
      for i in range(n):
        arr[i] = randint(1, 100000)
      ans1 = max_pairwise_product_fast(arr)
      ans2 = max_pairwise_product_single(arr)
      print(arr)
      print(ans1, ans2)
      if ans1 != ans2:
        break
    break

if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product_single(input_numbers))
    main()