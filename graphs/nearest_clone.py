class Graph:
    def __init__(self, graph_nodes, graph_from, graph_to, ids):
        self.graph = []
        for i in range(graph_nodes):
            self.graph.append(Node(i+1, ids[i]))
        for i in range(len(graph_to)):
            from_ = graph_from[i]-1
            to_ = graph_to[i]-1
            self.graph[from_].add_neighbor(self.graph[to_])
            self.graph[to_].add_neighbor(self.graph[from_])

    def __str__(self):
        result = ""
        for node in self.graph:
            result += str(node.value) + ": ["
            for neighbor in node.neighbor:
                result += str(neighbor)+" "
            result += "]\n"
        return result
        

class Node:
    def __init__(self, value, id):
        self.value=value
        self.neighbor = set()
        self.distance = 0
        self.origin=0
        self.color=id

    def add_neighbor(self, node):
        self.neighbor.add(node)

    def __str__(self):
        return "("+str(self.value)+"/"+str(self.color)+")"

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    g = Graph(graph_nodes, graph_from, graph_to, ids)
    queue=[]
    visited=[]
    for node in g.graph:
        if node.color == val:
            node.origin = node.value
            queue.append(node)
            visited.append(node)
    if len(queue) <= 1:
        return -1
    distance = bfs(queue, visited)
    return distance
    
def bfs(queue, visited):
    node = queue.pop(0)
    for neighbor in node.neighbor:
        if neighbor in visited and neighbor.origin != node.origin:
            print("Returning", node, neighbor, node.distance, neighbor.distance)
            return node.distance + neighbor.distance + 1
        if neighbor.origin != neighbor.value:
            neighbor.distance = node.distance + 1
        neighbor.origin = node.origin
        print(node, neighbor, node.distance, neighbor.distance)
        queue.append(neighbor)
        visited.append(neighbor)
    return bfs(queue, visited)

distance = findShortest(
    6,
    [1,1,2,4,4],
    [2,3,6,3,5],
    [2,1,2,2,1,2],
    1
)

print(distance)