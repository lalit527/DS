# python3
import sys
from random import randint

DEFAULT_READS_NUMBER = 5
DEFAULT_MIN_OVERLAP_LENGTH = 0
LENGTH_OF_READ = 0

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
  
  
def string_overlap_value(s, t):
  for i in range(LENGTH_OF_READ, 0, -1):
    if s[LENGTH_OF_READ - i:] == t[:i]: 
      return i
  return 0

def generate_overlap_graph(reads):
  prefix_trie = PrefixTrie()
  for i, read in enumerate(reads):
    prefix_trie.add_prefix(read, i)
  adj = [[] for _ in range(len(reads))]
  for i, read in enumerate(reads):
    adj[i] = prefix_trie.match(read)
  for l in adj:
    l.sort(key = lambda x: x[1], reverse = True)
  return adj

def build_hamiltonian_path(adj):
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

def assemble(path, reads):
  genome = ""
  for node in path:
    genome += reads[node[0]][node[1]:]
  genome = genome[:-string_overlap_value(reads[path[-1][0]], reads[0])]
  return genome

class GenomeAssmbling:
  def __init__(self):
    self.read_data()
  
  def read_data(self):
    reads = []
    for i in range(DEFAULT_READS_NUMBER):
      reads.append(input())
    reads = list(set(reads))
    adj = generate_overlap_graph(reads)
    path = build_hamiltonian_path(adj)
    genome = assemble(path, reads)
    print(genome)

if __name__ == '__main__':
  GenomeAssmbling()