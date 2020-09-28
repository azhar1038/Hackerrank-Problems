class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
    
    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generateEdges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.__graph_dict:
            self.__graph_dict[v1].append(v2)
        else:
            self.__graph_dict[v1] = [v2]


    def __generateEdges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __repr__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k)+" "
        res += "\nedges: "
        for edge in self.__generateEdges():
            res += str(edge)+" "
        return res


if __name__ == "__main__":
    g={
        "a":["d"],
        "b":["c"],
        "c":["b", "c", "d", "e"],
        "d":["a","c"],
        "e":["c"],
        "f":[]
    }

    graph = Graph(g)

    print("Vertices of graph: ", graph.vertices())
    print("Edges of graph: ", graph.edges())
    print("Add vertex z!")
    graph.add_vertex("z")
    print("Vertices of graph: ", graph.vertices())
    print("Add an edge {a, z}")
    graph.add_edge(("a", "z"))
    print("Edges of graph: ", graph.edges())
    print("\n")
    print(graph)