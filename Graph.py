import networkx as nx
import matplotlib.pyplot as plt

# Define the function to create the graph:

def create_graph(l):
    G = nx.Graph(name='my graph')
    for element in l:
        G.add_node(element)
    return G

# Give in input a graph and plot it with its info:

def plot_graph(G):
    print(nx.info(G))
    pos = nx.random_layout(G)
    degrees = nx.degree(G)
    nx.draw_networkx_nodes(G, pos, node_shape = "o", node_size = 0.5 , node_color = "yellow")
    nx.draw_networkx_edges(G, pos, width = 0.2 , edge_color = "black", alpha = 0.5)
    plt.axis('off')
    plt.show()
 
# Give in input a graph and a list with which build a subgraph:    
    
def subgraph(graph, lis):
    return graph.subgraph(lis)

# Give in input a graph and a list with which plot a subgraph:     
    
def plot_subgraph(subgraph, lis):    
    map(int, lis)
    plt.plot(lis, color = "red")
    print('Authors IDs by ax')
    plt.ylabel('Authors in conference given in input:')
    plt.show()
    print(nx.info(subgraph))
    degDict = nx.degree(subgraph)
    keyList = []
    degList = []
    for keys in degDict.keys():
        keyList.append(keys)
        degList.append(degDict[keys])
    #plt.plot(degList, keyList)
    plt.hist(degList, color= "orange") #histogram for the distribution of graph degrees in the subgraph
    plt.ylabel('Subgraph degree')
    plt.show()
    print('Subgraph induced:')
    pos = nx.random_layout(subgraph)
    nx.draw_networkx_nodes(subgraph, pos, node_shape = "o", node_size = [v*27 for v in degDict.values()] , node_color = "yellow")
    nx.draw_networkx_edges(subgraph, pos, width = 0.2 , edge_color = "black", alpha = 0.5)
    plt.axis('off')
    plt.show()
    
# Define a function which finds, for each node, its neihbours until a defined
# distance d from the starting node:

def neighbourhood(a, dist, graph):
    l = []
    l.extend(graph.neighbors(a))    
    for i in range(dist - 1):
        for el in l:
            l.extend(graph.neighbors(el))
            l = list(set(l))
    return l    
    
    
    
    
    
    
    
