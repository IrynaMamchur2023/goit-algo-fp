import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.key = key
        self.color = color
        self.id = str(uuid.uuid4())  

def add_heap_edges(graph, heap, pos, layer=1, index=1):
    if index <= len(heap):
        node = heap[index - 1]
        graph.add_node(node.id, color=node.color, label=node.key)  
        if 2 * index <= len(heap):
            graph.add_edge(node.id, heap[2 * index - 1].id)
            l = -1 / 2 ** layer
            pos[heap[2 * index - 1].id] = (l, -layer)
            add_heap_edges(graph, heap, pos, layer=layer + 1, index=2 * index)
        if 2 * index + 1 <= len(heap):
            graph.add_edge(node.id, heap[2 * index].id)
            r = 1 / 2 ** layer
            pos[heap[2 * index].id] = (r, -layer)
            add_heap_edges(graph, heap, pos, layer=layer + 1, index=2 * index + 1)

def draw_heap(heap):
    heap_graph = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}  # Початкова позиція для кореня купи
    add_heap_edges(heap_graph, heap, pos)

    colors = [node.color for node in heap]
    labels = {node.id: node.key for node in heap}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


heap = [HeapNode(1), HeapNode(2), HeapNode(3), HeapNode(4), HeapNode(5)]
for i, node in enumerate(heap):
    node.key = i + 1  


draw_heap(heap)