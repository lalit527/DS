def tower_hanoi(n, origin, destination, buffer):
  if n <= 0:
    return
  
  tower_hanoi(n - 1, origin, buffer, destination)
  move_top(n, origin, destination)
  tower_hanoi(n - 1, buffer, destination, origin)

def move_top(n, origin, destination):
  print("Disk, {}:- move from origin {} to destination {}".format(n, origin, destination))

n = 4
tower_hanoi(n, 'A', 'C', 'B')