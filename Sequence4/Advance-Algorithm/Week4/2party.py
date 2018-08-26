#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
    
    def __str__(self):
        # print(self)
        result = ",".join(str(c) for c in self.children)
        return str(self.weight) + "->" + result


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent, s):
    print(vertex)
    if s[vertex] == -1:
        print(tree, vertex, parent)
        if len(tree[vertex].children) == 0:
            s[vertex] = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for child in tree[vertex].children:
                if child == parent:
                    continue
                for w in tree[child].children:
                    if w != vertex:
                        m1 += dfs(tree, w, child, s)

            m0 = 0
            for child in tree[vertex].children:
                if child != parent:
                    m0 += dfs(tree, child, vertex, s)
            s[vertex] = max(m0, m1)
        # This is a template function for processing a tree using depth-first search.
        # Write your code here.
        # You may need to add more parameters to this function for child processing.
    return s[vertex]

def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    sum = [-1] * size
    result = dfs(tree, 0, -1, sum)
    # You must decide what to return.
    return result


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
