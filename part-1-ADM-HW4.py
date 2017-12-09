#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:41:39 2017

@author: niharikarachuri
"""

import json
data = json.load(open('/Users/niharikarachuri/Documents/Python Files/ADM/HW4/reduced_dblp.json'))
# dict_keys(['authors', 'id_conference', 'id_conference_int', 'id_publication', 'id_publication_int', 'title'])

authorsDict = {}
'''
# If we need a dict of only author_id and author
for i in range(len(data)):
    for a in data[i]['authors']:
        for j in range(len(data[i]['authors'])):
            key = data[i]['authors'][j]['author_id']
            authorsDict[key] = data[i]['authors'][j]['author']
'''

# key: author id, value = list(publication1,pub2,...)
for i in range(len(data)):
    for a in data[i]['authors']:
        for j in range(len(data[i]['authors'])):
            key = data[i]['authors'][j]['author_id']
            if key in authorsDict.keys():
                if data[i]['id_publication_int'] not in authorsDict[key]:
                    authorsDict[key].append(data[i]['id_publication_int'])
            else:
                authorsDict[key] = [data[i]['id_publication_int']]

# To get authors for a given publication
for i in range(len(data)):
    if data[i]['id_publication_int'] == 342780:
        print(data[i])

# Function to find the Jaccardian distance
def DistJaccard(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    return (1-float(len(lst1 & lst2)) / len(lst1 | lst2))

# for checking the execution time
from datetime import datetime
start_time = datetime.now()

import networkx as nx
G = nx.Graph() # Empty graph
for authorid in authorsDict.keys():
    G.add_node(str(authorid))

# Loading all the publications id's into a list for easy access
pubIdList = []
for i in range(len(data)):
    pubIdList.append(data[i]['id_publication_int'])

import itertools

for i in range(len(data)):
    authorList = []
    #print(i)
    for j in range(len(data[i]['authors'])):
            authorList.append(data[i]['authors'][j]['author_id'])
    #for pubid in pubIdList:
        #print(authorList)
    combinationsAll = list(itertools.combinations(authorList,2))
    for k in combinationsAll :
        G.add_edge(str(k[0]),str(k[1]), weight = DistJaccard(authorsDict[k[0]],authorsDict[k[1]]))

#nx.draw(G)
print(nx.info(G))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)) # for checking the speed

import matplotlib.pyplot as plt
plt.savefig('foo.png')
