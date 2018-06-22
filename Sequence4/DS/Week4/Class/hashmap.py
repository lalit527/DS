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
    # if curr.next is None:
    #   if curr.key == key:
    #     self.hash[index].head = None
    # else:
    prev = None
    while curr is not None:
      if curr.key == key:
        print('found')
        if prev is None:
          print('no prev')
          self.hash[index].head = curr.next
        else:
          print('prev')
          prev.next = curr.next
        break
      prev = curr
      curr = curr.next




  def hash_function(self, data):
    return data % self.size

def main():
  H = HashMap()
  H.add(5, 'Hey')
  H.add(4, 'Ok')
  H.add(2, 'Sure')
  H.add(5, 'Hiiiii')
  H.add(21, 'Uff')
  H.delete(5)
  print(H.get(5))
  print(H.get(21))
  print(H.hash)

if __name__ == "__main__":
  main()