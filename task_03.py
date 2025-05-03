import heapq
from collections import defaultdict

def create_graph():
    graph = defaultdict(list)
    edges = [
        ("A", "B", 1),
        ("A", "C", 7),
        ("B", "D", 2),
        ("C", "D", 2),
        ("C", "E", 3),
        ("D", "E", 1),
        ("E", "F", 5),
    ]
    nodes = {"A", "B", "C", "D", "E", "F"}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph, nodes

def dijkstra(graph, nodes, start):
    distances = {node: float("inf") for node in nodes}
    distances[start] = 0
    paths = {node: [] for node in nodes}
    paths[start] = [start]

    pq = [(0, start)]
    while pq:
        dist_u, u = heapq.heappop(pq)
        if dist_u > distances[u]:
            continue
        for v, weight in graph[u]:
            new_dist = dist_u + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                paths[v] = paths[u] + [v]
                heapq.heappush(pq, (new_dist, v))
    return distances, paths

# Test
graph, nodes = create_graph()
start = "A"
distances, paths = dijkstra(graph, nodes, start)

print(f"Shortest paths from {start}:")
for node in sorted(nodes):
    if node != start:
        print(f"To {node}: Distance = {distances[node]}, Path = {' -> '.join(paths[node])}")
