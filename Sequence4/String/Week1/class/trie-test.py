class Node:
  def __init__(self, label, data = None):
    self.data = data
    self.children = [None] * 26
    self.eos = False
    self.label = label
  
  # def __str__(self):
  #   return str(self.data) + str(self.children) + str(self.label)

class Trie:
  def __init__(self):
    self.root = Node(0)
    self.label = 0
  
  def get_index(self, c):
    return ord(c) - ord('A')

  def insert(self, text):
    root = self.root
    for c in text:
      i = self.get_index(c)
      if root.children[i] is None:
        # print(root.label)
        node = Node(i + 1, c)
        self.label += 1
        root.children[i] = node
      root = root.children[i]
    root.eos = True
  
  def search(self, pattern):
    root = self.root
    for c in pattern:
      i = self.get_index(c)
      root = root.children[i]
      if root is not None:
        print(str(root.label - 1) + '->' + str(root.label) + ':' + c)


  # def __str__(self):
  #   result = ''
  #   root = self.root
  #   while True:
  #     result 
  #   for i in self.root.children:
  #     result += str(i) + ' ' + '\n'
  #   return result


T = Trie()
T.insert('ATAGA')
T.insert('ATC')
T.insert('GAT')
T.search('ATAGA')
T.search('ATC')
T.search('GAT')

# TrieConstruction(Patterns):
#   Trie = graph consisiting of single node root
#   for pattern in patterns:
#     currentNode = root
#     for i = 1 to pattern:
#       currentSymbol = ith symbol of pattern
#       if there is an outgoing edge from currentNode with label currentSymbol:
#         currentNode = ending of this node 
#       else:
#         add a new node newNode to the root of trie
#         add a new edge from currentNode to newNode with label as currentSymbol
#         currentNode = newNode

#   return Trie
# TrieMatching(Text, Trie):
#   while text is nonEmpty:
#     PrefixTrieMatching(Text, Trie)
#     remove first symbol from the Text

# PrefixTrieMatching(Text, Trie):
#   symbol = first letter of Trie
#   v = root of Trie
#   while Forever:
#     if v is a leaf in Trie:
#       return pattern spelled by the path from the root to v
#     else if there is an edge(v, w) in the Trie labelled by the symbol:
#       symbol = next letter of Trie
#       v = w 
#     else output 'no match found':
#       return


