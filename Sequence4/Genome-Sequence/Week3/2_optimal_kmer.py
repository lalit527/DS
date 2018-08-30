# uses python3
import sys

def optimal_kmer(n , reads):
  k_mers = set()
  for read in reads:
    for i in range(0, len(read) - n+1):
      k_mers.add(read[i:i+n])
  prefixes = set()
  suffixes = set()
  for kmer in k_mers:
    prefixes.add(kmer[:-1])
    suffixes.add(kmer[1:])
  return prefixes == suffixes

if __name__ == "__main__":
  reads = []
  for i in range(5):
    read = sys.stdin.readline().strip()
    reads.append(read)
  
  for n in range(len(reads[2]), 1, -1):
    if optimal_kmer(n , reads):
      print(n)
      break