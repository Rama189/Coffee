'''Follow the below steps to solve the problem:

1. Create a recursive function that takes the index of the node and a visited array.
2. Mark the current node as visited and print the node.
3. Traverse all the adjacent and unmarked nodes and call the recursive function with the index of the adjacent node.

For DFS with adjacency list:
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Auxiliary Space: O(V), since an extra visited array of size V is required.
'''

from collections import defaultdict
# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        if v in visited:
            return

        print(v) #Node being visited now
        visited.add(v)

        # Recur for all the vertices adjacent to this vertex
        neighbours = self.graph[v]
        for next_node in neighbours:
            self.DFSUtil(next_node, visited)

    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)

# Create a graph given in the above diagram
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)