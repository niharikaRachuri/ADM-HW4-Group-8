import networkx as nx
import heapq

# Definition of the function for the Jaccard distance to use as weight
# for the edges for the graph:
    
def JaccardSim(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    return (1-float(len(lst1.intersection(lst2))) / len(lst1.union(lst2)))

# Dijkstra function:

def Dijkstra(graph, source, target):    
    dist = {}
    prev = {}
    visited = set()
    for v in graph:
        dist[v] = float('inf')
        prev[v] = None
    dist[source] = 0

    while sum(1 for k, v in dist.items() if k not in visited and v < float('inf')):
        sorted_x = [v for v in sorted(dist, key=dist.get) if v not in visited]
        u = sorted_x[0]
        if u in visited:
            continue
        visited.add(u)
        if u == target:
            break

        for v in graph.neighbors(u):
            alt = dist[u] + graph[u][v]['weight']
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
            
    return dist[target]

# Shortest Path function:
    
def shortestPath(graph, source, target):
    dist = []
    prev = {}
    heapq.heappush(dist, (source, 0))
    
    for node in graph.nodes():
        prev[node] = None
    while len(dist) != 0:
        p = heapq.heappop(dist)
        
        if p[0] == target:
            return p[1]
        
        if prev[p[0]] is None:
            prev[p[0]] = p[1]
            
            for n in graph.neighbors(p[0]):
                heapq.heappush(dist, (n, graph[p[0]][n]['weight'] + p[1]))

#def shortestPath(graph, source, target):    
#    dist = []               
#    prev = {}               
#    for node in graph.nodes():
#        prev[node] = None
    
#    heapq.heappush(dist, [source, 0])

#    while len(dist) != 0:
#        p = heapq.heappop(dist)
#        if p[0] == target:
#            return p[1]
    
#        prev[p[0]] = p[1]

#        for vertex in graph.neighbors(p[0]):
#            if prev[vertex] is None:
#                heapq.heappush(dist, [vertex, p[1] + graph[p[0]][vertex]['weight']])

# Definition of the function that computes the Group Number:

#def groupNumber(subset, graph):
#    for j in subset:
#        for i in graph.nodes():    
#            if nx.has_path(graph, i, j):
#                print("The Group Number for ", i, "with", j, "is: ", Dijkstra(graph, i, j))

# Definition of the function that computes the Group Number:

def groupNumber(subset, graph):
    for j in subset:
        for i in graph.nodes():    
            if nx.has_path(graph, i, j):
                print("The Group Number for ", i, "with", j, "is: ", shortestPath(graph, i, j))



