class Box:
  def __init__(self, l, w, h):
    self.length = l
    self.width = w
    self.height = h
  def can_be_under(self, box):
    if self.width > box.width and self.height > box.height and self.length > box.length:
      return True
    return False
  def can_be_above(self, box):
    if self.width < box.width and self.height < box.height and self.length < box.length:
      return True
    return False


def create_stack(boxes):
  boxes.sort(key= lambda x: x.height)
  max_height = 0
  for i in range(len(boxes)):
    height = _create_stack(boxes, i)
    max_height = max(height, max_height)
  return max_height

def _create_stack(boxes, index):
  bottom = boxes[index]
  max_height = 0
  for i in range(index + 1, len(boxes)):
    height = _create_stack(boxes, i)
    max_height = max(max_height, height)
  max_height += bottom.height
  return max_height

boxList = [Box(6, 4, 4), Box(8, 6, 2), Box(5, 3, 3), Box(7, 8, 3), Box(4, 2, 2), Box(9, 7, 3)]
height = create_stack(boxList)