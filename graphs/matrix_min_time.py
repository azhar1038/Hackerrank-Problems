# REJECTED
# Failed Most of the case

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.visited = False
#         self.machine = False

# class Graph:
#     def __init__(self, roads, machines):
#         self.nodes = dict()
#         for i in range(len(roads)+1):
#             self.nodes[i] = [Node(i), []]

#         for road in roads:
#             from_town = road[0]
#             to_town = road[1]
#             weight = road[2]
#             self.nodes[from_town][1].append((to_town, weight))
#             self.nodes[to_town][1].append((from_town, weight))
#         for i in machines:
#             self.nodes[i][0].machine=True


# def minTime(roads, machines):
#     g = Graph(roads, machines)
#     for node in g.nodes:
#         print(node, g.nodes[node][0].machine, g.nodes[node][1])
#     g.nodes[machines[0]][0].visited=True
#     bfs(g.nodes, machines[0])
    

# def bfs(graph, start):
#     queue = [start]
#     cost=0
#     minimum=graph[start][1][0][1]
#     while len(queue) != 0:
#         node = graph[queue.pop(0)]
#         # if node[0].machine:
#         for neighbor in node[1]:
#             neighbor_node = graph[neighbor[0]][0]
#             if not neighbor_node.visited:
#                 weight = neighbor[1]
#                 if neighbor_node.machine:
#                     print(weight, minimum, cost)
#                     if weight < minimum:
#                         cost += weight
#                     else:
#                         cost += minimum
#                         minimum = weight
#                 # else:
#                 #     if weight < minimum:
#                 #         minimum = weight
#                 neighbor_node.visited = True
#                 queue.append(neighbor_node.data)
#     print(cost)

# def dfs(graph, machines, cost):
#     for machine in machines:
#         if not graph[machine][0].visited:
#             dfs_visit(graph, i, cost)

# def dfs_visit(graph, i, cost):
#     for neighbor in graph[i][1]:
#         neighbor_node = graph[neighbor[0]]
#         weight = neighbor[1]
#         if not neighbor_node.visited:
#             if not neighbor_node.machine:
#                 dfs_visit(graph, neighbor_node.data)

# minTime([
#     [0,4,2],
#     [0,1,4],
#     [1,3,7],
#     [1,2,3],
# ],[2,3,4])