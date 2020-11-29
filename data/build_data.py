import json
from ast import literal_eval
import csv

src_file = 'all-nodes.csv'
out_file = 'all-data.json'
# src_file = 'PetSupplies.csv'
# out_file = 'pet-data.json'

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
    
  def to_json(self):
    return json.loads(json.dumps(self.__dict__))

# construct a list of all nodes in it
nodes = []
with open(src_file) as file:
  reader = csv.DictReader(file)
  for row in reader:
    new_node = Node(row['id'], row['name'], row['subtreeProductCount'], literal_eval(row['children']))
    nodes.append(new_node)

def get_height(node):
  if len(node.children_ids) == 0:
    return 0
  return 1 + max(nodes[id].height for id in node.children_ids)

# compute the height of each node
# construct children array for each node
for i in range(len(nodes) - 1, -1, -1):
  node = nodes[i]
  node.height = get_height(node)
  children = []
  for kid_id in node.children_ids:
    children.append(nodes[kid_id].to_json())
  node._children = children

json_root = nodes[0].to_json()
res = {"name": json_root['name'], "subcnt": json_root['sub_cnt'], "children": json_root['_children']}
# for node in nodes:
#   json_nodes.append(node.to_json())

with open(out_file, 'w') as outfile:
  json.dump(res, outfile)