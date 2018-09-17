from collections import deque

class Tower:
  def __init__(self, i):
    self.disks = deque()
    self.index = i
  
  def add(self, d):
    if len(self.disks) > 0 and self.disks[-1] <= d:
      print("Error")
    else:
      self.disks.append(d)

  def move_top(self, t):
    top = self.disks.pop()
    t.add(top)

  def print_move(self):
    print("Contents of Tower {} moved :- {}".format(self.index, self.disks))

  def move_disk(self, n, destination, buffer):
    if n > 0:
      tag = "move_ {} _disks_from_ {} _to_ {} _with_buffer_ {}".format(self.index, destination.index, buffer.index)
      print("< {} >".format(tag))
      self.move_disk(n - 1, buffer, destination)
      print("<move_top_from_" + self.index + "_to_" + destination.index + ">")
      print("<before>")
      print("<source_print>")
      this.print_move()
      print("</source_print>")
      print("<destination_print>")
      destination.print()
      print("</destination_print>")
      print("</before>")

      self.move_top(destination)

      print("<after>")
      print("<source_print>")
      this.print_move()
      print("</source_print>")
      print("<destination_print>")
      print()
      print("</destination_print>")
      print("</after>")
      print("</move_top_from_" + self.index + "_to_" + destination.index + ">")

      buffer.move_disk(n - 1, destination, self)

      print("< {} >".format(tag))



if __name__ == "__main__":
  n = 4
  tower = []
  for i in range(3):
    tower.append(Tower(i))

  for i in range(n - 1, -1, -1):
    tower[0].add(i)

  tower[0].move_disk(n, tower[2], tower[1])