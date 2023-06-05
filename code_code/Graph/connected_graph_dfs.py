'''Python3 program to print DFS traversal for complete graph
This will happen by handling a corner case. 

The above code traverses only the vertices reachable from a given source vertex.
All the vertices may not be reachable from a given vertex, as in a Disconnected graph. 
To do a complete DFS traversal of such graphs, run DFS from all unvisited nodes after a DFS. 
The recursive function remains the same.

'''
from collections import defaultdict

# this class represents a directed graph using adjacency list representation


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.count = 0
        # keeps track of which element belongs to which component list.
        self.component = defaultdict(int)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        if v in visited:
            return

        print(v)  # Node being visited now
        visited.add(v)
        self.component[v] = self.count

        # call the recursive helper function to print DFS traversal starting from all
        # vertices one by one
        neighbours = self.graph[v]
        for next_node in neighbours:
            self.DFSUtil(next_node, visited)

    def find_DFS_components(self):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal
        for vertex in self.graph:
            if vertex not in visited:
                self.count += 1
                self.DFSUtil(vertex, visited)


# Driver's code
# create a graph given in the above diagram
if __name__ == "__main__":
    print("Following is Depth First Traversal \n")
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.find_DFS_components()



