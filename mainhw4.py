
import parsing as ps
import graph as g
import statistics as stat
import distances as d

# 1. Processing JSON file and creation of a graph G

# Import the data set:

data = ps.json.load(open('/Users/gaetanocirianni/Lab ADM/HW4/full_dblp.json'))

# Find the ID for a specific author:

ps.author_id(data, 'aris anagnostopoulos')

# Given the author's ID, find her/his publications:

ps.publications_for_author_id(data, 256176)

# Create the set of all author IDs in order to build the graph:

list_of_authors_IDs = ps.return_all_the_authors_IDs(data)
len(list_of_authors_IDs)

# Graph:

G = g.create_graph(list_of_authors_IDs)
g.plot_graph(G)

# We need a dictionary containing all the publications for a given author
# in order to give a relationship author-publication:

authorsDict = {}
for i in range(len(data)):
    for author in data[i]['authors']: 
        for j in range(len(data[i]['authors'])):
            key = data[i]['authors'][j]['author_id'] # the key is the ID for every author
            if key in authorsDict.keys(): 
                if data[i]['id_publication_int'] not in authorsDict[key]:
                    authorsDict[key].append(data[i]['id_publication_int'])
            else:
                authorsDict[key] = [data[i]['id_publication_int']]
authorsDict

# Now we can link the nodes:

# Loading all the publications ID's into a list for easy access

pubIdList = []
for i in range(len(data)):
    pubIdList.append(data[i]['id_publication_int'])

# 1. Create a list with all the authors' IDs for the authors wich enjoyed a conference
# 2. with intertools.combinations create all the possible pairs for each element in the list 
#    es: combinations('ABCD', 2) | AB AC AD CD
# 3. add an edge between the pairs created

for i in range(len(data)):
    authorList = []
    for j in range(len(data[i]['authors'])):
            authorList.append(data[i]['authors'][j]['author_id'])
    #for pubid in pubIdList:
     #   print(authorList)
    combinationsAll = list(ps.itertools.combinations(authorList, 2))
    #print(combinationsAll)
    for k in combinationsAll :
        G.add_edge((k[0]), (k[1]), weight = 1 - d.JaccardSim(authorsDict[k[0]],authorsDict[k[1]] ))

g.plot_graph(G)

# 2. Some statistics and visualizations:

# Find a list of IDs for the authors that have partecipated to a conference
# ('id_conference_int' in input):   

author_conf_list = ps.authors_for_conference(data, 3052)

# (a): Given the conference in input, return the subgraph induced by the set
# of authors who have published at the input conference at least once. 

confG = g.subgraph(graph=G, lis=author_conf_list) 

g.plot_subgraph(lis=author_conf_list, subgraph=confG)

# # Now we have the graph. Computation of some centralities measures and plot them.

# Closeness centrality:
# Represents the mean distance between a given node and all the others.   

stat.closeness(confG)
stat.plot_closeness(confG)
closenessDict = stat.closeness(confG)

# Betweeness centrality:
# It is a measure of centrality based on the shortest paaths.
# Fore every pair of vertices in a conncted graph, there exists at least one
#  shortest path between the vertices such that the sum of the weights of the edegs,
# for a weighted graph is minimized. The betweenness centrality for each vertex 
# is the number of these shortest paths that pass through the vertex.

stat.betweeness(confG)
stat.plot_betweeness(confG)
betweenessDict = stat.betweeness(confG)

# Degree centrality:
# Degree is a simple centrality measure that counts how many neighbors a node has.

stat.degree(confG)
stat.plot_degree(confG)
degreeDict = stat.degree(confG)

# Plot the regression for the three analysis

stat.plot_regression(closenessDict, betweenessDict, degreeDict)

# (b): Given in input an author and an integer d, get the subgraph induced by
# the nodes that have hop distance at most equal to d with the input author.
# Then, visualize the graph.

list_neighbors = g.neighbourhood(a= 43, dist= 2, graph= G)
G1 = g.subgraph(G, list_neighbors)
g.plot_subgraph(G1, list_neighbors)

# 3. Compute some generalized version of the Erdos number
# (a): Verify the presence of a path between Aris and the input author:

authorID = int(input("Enter the ID of the author you want to compute the distance from Aris: "))
d.nx.has_path(G, source = authorID, target = 256176)

#d.Dijkstra(G, authorID, 256176)
d.shortestPath(G, authorID, 256176)

#(b): Take in input a subset of nodes (cardinality smaller than 21) and returns,
# for each node of the graph, its GroupNumber, defined as the minimum SP
# between u and v, where v is a node in the graph and u belongs to I,
# which is the set of input nodes.

subset = list(map(int, input('Insert a subset (of cardinality smaller than 21) of nodes: ').split(" ")))

d.groupNumber(subset, G)