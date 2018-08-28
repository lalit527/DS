# uses python3

from collections import defaultdict

def genome_kmer(reads):
  default_reads = reads

  reads_list = []

  for _ in range(default_reads):
    reads_list.append(input())
  adj = defaultdict(list)
  id = 0
  for read in reads_list:
    adj[read[:-1]].append((read[1:], id))
    id += 1

  path = [reads_list[0][:-1]]
  already_visited = set()

  while len(already_visited) < len(reads_list):
    for i, node in enumerate(path):
      all_visited = True
      for next in adj[node]:
        if next[1] not in already_visited:
          all_visited = False
          break
      if all_visited:
        continue
      new_cycle = [node]
      current = node
      find_next = True
      while find_next:
        find_next = False
        for next in adj[current]:
          if next[1] not in already_visited:
            already_visited.add(next[1])
            new_cycle.append(next[0])
            current = next[0]
            find_next = True
            break
      break
    path = path[:i] + new_cycle + path[i+1:]
  cycle = ""

  for node in path:
    cycle += node[0]
  print(cycle[:-1])

if __name__ == "__main__":
  genome_kmer(5396)