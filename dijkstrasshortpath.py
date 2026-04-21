import heapq

graph = {
0: [(1, 4), (2, 1)],
1: [(3, 1)],
2: [(1, 2), (3, 5)],
3: []
}

dist = {node: float('inf') for node in graph}
dist[0] = 0

pq = [(0, 0)]

while pq:
    d, node = heapq.heappop(pq)

    for neighbor, weight in graph[node]:
        new_dist = d + weight

        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

print(dist)