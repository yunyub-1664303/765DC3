import json
from ast import literal_eval
import csv

class Node:
  def __init__(self, id: int, name: str, sub_cnt: int, children_ids: [int]):
    self.id = id
    self.name = name
    self.sub_cnt = sub_cnt
    self.children_ids = children_ids
    
  def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        else:
            return False

  def __str__(self):
     return json.dumps(self.__dict__)

# construct a list of all nodes in it
nodes = []
with open('all-nodes.csv') as file:
  reader = csv.DictReader(file)
  for row in reader:
    new_node = Node(row['id'], row['name'], row['subtreeProductCount'], literal_eval(row['children']))
    nodes.append(new_node)

def get_height(node):
  if len(node.children_ids) == 0:
    return 0
  return 1 + max(get_height(nodes[id]) for id in node.children_ids)

# compute the height of each node
for node in nodes:
  node.height = get_height(node)

print(nodes[29240])