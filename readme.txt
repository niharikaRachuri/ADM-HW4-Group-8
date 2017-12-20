
In this homework we want to carry out some information from Computer Scientists network, by applying the graph methodologies. For the information that we want we used the reduced dblp.json: json file, which needs to be parsed and contains a portion of the network. Each entry contains the following information:
. author: the name of the authors
. authors_id: the ID of the authors
. id_conference: conference in which the authors participated
. id_conference_int: the integer number that corresponds to a specific conference
. id_publication:  publication of the conference
. id_publication_int: the integer number that corresponds to a specific publication
. title: title of the conference

In the first part we create a graph where whose nodes are the authorsID and two node are connected if they share one publication. The weight of each edge is equal to (1 - Jaccard similarity).

In the second part we compute some statistics and create the subgraph induced by the set of authors who published at the input conference at least once. Therefore, we compute three centrality measures: degree, betweenness and closeness. After that, we give in input authorsID and the integer d, create and visualize the second subgraph induced  by the nodes that have hop distance at most equal to d with the input author.

In the last part we compute the shortest path between the authorsID, that we give as input, and Aris. For the shortest path we used Dijkstra algorithm. After that, for the final point, define function that takes in input a subset of nodes (cardinality smaller than 21) and returns, for each node of the graph, its GroupNumber


PARSING.PY

1. Function: def author_id
	we create a dictionary for simplify the research of the ID authors, indeed the 		function return us the ID for a specific author
	
2. Function: def publications_for_author_id
	we create a dictionary authorsDict where the keys are the ID and the values are 	all the publications. The result of the function are all the publications for a 	given author

3. Function: def return_all_the_authors_IDs
	define a function where we create a list with all the authors ID

4. Function: def authors_for_conference
	define a function where create a list of IDs for the authors that have 			participated to a conference given in input, return the  who published at the 		input conference at least once


GRAPH.PY

1. Function: def create_graph
	define a function for create a graph where the nodes are all the ID authors

2. Function: def plot_graph
	define a function that given in input a graph and plot it with its info

3. Function: def subgraph
	define a function that given in input a graph and a list(list of IDs for 		the authors that have participated to a conference('id_conference_int' in input)) 	with which build a subgraph 

4. Function: def plot_subgraph

5 Function: def neighborhood
	define a function which finds, for each node, its neihbors until a defined
	distance d from the starting node



STATISTICS.PY

1. Function: def closeness
	define a function which we use networkx for computes the Closeness centrality 		measures. In a connected graph, closeness centrality (or closeness) of a node is a 	measure of centrality in a network, calculated as the sum of the length of the 		shortest paths between the node and all other nodes in the graph. Thus the more 	central a node is, the closer it is to all other nodes.

2. Function: def plot_closeness
	in this function we plot the Closeness Centrality

3. Function: def betweeness
	define a function which we use networkx for computes the Betweenness centrality 		measures. betweenness centrality is a measure of centrality in a graph based on 	shortest paths. For every pair of vertices in a connected graph, there exists at 	least one shortest path between the vertices such that either the number of edges 	that the path passes through (for unweighted graphs) or the sum of the weights of 	the edges (for weighted graphs) is minimized. The betweenness centrality for each 	vertex is the number of these shortest paths that pass through the vertex.

4. Function: def plot_betweeness
	define function with plot the Betweenness Centrality

5. Function: def degree
	define a function which we use networkx for computes the Degree centrality 		measures, which is defined as the number of links incident upon a node (i.e., the 	number of ties that a node has). The degree can be interpreted in terms of the 		immediate risk of a node for catching whatever is flowing through the network.

6. Function: def plot_degree
	plot the Degree Centrality


DISTANCES.PY

1 Function: def JaccardSim
	define the function for the Jaccard similarity.
	The Jaccard index, also known as Intersection over Union and the Jaccard 		similarity coefficient (originally coined coefficient de communauté by Paul 		Jaccard), is a statistic used for comparing the similarity and diversity of sample 	sets. The Jaccard coefficient measures similarity between finite sample sets, and 	is defined as the size of the intersection divided by the size of the union of the 	sample sets. The Jaccard distance, is a measure of how dissimilar two sets are, is 	complementary to the Jaccard coefficient and is obtained by subtracting 		the Jaccard coefficient from 1, or, equivalently, by dividing the difference of 	the sizes of the union and the intersection of two sets by the size of the union.

2. Function: def Dijkstra
	define a function for a Dijkstra's algorithm. This is an algorithm for finding the 	shortest paths between nodes in a graph. In our case we used Dijkstra for finding 	the shortest paths from a single node(source) to a single destination node(target) 	by stopping the algorithm once the shortest path to the destination node has been 	determined.

3. Function: def groupNumber
	define a function that takes in input a subset of nodes returns, for each node of 	the graph, its GroupNumber, defined as follow:			GroupNumber(v) = min{ShortestPath(v,u)}, u∈I	where v is a node in the graph and I is the set of input nodes.




