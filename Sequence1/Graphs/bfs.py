from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()
    queue.append(start)

    while len(queue) > 0:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:
                queue.append(i)
    return visited

def bfs_rec(graph, start):
    

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(bfs(graph, 'A'))
        
