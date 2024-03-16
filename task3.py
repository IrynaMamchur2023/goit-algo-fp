import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append((destination, weight))

    def dijkstra(self, source):
        distances = [float('inf')] * self.vertices
        distances[source] = 0
        
        min_heap = [(0, source)]
        
        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)
            
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        
        return distances


graph = Graph(6)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 6)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 4, 4)
graph.add_edge(2, 5, 2)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 4, 1)
graph.add_edge(4, 5, 2)

source_vertex = 0
shortest_distances = graph.dijkstra(source_vertex)
print("Найкоротші відстані від вершини", source_vertex, ":", shortest_distances)