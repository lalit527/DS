class Node:
  def __init__(self, key = None, value = None):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None

class HashTable:
  def hash(self, key):
    return ord(str(key)) % self.size

  def chaining(self):
    pass

  def __init__(self, size = 16):
    self.size = size
    self.key = [None] * size
    for i in range(size):
      self.key[i] = Node()

  def put(self, key, value):
    slot = self.hash(key)
    head = self.key[slot]
    while head.next is not None:
      if head.key == key:
        head.value = value
        return
      head = head.next
    print('Key--', head.key)
    node = Node(key, value)
    head.next = node  
    node.prev = head

  def get(self, key):
    slot = self.hash(key)
    head = self.key[slot]
    while head is not None:
      if head.key == key:
        return head.value
      head = head.next
    return Exception("No Key")

  def delete(self, key):
    slot = self.hash(key)
    head = self.key[slot]
    while head is not None:
      if head.key == key:
        head.prev.next = head.next if head else None
        return True
      head = head.next
    return False

H = HashTable()
H.put('a', 5)    
H.put(1, 6)    
print(H.get('a'))
print(H.get(1))
print(H.delete(1))
print(H.get(1))
# print(H.data)
# print(H.key)
