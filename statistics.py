import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
from collections import Counter
import pandas as pd

# Define a function wich computes the Closeness Centrality:

def closeness(graph):
    return nx.closeness_centrality(graph)

# Define a function wich plots the Closeness Centrality:

def plot_closeness(graph):
    closenessDict = closeness(graph)
    clos = Counter(closenessDict.values())
    sns.barplot(x = list(clos.keys()), y = list(clos.values()),  palette = 'Greens_d')
    plt.title('Closeness Centrlality Bar Chart')
    plt.ylabel('Frequency for each CC value')
    plt.xlabel('Degree')
    plt.xticks(rotation='vertical')
    plt.show()    

    
# Define a function wich computes the Betweeness Centrality:

def betweeness(graph):    
    return nx.betweenness_centrality(graph)

# Define a function wich plots the Betweeness Centrality:
    
def plot_betweeness(graph):
    betweenessDict = betweeness(graph)
    betw = Counter(betweenessDict.values())
    sns.barplot(x = list(betw.keys()), y = list(betw.values()),  palette = 'Greens_d')
    plt.title('Betweeness Centrlality Bar Chart')
    plt.ylabel('Frequency for each BC value')
    plt.xlabel('Degree')
    plt.xticks(rotation='vertical')
    plt.show()

# Define a function wich computes the Degree Centrality:

def degree(graph):    
    return nx.degree_centrality(graph)

# Define a function wich plots the Degree Centrality:
    
def plot_degree(graph):
    degreeDict = degree(graph)
    deg = Counter(degreeDict.values())
    sns.barplot(x = list(deg.keys()), y = list(deg.values()),  palette = 'Greens_d')
    plt.title('Degree Centrlality Bar Chart')
    plt.ylabel('Frequency for each DC values')
    plt.xlabel('Degree')
    plt.xticks(rotation='vertical')
    plt.show()
    
# Define a function wich plots the regression for closenessDict, betweenessDict and degreeDict:    
    
def plot_regression(d1, d2, d3):    
    dataFrame = pd.DataFrame.from_dict([d1, d2, d3]).transpose()
    sns.pairplot(dataFrame,  kind = 'reg')
    plt.show()    