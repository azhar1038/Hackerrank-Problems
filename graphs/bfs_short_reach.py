class Node:
    def __init__(self, value):
        self.value = value
        self.distance = 0
        self.visited = False
        self.adjacent=[]
    def add_neighbor(self, node):
        self.adjacent.append(node)

class Graph:
    def __init__(self, n):
        self.graph_list=[]
        for i in range(n):
            self.graph_list.append(Node(i))

    def connect(self, x, y):
        x = self.graph_list[x]
        y = self.graph_list[y]
        x.add_neighbor(y)
        y.add_neighbor(x)

    def find_all_distances(self, s):
        distances = [-1]*len(self.graph_list)
        node = self.graph_list[s]
        node.visited=True
        queue=[node]
        while len(queue) != 0:
            current = queue.pop(0)
            for node in current.adjacent:
                if not node.visited:
                    node.visited = True
                    node.distance = current.distance + 6
                    distances[node.value]=node.distance
                    queue.append(node)
        for i in range(len(distances)):
            if i != s:
                print(distances[i], end=" ")
        print()



t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)

# Example Input:
# 2
# 4 2
# 1 2
# 1 3
# 1
# 3 1
# 2 3
# 2