# python3
import sys
from random import randint

DEFAULT_READS_NUMBER = 1618
DEFAULT_MIN_OVERLAP_LENGTH = 70
LENGTH_OF_READ = 100

class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.indexes = []

class PrefixTrie(object):
  def __init__(self):
	  self.root = TrieNode()

  def add_prefix(self, string, index):
    for end in range(DEFAULT_MIN_OVERLAP_LENGTH, len(string)):
      reversed_prefix = string[:end][::-1]
      node = self.root
      for char in reversed_prefix:
        if char not in node.children:
          node.children[char] = TrieNode()
        node = node.children[char]
      node.indexes.append(index)

  def match(self, string):
    adj = []
    node = self.root
    n = 0
    for c  in string[::-1]:
      if c not in node.children:
        break
      node = node.children[c]
      n += 1
      if n >= DEFAULT_MIN_OVERLAP_LENGTH and node.indexes:
        for index in node.indexes:
          adj.append((index, n))
    return adj
  
  



class GenomeAssmbling:
  def __init__(self):
    data = self.read_data()
    adj = self.generate_overlap_graph(data)
    path = self.hamiltonian_path(adj)
    genome = self.assemble(data)
    print(genome)
  
  def read_data(self):
    # data = list(set(sys.stdin.read().strip().split()))
    # print(data)
    data = []
    alpha = ['A', 'C', 'G', 'T']
    for i in range(DEFAULT_READS_NUMBER):
      r = ""
      for _ in range(5):
        r += alpha[randint(0, 3)]
      data.append(r)
    return data
  


  def generate_overlap_graph(self, data):
    prefic_trie = PrefixTrie()
    for i, d in enumerate(data):
      prefic_trie.add_prefix(d, i)
    adj = [[] for _ in range(len(data))]
    for i, d in enumerate(data):
      adj[i] = prefic_trie.match(d)
    for a in adj:
      a.sort(key=lambda x: x[1], reverse=True)
    return adj

  def hamiltonian_path(self, adj):
    cur = 0
    added = set([0])
    path = [(0, 0)]
    while len(added) < len(adj):
      for i, link in enumerate(adj[cur]):
        if link[0] not in added:
          added.add(link[0])
          cur = link[0]
          path.append(link)
          break
    return path

  def string_overlap_value(self, s, t):
    for i in range(LENGTH_OF_READ, 0, -1):
      if s[LENGTH_OF_READ-i:] == t[:i]: 
        return i
    return 0

  def assemble(self, data):
    genome = ""
    for node in path:
      genome += data[node[0]][node[1]:]
    genome = genome[:string_overlap_value(data[path[-1][0]], reads[0])]
    return genome
  

if __name__ == '__main__':
  GenomeAssmbling()