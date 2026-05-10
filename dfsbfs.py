# Simple Python Program for DFS and BFS
# Using an Undirected Graph

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # Add edge in undirected graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # ---------- DFS ----------
    def DFS(self, v, visited):

        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)

    # ---------- BFS ----------
    def BFS(self, start):

        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:

            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


# Driver Code
g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)

print("DFS Traversal:")
visited = set()
g.DFS(0, visited)

print("\n")

print("BFS Traversal:")
g.BFS(0)