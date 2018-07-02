def shift_down(A, size, index):
    left = 2 * index + 1
    right = 2 * index + 2
    max_index = index
    if left <= size and A[left] > A[max_index]:
      max_index = left

    if right <= size and A[right] > A[max_index]:
      max_index = right

    if max_index != index:
      A[max_index], A[index] = A[index], A[max_index]
      shift_down(A, size, max_index)

def build_heap(A, size):
  for i in range(size//2, -1, -1):
    shift_down(A, size, i)

def heap_sort(A):
  size = len(A) - 1
  build_heap(A, size)
  print(A)
  for i in range(size, -1, -1):
    A[0], A[i] = A[i], A[0]
    shift_down(A, i-1, 0)

if __name__ == '__main__':
  arr = [9, 5, 7, 3, 2, 1]
  heap_sort(arr)
  print(arr)
