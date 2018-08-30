from queue import Queue

class Animal:
  def __init__(self, name):
    self.name = name
  
  def set_order(self, order):
    self.order = order
  
  def is_older_than(self, other):
    return self.order > other.order

class Dog(Animal):
  def __init__(self, name):
    super().__init__(name)

  def __str__(self):
    return "Dog: " + self.name

class Cat(Animal):
  def __init__(self, name):
    super().__init__(name)

  def __str__(self):
    return "Cat: " + self.name


class AnimalShelter:
  def __init__(self):
    self.dogs = Queue()
    self.cats = Queue()
    self.order = 0

  def enqueue(self, a):
    a.set_order(self.order)
    self.order += 1
    if type(a) == Dog.__class__:
      self.dogs.enqueue(a)
    else:
      self.cats.enqueue(a)

  def dequeue_any(self):
    if self.dogs.size == 0:
      return self.dequeue_cats()
    elif self.cats.size == 0:
      return self.dequeue_dogs()
    
    dog = self.dogs.peek()
    cat = self.cats.peek()
    if dog.is_older_than(cat):
      return self.dogs.dequeue()
    else:
      return self.cats.dequeue()
  
  def peek():
    if self.dogs.size == 0:
      return self.cats.peek()
    elif self.cats.size == 0:
      return self.dogs.peek()
    
    dog = self.dogs.peek()
    cat = self.cats.peek()
    if dog.is_older_than(cat):
      return dog
    else:
      return cat

  def dequeue_cats(self):
    return self.cats.dequeue()

  def dequeue_dogs(self):
    return self.dogs.dequeue()

animals = AnimalShelter()
animals.enqueue( Cat("Callie"))
animals.enqueue( Cat("Kiki"))
animals.enqueue( Dog("Fido"))
animals.enqueue( Dog("Dora"))
animals.enqueue( Cat("Kari"))
animals.enqueue( Dog("Dexter"))
animals.enqueue( Dog("Dobo"))
animals.enqueue( Cat("Copa"))

print(animals.dequeue_any())
print(animals.dequeue_any())
print(animals.dequeue_any())
