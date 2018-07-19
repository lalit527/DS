#Uses python3
import sys
from collections import OrderedDict

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

  def insert(self, patterns):
    for pattern in patterns:
      self._insert(pattern)

  def _insert(self, text):
    root = self.root
    for c in text:
      i = self.get_index(c)
      # print(c, i, root.data)
      if root.children[i] is None:
        # print(root.label)
        node = Node(self.label + 1, c)
        self.label += 1
        root.children[i] = node
      else:
        pass
      root = root.children[i]
    root.eos = True
  
  def search(self, patterns):
    D = OrderedDict()
    for pattern in patterns:
      self._search(pattern, D)
    for key, value in D.items():
      print(key+ ':' + value)

  def _search(self, pattern, D):
    root = self.root
    prev = None
    for c in pattern:
      i = self.get_index(c)
      prev = root
      root = root.children[i]
      if root is not None:
        D[str(prev.label) + '->' + str(root.label)] = c

def _prefixTrieMatch(text, trie, index, s):
  root = trie.root
  for c in text:
    i = trie.get_index(c)
    if root.children[i] is not None and root.children[i].eos:
      s[index] = True
    elif root.children[i] is not None:
      root = root.children[i]
    else:
      return


def prefixTrieMatch(text, trie):
  i = 0
  S = OrderedDict()
  while len(text) > 0:
    _prefixTrieMatch(text, trie, i, S)
    i += 1
    text = text[1:]
  for key in S.keys():
    print(key, end = ' ')
  print('')

if __name__ == '__main__':
    # n = sys.stdin.read()
    # text = sys.stdin.read()
    # print(text)
    # T = Trie()
    # T._insert(text)
    text, n, *patterns = sys.stdin.read().split()
    # print(text)
    T = Trie()
    T.insert(patterns)
    prefixTrieMatch(text, T)
#     T = Trie()
#     tree = build_trie(patterns)
#     for node in tree:
#         for c in tree[node]:
#             print("{}->{}:{}".format(node, tree[node][c], c))


# for pattern in 
# T.insert('ATAGA')
# T.insert('ATC')
# T.insert('GAT')
# T.search('ATAGA')
# T.search('ATC')
# T.search('GAT')

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


