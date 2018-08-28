class FixedStack:
  def __init__(self, stack_size):
    self.num_of_stacks = 3
    self.array = [None] * (stack_size * self.num_of_stacks)
    self.size = [0] * stack_size
    self.stack_size = stack_size
  
  def push(self, data, stack_num):
    if self.is_full(stack_num):
      raise Exception(str(stack_num) + ':- Stack is Full')
    
    self.size[stack_num - 1] += 1
    self.array[self.index_of_top(stack_num)] = data

  def pop(self, stack_num):
    if self.is_empty(stack_num):
      raise Exception(str(stack_num) + ':- Stack is Empty')
    
    top = self.index_of_top(stack_num)
    value = self.array[top]
    self.array[top] = None
    self.size[stack_num] -= 1
    return value

  def is_empty(self, stack_num):
    return self.size[stack_num - 1] == 0

  def is_full(self, stack_num):
    return self.size[stack_num - 1] == self.stack_size

  def index_of_top(self, stack_num):
    offset = stack_num * self.stack_size
    size = self.size[stack_num]
    print('Issue', offset, size)
    return offset + size - 1


    

FS = FixedStack(10)
FS.push(5, 1)
FS.push(7, 1)
FS.push(11, 2)
FS.push(17, 2)
FS.push(13, 3)
FS.push(8, 3)
print(FS.pop(3))