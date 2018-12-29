num = [1, 2, 3, 4, 5, 6]
square = [1, 4, 9, 16, 25, 36]
cube = [1, 8, 27, 64, 125, 216]

for item in zip(num, square, cube):
  print(item)

all_num = [num, square, cube]

for item in zip(all_num[0], all_num[1], all_num[2]):
  print(item)