import matplotlib.pyplot as plt
import networkx as nx

# Define a function wich computes the Closeness Centrality:

def closeness(graph):
    return nx.closeness_centrality(graph)

# Define a function wich plots the Closeness Centrality:

def plot_closeness(graph):
    closenessDict = closeness(graph)
    keyList = []
    closenessList = []
    for keys in closenessDict.keys():
        keyList.append(keys)
        closenessList.append(closenessDict[keys])
    y = closenessList
    print('Closeness Centrlality histogram:')
    plt.ylabel('Frequency for each CC value')
    plt.hist(y)
    plt.show()
    
# Define a function wich computes the Betweeness Centrality:

def betweeness(graph):    
    return nx.betweenness_centrality(graph)

# Define a function wich plots the Betweeness Centrality:
    
def plot_betweeness(graph):
    betweennessDict = betweeness(graph)
    keyList = []
    betweennessList = []
    for keys in betweennessDict.keys():
        keyList.append(int(keys))
        betweennessList.append(betweennessDict[keys])
    y = betweennessList
    print(' Betweeness Centrality histogram:')
    plt.ylabel('Frequency for each BC value')
    plt.hist(y)
    plt.show()

# Define a function wich computes the Degree Centrality:

def degree(graph):    
    return nx.degree_centrality(graph)

# Define a function wich plots the Degree Centrality:
    
def plot_degree(graph):
    degreeDict = degree(graph)
    keyList = []
    degreeList = []
    for keys in degreeDict.keys():
        keyList.append(int(keys))
        degreeList.append(degreeDict[keys])
    y = degreeList
    print(' Degree Centrality histogram:')
    plt.ylabel('Frequency for each DC value')
    plt.hist(y)
    plt.show()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    