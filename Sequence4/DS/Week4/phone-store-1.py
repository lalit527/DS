# python3

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

    return "not found"

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


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

def process_queries(queries):
  # for cur_query in queries:
  n = len(queries)
  H = HashMap(n)
  result = []
  for cur_query in queries:
    if cur_query.type == 'add':
      H.add(cur_query.number, cur_query.name)
    elif cur_query.type == 'del':
      H.delete(cur_query.number)
    elif cur_query.type == 'find':
      result.append(H.get(cur_query.number))
  return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

