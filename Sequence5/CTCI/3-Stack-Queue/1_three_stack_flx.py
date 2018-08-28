class StackInfo:
    def __init__(self, start, capacity, num_of_stacks):
      self.start = start
      self.capacity = capacity
      self.total_capacity = (num_of_stacks * capacity)

    
    def is_within_stack(self, index):
      if index < 0 or index >= self.total_capacity:
        return False
      
      con_index = index + self.capacity if index < self.start else index
      end = self.start + self.capacity
      return self.start <= con_index and con_index < end
    
    def last_capacity_index(self):
      return adj

class MultiStack:

  def __init__(self, num_of_stacks, default_size):
    self.info = [None] * num_of_stacks
    for i in range(num_of_stacks):
      self.info[i] = MultiStack.StackInfo(default_size * i, default_size, num_of_stacks)
    self.values = [0] * (num_of_stacks * default_size)
    

  

    

FS = FixedStack(10)
FS.push(5, 1)
FS.push(7, 1)
FS.push(11, 2)
FS.push(17, 2)
FS.push(13, 3)
FS.push(8, 3)
print(FS.pop(3))