class Node:
  def __init__(self):
    self.children = [None] * 26
    self.isEndOfList = False

  def isFreeNode(self):
    for i in self.children:
      if self.children is not None:
        return False
    return True
  
class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, s):
    pCrawl = self.root
    length = len(s)
    for level in range(length):
      index = self.char_to_index(s[level])
      if not pCrawl.children[index]:
        pCrawl.children[index] = Node()
      pCrawl = pCrawl.children[index]

    pCrawl.isEndOfList = True
  
  def char_to_index(self, c):
    return ord(c) - ord('a')

  def search(self, s):
    pCrawl = self.root
    length = len(s)
    for level in range(length):
      index = self.char_to_index(s[level])

      if not pCrawl.children[index]:
        return False
      
      pCrawl = pCrawl.children[index]

    return pCrawl is not None and pCrawl.isEndOfList

  def delete(self, s):
    length = len(s)
    if length > 1:
      self._delete(self.root, s, 0, length)

  def _delete(self, root, s, level, length):
    if root:
      if level == length:
        if root.isEndOfList:
          root.isEndOfList = False
        return root.isFreeNode()
      else:
        index = self.char_to_index(s[level])
        if self._delete(root.children[index], s, level + 1, length):
          root.children[index] = None
        return root.isEndOfList and root.isFreeNode()
    return False

  def autoSuggestion(prefix):
    return _autoSuggestion(self.root, prefix)
  
  def _autoSuggestion(self, root, prefix):
    if root.isEndOfList:
      print(prefix)
    
    if root.isFreeNode():
      return
    
    for i in range(26):
      if root.children[i]:
        prefix = prefix + chr(97 + i)
        self._autoSuggestion(root.children[i], prefix)
        prefix = prefix[:-1]

  def printAutoSuggestions(self, root, s):
    pCrawl = root
    level = 0
    length = len(s)
    for i in range(length):
      index = self.char_to_index(s[i])
      if not pCrawl.children[index]:
        return 0
      
      pCrawl = pCrawl.children[index]
    
    isWord = pCrawl.isEndOfList
    isLast = pCrawl.isFreeNode()
    if isWord and isLast:
      print(s)
    
    if not isLast:
      prefix = s
      self._autoSuggestion(pCrawl, prefix)
      return 1




def main():
  keys = ["hello","dog","hell","cat","a",
          "hel","cat","help","help","helps","helping"]
  output = ["Not present in trie",
            "Present in tire"]
  t = Trie()

  for key in keys:
      t.insert(key)

  com = t.printAutoSuggestions(t.root, "hel")
 
if __name__ == '__main__':
    main()