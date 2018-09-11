class Project:
  def __init__(self, n):
    self.children = []
    self.map = dict()
    self.name = n
    self.dependencies = 0

  def add_neighbor(self, node):
    if node.name not in self.map:
      self.children.append(node)
      self.map[node.name] = node
      node.increment_dependencies()
  
  def increment_dependencies(self):
    self.dependencies += 1
  
  def decrement_dependencies(self):
    self.dependencies -= 1

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

  def get_nodes(self):
    return self.nodes


def build_graph(projects, dependencies):
  graph = Graph()
  for project in projects:
    graph.get_create_node(project)
  
  for dependency in dependencies:
    first = dependency[0]
    second = dependency[1]
    graph.add_edge(first, second)
  
  return graph

def add_nondependent(order, projects, offset):
  for project in projects:
    if project.dependencies == 0:
      order[offset] = project
      offset += 1
  return offset

def order_projects(projects):
  order = [None] * len(projects)
  end_of_list = add_nondependent(order, projects, 0) 
  to_be_processed = 0
  while to_be_processed < len(order):
    current = order[to_be_processed]

    if current is None:
      return None

    children = current.children
    for child in children:
      child.decrement_dependencies()
    end_of_list = add_nondependent(order, children, end_of_list)
    to_be_processed += 1
  return order

def find_build_order(projects, dependencies):
  graph = build_graph(projects, dependencies)
  return order_projects(graph.get_nodes())

def build_order_wrapper(projects, dependencies):
  build_order = find_build_order(projects, dependencies)
  if build_order is None:
    return None
  
  buil_order_string = convert_to_stringlist(build_order)
  return buil_order_string


def convert_to_stringlist(projects):
  build_order = [''] * len(projects)
  for i in range(len(projects)):
    build_order[i] = projects[i].name
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