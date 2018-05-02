class Graph:
    def __init__(self):
        self.nodes = set()
        self.connections = {}

    def add_node(self, node):
        self.nodes.add(node)
    
    def contains(self, v):
        return v in self.connections.keys()

    def connect(self, start, end, weight = 1):
        if start not in self.connections:
            self.connections[start] = { end: weight }
        else:
            self.connections[start][end] = weight

        if end not in self.connections:
            self.connections[end] = { start: end }

    def get_node(self):
        return self.connections.keys()

    def get_start_vertex(self):
        candidates = set(self.get_node())
        for end in self.connections.values():
            for k in end.keys():
                if k in candidates:
                    candidates.remove(k)
        return candidates

    def paint(self):
        print(self.connections)
