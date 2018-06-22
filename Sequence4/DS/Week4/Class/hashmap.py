class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None

class HashNode:
  def __init__(self):
    self.head = None
    self.tail = None

class HashMap:
  def __init__(self, size=16):
    self.size = size
    self.hash = [HashNode()] * size


  def add(self, key, value):
    node = Node(key, value)
    if type(key) is str:
      index = self.hash_str_fn(key)
    elif type(key) is int:
      index = self.hash_function(key)

    head =  self.hash[index].head
    if head is None:
      self.hash[index].head = node
    else:
      prev = None
      while head is not None:
        if head.key == key:
          head.value = value
          break       
        prev = head
        head = head.next
      if head is None:
        prev.next = node

  def get(self, key):
    if type(key) is str:
      index = self.hash_str_fn(key)
    elif type(key) is int:
      index = self.hash_function(key)
    head =  self.hash[index].head
    while head is not None:
      if head.key == key:
        return head.value
      head = head.next

    return Exception("Key not present")

  def delete(self, key):
    index = self.hash_function(key)
    curr = self.hash[index].head
    prev = None
    while curr is not None:
      if curr.key == key:
        if prev is None:
          self.hash[index].head = curr.next
        else:
          prev.next = curr.next
        break
      prev = curr
      curr = curr.next

  def hash_function(self, data):
    a = 34
    b = 2
    index = (a * data + b)
    p = len(str(index)) - 1
    p = 10 ** p + 19
    index %= p
    return index % self.size

  def hash_str_fn(self, data):
    h = 0
    n = len(data)
    x = 31
    p = 119
    for i in range(n-1, -1, -1):
      h += ((h * x) + ord(data[i]))
      h %= p
    return h % self.size


def main():
  H = HashMap()
  H.add(5, 'Hey')
  H.add(4, 'Ok')
  H.add(2, 'Sure')
  H.add('Hey', 'Sure')
  print(H.get(5))
  H.add(5, 'Hiiiii')
  H.add(21, 'Uff')
  print(H.get(5))
  H.delete(5)
  print(H.get(5))
  print(H.get(21))
  print(H.get('Hey'))

if __name__ == "__main__":
  main()