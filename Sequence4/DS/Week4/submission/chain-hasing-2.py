# python3

class Node:
  def __init__(self, key):
    self.key = key
    self.next = None

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [None] * bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return (ans % self.bucket_count + self.bucket_count) % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # self.write_chain(cur for cur in reversed(self.elems)
            #             if self._hash_func(cur) == query.ind)
            data = self.elems[query.ind]
            result = []
            while data is not None:
              result.append(data.key)
              data = data.next
            self.write_chain(result)
        else:
            if query.type == 'find':
                index = self._hash_func(query.s)
                data = self.elems[index]
                found = False
                while data is not None:
                  if data.key == query.s:
                    found = True
                    break
                  data = data.next
                if found:
                  self.write_search_result(True) 
                else:
                  self.write_search_result(False)
            elif query.type == 'add':
                node = Node(query.s)
                index = self._hash_func(query.s)
                data = self.elems[index]
                found = False
                while data is not None:
                  if data.key == query.s:
                    found = True
                    break
                  data = data.next
                if not found:
                  data = self.elems[index]
                  self.elems[index] = node
                  node.next = data 
            elif query.type == 'del':
                index = self._hash_func(query.s)
                data = self.elems[index]
                prev = None
                while data is not None:
                  if data.key == query.s:
                    if prev is None:
                      self.elems[index] = data.next
                    else:
                      prev.next = data.next
                  prev = data
                  data = data.next
            elif query.type == 'show':
              self.checkTable()

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
    
    def checkTable(self):
      for i in self.elems:
        print(i.key if i else None)

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
