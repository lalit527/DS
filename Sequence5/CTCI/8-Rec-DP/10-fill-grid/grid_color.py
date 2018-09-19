def paint_fill(screen, row, col, ncolor):
  if screen[row][col] == ncolor:
    return False
  else:
    return paint_fill_screen(screen, row, col, screen[row][col], ncolor)

def paint_fill_screen(screen, row, col, ocolor, ncolor):
  if row < 0 or row >= len(screen) or col < 0 or col >= len(screen[0]):
    return False
  if screen[row][col] == ocolor:
    screen[row][col] = ncolor
    paint_fill_screen(screen, row - 1, col, ocolor, ncolor)
    paint_fill_screen(screen, row + 1, col, ocolor, ncolor)
    paint_fill_screen(screen, row, col - 1, ocolor, ncolor)
    paint_fill_screen(screen, row, col + 1, ocolor, ncolor)
  return True

screen = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

paint_fill(screen, 2, 2, 1)
print(screen)