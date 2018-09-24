## Memoized Version
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
  stack_map = [0] * (len(boxes))
  for i in range(len(boxes)):
    height = _create_stack(boxes, i, stack_map)
    max_height = max(height, max_height)
  return max_height

def _create_stack(boxes, index, stack_map):
  if index < len(boxes) and stack_map[index] > 0:
    return stack_map[index]
  bottom = boxes[index]
  max_height = 0
  for i in range(index + 1, len(boxes)):
    if boxes[i].can_be_above(bottom):
      height = _create_stack(boxes, i, stack_map)
      max_height = max(height, max_height)
  max_height += bottom.height
  stack_map[index] = max_height
  return max_height