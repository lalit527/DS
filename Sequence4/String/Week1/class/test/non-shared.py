#!/usr/bin/env python
# The data structure suffix tree is from https://github.com/kvh/Python-Suffix-Tree

import sys
from suffixtree import SuffixTree


def main():

    patterns = sys.stdin.read().split()
    seq_1 = patterns[0] + "#"
    seq_2 = patterns[1] + "$"

    result = find_shortest_nonshared_substring(seq_1, seq_2)
    print(result)


def find_shortest_nonshared_substring(seq_1, seq_2):
    st = SuffixTree(seq_2)
    
    for k in range(2, len(seq_1) + 1):
        shared = True
        for kmer in generate_kmers(seq_1, k):
            if not st.has_substring(kmer):
                shared = False
                break
        if not shared:
            return kmer


def generate_kmers(sequence, k):
    for i in range(len(sequence) - k + 1):
        yield sequence[i: i + k]


if __name__ == '__main__':
    main()