class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False

class Graph:
    def __init__(self, grid, n, m):
        self.nodes=dict()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    current = str(i)+str(j)
                    self.add_node(current)
                    if j>0 and grid[i][j-1]==1:
                        left = str(i)+str(j-1)
                        self.add_node(left)
                        self.add_neighbor(current, left)
                    if j<m-1 and grid[i][j+1]==1:
                        right = str(i)+str(j+1)
                        self.add_node(right)
                        self.add_neighbor(current, right)
                    if i>0 and grid[i-1][j]==1:
                        top = str(i-1)+str(j)
                        self.add_node(top)
                        self.add_neighbor(current, top)
                    if i<n-1 and grid[i+1][j]==1:
                        bottom = str(i+1)+str(j)
                        self.add_node(bottom)
                        self.add_neighbor(current, bottom)
                    if i>0 and j>0 and grid[i-1][j-1]==1:
                        top_left = str(i-1)+str(j-1)
                        self.add_node(top_left)
                        self.add_neighbor(current, top_left)
                    if i>0 and j<m-1 and grid[i-1][j+1]==1:
                        top_right = str(i-1)+str(j+1)
                        self.add_node(top_right)
                        self.add_neighbor(current, top_right)
                    if i<n-1 and j>0 and grid[i+1][j-1]==1:
                        bottom_left = str(i+1)+str(j-1)
                        self.add_node(bottom_left)
                        self.add_neighbor(current, bottom_left)
                    if i<n-1 and j<m-1 and grid[i+1][j+1]==1:
                        bottom_right = str(i+1)+str(j+1)
                        self.add_node(bottom_right)
                        self.add_neighbor(current, bottom_right)

    def add_neighbor(self, node1, node2):
        self.nodes[node1].neighbors.append(self.nodes[node2])
        self.nodes[node2].neighbors.append(self.nodes[node1])
    def add_node(self, node):
        if self.nodes.get(node, "-1") == "-1":
            self.nodes[node] = Node(node)
    def dfs(self):
        counts = []
        for key in self.nodes:
            node = self.nodes[key]
            if not node.visited:
                node.visited = True
                counts.append(self.dfs_visit(node, 0))
        return counts
    def dfs_visit(self, node, count):
        count += 1
        for neighbor in node.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                count = self.dfs_visit(neighbor, count)     
        return count



def maxRegion(grid):
    g = Graph(grid, len(grid), len(grid[0]))
    regions = g.dfs()
    print("All regions:", regions)
    print("Largest region:", max(regions))

maxRegion([
    [1,1,0,1],
    [0,0,0,0],
    [0,0,1,0],
    [1,0,1,0],
])

