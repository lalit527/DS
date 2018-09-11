from enum import Enum

class State(Enum):
  COMPLETE = 1
  PARTIAL = 2
  BLANK = 3


class Project:
  def __init__(self, n):
    self.state = State.BLANK
    self.children = []
    self.map = dict()
    self.name = n

  def add_neighbor(self, node):
    if node.name not in self.map:
      self.children.append(node)
      self.map[node.name] = node

class Graph:
  def __init__(self):
    self.nodes = []
    self.map = dict()

  def get_create_node(self, name):
    if name not in self.map:
      node = Project(name)
      self.nodes.append(node)
      self.map[name] = node
    
    return self.map[name]

  def add_edge(self, start_node, end_node):
    start = self.get_create_node(start_node)
    end = self.get_create_node(end_node)
    start.add_neighbor(end)

def build_graph(projects, dependencies):
  graph = Graph()
  for project in projects:
    graph.get_create_node(project)
  
  for dependency in dependencies:
    first = dependency[0]
    second = dependency[1]
    graph.add_edge(first, second)
  
  return graph

def do_DFS(project, stack):
  if project.state == State.PARTIAL:
    return False
  
  if project.state == State.BLANK:
    project.state = State.PARTIAL
    children = project.children
    for child in children:
      if not do_DFS(child, stack):
        return False
    
    project.state = State.COMPLETE
    stack.append(project)
  return True

def order_projects(projects):
  stack = []
  for project in projects:
    if project.state == State.BLANK:
      if not do_DFS(project, stack):
        return None

  return stack

def find_build_order(projects, dependencies):
  graph = build_graph(projects, dependencies)
  return order_projects(graph.nodes)

def build_order_wrapper(projects, dependencies):
  build_order = find_build_order(projects, dependencies)
  if build_order is None:
    return None
  
  buil_order_string = convert_to_stringlist(build_order)
  return buil_order_string


def convert_to_stringlist(projects):
  build_order = [''] * len(projects)
  for i in range(len(projects)):
    build_order[i] = projects.pop().name
  return build_order



def main():
  projects = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
  dependencies = [
          ("a", "b"),
          ("b", "c"),
          ("a", "c"),
          ("a", "c"),
          ("d", "e"),
          ("b", "d"),
          ("e", "f"),
          ("a", "f"),
          ("h", "i"),
          ("h", "j"),
          ("i", "j"),
          ("g", "j")
  ]

  build_order = build_order_wrapper(projects, dependencies)
  if build_order is None:
    print("Circular Dependencies")
  else:
    for s in build_order:
      print(s)

if __name__ == "__main__":
  main()