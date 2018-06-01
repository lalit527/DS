class HashMapBase:
  def hash(self, key):
    return ord(str(key)) % self.size
  
  def linerProbing(self, oldHash):
    return (oldHash + 1) % self.size

  def __init__(self, size = 16):
    self.size = size
    self.data = [None] * size
    self.key = [None] * size
  
  def put(self, key, value):
    slot = self.hash(key)
    if self.key[slot] == None:
      self.key[slot] = key
      self.data[slot] = value
    elif self.key[slot] == key:
      self.data[slot] = value
    else:
      nextSlot = slot
      while True:
        nextSlot = self.linerProbing(nextSlot)
        if self.key[nextSlot] == None:
          self.key[nextSlot] = key
          self.data[nextSlot] = value
          break
        elif self.key[nextSlot] == key:  
          self.data[nextSlot] = value
          break
        
        nextSlot += 1
        if nextSlot == slot:
          return Exception("No More Space")
          break
          

  def get(self, key):
    slot = self.hash(key)
    if self.key[slot] == key:
      return self.data[slot]
    nextSlot = slot
    while True:
      nextSlot = self.linerProbing(nextSlot)
      if self.key[nextSlot] == key:
        return self.data[nextSlot]
      nextSlot += 1

      if nextSlot == slot:
        return Exception("No Data Found")
        break;
      
  def delete(self, key):
    slot = self.hash(key)
    if self.key[slot] == key:
      self.data[slot] = None
      self.key[slot] = None
      return True
    nextSlot = slot
    while True:
      nextSlot = self.linerProbing(nextSlot)
      if self.key[nextSlot] == key:
        self.data[nextSlot] = None
        self.key[nextSlot] = None
        return True
      nextSlot += 1

      if nextSlot == slot:
        return Exception("No Data Found")
        break;

H = HashMapBase()
H.put('a', 5)    
H.put(1, 6)    
print(H.get('a'))
print(H.get(1))
print(H.delete(1))
print(H.data)
print(H.key)
