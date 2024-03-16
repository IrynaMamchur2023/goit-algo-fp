import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, node_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = []
    for node_id in tree.nodes():
        if node_id in node_colors:
            colors.append(node_colors[node_id])
        else:
            colors.append("skyblue")  

    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def DFS(node, depth=0, node_colors=None):
    if node_colors is None:
        node_colors = {}
    if node:
        if node.id not in node_colors:
            color = '#{:02x}{:02x}{:02x}'.format(20 + depth * 10, 20 + depth * 10, 200)
            node_colors[node.id] = color
            draw_tree(node, node_colors)
            DFS(node.left, depth + 1, node_colors)
            DFS(node.right, depth + 1, node_colors)
        else:
            pass 

def BFS(node):
    if node is None:
        return
    queue = [(node, 0)]
    node_colors = {}
    while queue:
        current_node, depth = queue.pop(0)
        if depth not in node_colors:
            node_colors[depth] = {}
        if current_node.id not in node_colors[depth]:
            color = '#{:02x}{:02x}{:02x}'.format(20 + depth * 10, 20 + depth * 10, 200)
            node_colors[depth][current_node.id] = color
            draw_tree(current_node, node_colors[depth])
            if current_node.left:
                queue.append((current_node.left, depth + 1))
            if current_node.right:
                queue.append((current_node.right, depth + 1))

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

DFS(root)
BFS(root)