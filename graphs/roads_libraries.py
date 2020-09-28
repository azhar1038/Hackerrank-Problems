def roadsAndLibraries(n, c_lib, c_road, cities):

    # If cost of building library is less than building road, simply build library in each city
    if c_lib<=c_road:
        return c_lib*n

    # Else create a graph to calculate
    visited = set()
    graph = {}

    # Initialise graph with each city as key
    for i in range(1,n+1):
        graph[i] = set()

    # Fill the graph
    for a, b in cities:
        graph[a].add(b)
        graph[b].add(a)

    # List to store number of vertex(city) in each component
    components=[]

    # Fill components list using dfs_count_neighbour method
    for vertex in graph:
        if vertex not in visited:
            components.append(dfs_count_neighbour(graph, visited, vertex))

    # Cost = Cost of building road connecting all city in each component + 
    #       Cost of building library in each component
    total_cost=0
    for component in components:
        total_cost += (component-1)*c_road + c_lib
    return total_cost
    
# Count number of vertices(cities) connected to the given vertex using recursion
def dfs_count_neighbour(graph, visited, vertex):
    visited.add(vertex)
    connected_vertices = 0
    for v in graph.get(vertex, []):
        if v not in visited:
            connected_vertices += dfs_count_neighbour(graph, visited, v)
    return connected_vertices+1


# SAMPLE GRAPH
#   1-----2
#        /
#       /
#      3
#     / \
#    /   \
#   4     5
#
#      6


cost = roadsAndLibraries(6, 4, 1, [
    (1,2),
    (2,3),
    (3,4),
    (3,5)
])

print(cost)