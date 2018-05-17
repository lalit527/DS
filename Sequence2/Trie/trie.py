class Node:
  def __init__(self, data = None):
    self.data = data
    self.isEndOfWord = False
    self.children = [None] * 26

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, c):
    self._insert(self.root, c)

  def char_to_index(self, c):
    return ord(c) - ord('a')

  def _insert(self, root, s):
    level = 0
    length = len(s)
    pCrawl = root
    for level in range(length):
      index = self.char_to_index(s[level])
      if not pCrawl.children[index]:
        pCrawl.children[index] = Node()
      pCrawl = pCrawl.children[index]
    pCrawl.isEndOfWord = True

  def search(self, s):
    pCrawl = self.root
    length = len(s)
    for level in range(length):
      index = self.char_to_index(s[level])
      if not pCrawl.children[index]:
        return False
      pCrawl = pCrawl.children[index]
    return pCrawl is not None and pCrawl.isEndOfWord

  def delet(self, s):
    length = len(s)
    self._traverse(self.root, s, 0, length)
  
  def _traverse(self, root, s, level, length):
    if root:
      _traverse(root, buffer)

def main():
  keys = ["the","a","there","anaswe","any",
          "by","their"]
  output = ["Not present in trie",
            "Present in tire"]
  t = Trie()

  for key in keys:
      t.insert(key)

  # Search for different keys
  print("{} ---- {}".format("the",output[t.search("the")]))
  print("{} ---- {}".format("these",output[t.search("these")]))
  print("{} ---- {}".format("their",output[t.search("their")]))
  print("{} ---- {}".format("thaw",output[t.search("thaw")]))
 
if __name__ == '__main__':
    main()