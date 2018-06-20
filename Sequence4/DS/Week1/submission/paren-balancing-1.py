# python3

import sys
class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None

class Stack:
  def __init__(self):
    self.top = None
  
  def push(self, data):
    node = Node(data)
    node.prev = self.top
    self.top = node
  
  def pop(self):
    top = self.top
    self.top = self.top.prev
    return top

  def peek(self):
    return self.top

  def isEmpty(self):
    return self.top is None

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def checkParen(text):
  s = Stack()
  for i, next in enumerate(text):
    if next == '(' or next == '[' or next == '{':
      # Process opening bracket, write your code here
      bracket = Bracket(next, i + 1)
      s.push(bracket)

    if next == ')' or next == ']' or next == '}':
      # Process closing bracket, write your code here
      if s.peek():
        data = s.pop()
        if not data.data.Match(next):
          return i + 1
      else:
        return i + 1

  if s.isEmpty():
    return 'Success'
  else:
    data = s.pop()
    return data.data.position

if __name__ == "__main__":
    text = sys.stdin.read()
    print(checkParen(text))
