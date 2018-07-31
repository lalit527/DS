# python3

def max_pairwise_product(numbers):
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

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))