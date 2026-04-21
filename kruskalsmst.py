class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def KruskalMST(self):

        result = []
        i = 0
        e = 0

        self.graph.sort(key=lambda item: item[2])

        parent = []

        for node in range(self.V):
            parent.append(node)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, x, y)

        cost = 0

        print("Edges in the constructed MST")

        for u, v, w in result:
            cost += w
            print(u, "--", v, "==", w)

        print("Minimum Spanning Tree", cost)


# Driver Code
g = Graph(4)

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()