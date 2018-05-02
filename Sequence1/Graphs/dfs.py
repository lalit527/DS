from collections import deque

def dfs(graph, start):
    visited = set()
    stack = deque()
    stack.append(start)

    while len(stack) > 0:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:
                stack.append(i)
    return visited

def dfs_rec(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    for i in graph[start] - visited:
        dfs_rec(graph, i, visited)
    
    return visited
    

    


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(dfs_rec(graph, 'A'))
        