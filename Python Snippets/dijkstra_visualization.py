from math import inf

class Node:
  def __init__(self):
    self.distance = inf
    self.parent = None
    self.is_visited = False
    self.is_blocked = False
    self.neighbours = []
    self.mark = "-"

def create_map(width, height):
  node_map = []

  for i in range(0, height):
    row = [Node() for node in range(0, width)]
    node_map.append(row)

  set_neighbours(node_map, width, height)

  return node_map

def set_neighbours(node_map, width, height):
  for y in range(0, height):
    for x in range(0, width):
      node = node_map[y][x] # gets node by coordinates
      if x > 0:
        node.neighbours.append(node_map[y][x - 1]) # sets neighbour to the right
      if x < width - 1:
        node.neighbours.append(node_map[y][x + 1]) # sets neighbour to the left
      if y > 0:
        node.neighbours.append(node_map[y - 1][x]) # sets neighbour above
      if y < height - 1:
        node.neighbours.append(node_map[y + 1][x]) # sets neighbour below

def do_dijkstra(nodeMap, start, end):
  iterations = 0
  nodes_to_visit = [start]
  start.distance = 0

  while(nodes_to_visit):
    best_node = min(nodes_to_visit, key= lambda x: x.distance)
    if best_node is end:
      print(f"Found ending node after {iterations} iterations")
      return

    for neighbour in best_node.neighbours:
      reach_distance = best_node.distance + 1
      if (not neighbour.is_visited and
          not neighbour.is_blocked and
          neighbour.distance > reach_distance):
        neighbour.distance = reach_distance
        neighbour.parent = best_node
        neighbour.mark = "+"
        nodes_to_visit.append(neighbour)

    best_node.isVisited = True
    best_node.mark = "+"
    nodes_to_visit.remove(best_node)
    iterations += 1

  print(f"No solution was found after {iterations} iterations")

def trace_path(start_node, end_node):
  head_node = end_node
  path = []
  while(head_node.parent != None and head_node != start_node):
    path.append(head_node)
    head_node.mark = "#"
    head_node = head_node.parent

  return path

def print_map(node_map):
  starting_node.mark = "o"
  ending_node.mark = "x"

  print()
  for row in node_map:
    rowText = "| "
    for node in row:
        rowText += node.mark + " "
    rowText += " |"
    print(rowText)
  print()

nodes = create_map(15, 15)
starting_node = nodes[1][1]
ending_node = nodes[10][6]

print_map(nodes)
do_dijkstra(nodes, starting_node, ending_node)
trace_path(starting_node, ending_node)
print_map(nodes)