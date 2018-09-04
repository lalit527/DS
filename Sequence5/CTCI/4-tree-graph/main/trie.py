class Node:
  def __init__(self, data = None):
    self.data = data
    self.isEndOfWord = False
    self.children = [None] * 26

  def is_it_free(self):
    for i in self.data:
      if self.children is not None:
        return False
    return True

class Trie:
  def __init__(self):
    self.root = Node()

  def char_to_index(self, c):
    return ord(c) - ord('a')

  def insert(self, s):
    self._insert(self.root, s)

  def _insert(self, root, s):
    level = 0
    n = len(s)
    crawler = root
    for level in range(n):
      index = self.char_to_index(s[level])
      if not crawler.children[index]:
        crawler.children[index] = Node(s[level])
      crawler = crawler.children[index]
    crawler.isEndOfWord = True

  def search(self, s):
    crawler = self.root
    n = len(s)
    for level in range(n):
      index = self.char_to_index(s[level])
      if crawler.children[index] is None:
        return False
      crawler = crawler.children[index]
    return crawler is not None and crawler.isEndOfWord


  def delete(self, s):
    n = len(s)
    if n > 0:
      self._delete(self.root, s, 0, n)

  def _delete(self, root, s, level, n):
    if root:
      if level == n:
        if root.isEndOfWord:
          root.isEndOfWord = False
        return root.is_it_free()

      else:
        index = self.char_to_index(s[level])
        if self._delete(root.children[index], s, level + 1, n):
          root.children[index] = None

          return root.isEndOfWord and root.is_it_free()
      
    return False

def main():
  keys = ["the","a","there","anaswe","any",
          "by","their"]
  output = ["Not present in trie",
            "Present in tire"]
  t = Trie()

  for key in keys:
      t.insert(key)

  t.delete("the")
  # Search for different keys
  print("{} ---- {}".format("the",output[t.search("the")]))
  print("{} ---- {}".format("these",output[t.search("these")]))
  print("{} ---- {}".format("their",output[t.search("their")]))
  print("{} ---- {}".format("thaw",output[t.search("thaw")]))
 
if __name__ == '__main__':
    main()