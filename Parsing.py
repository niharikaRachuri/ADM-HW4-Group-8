import json
import itertools
# Define a function to easily find the author ID for a given author name in input:

def author_id(data, author_name):
    nameID = {}
    for i in range (len(data)):
        for j in range(len(data[i]['authors'])):
            key = data[i]['authors'][j]['author']
            nameID[key] = data[i]['authors'][j]['author_id']
    return nameID[author_name]

# Define a function containing all the publications for a given author:

def publications_for_author_id(data, author_id):
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
    return authorsDict[author_id]

# Define a function wich returns all the authors' IDs

def return_all_the_authors_IDs(data):
    authors = []
    for i in range(len(data)):
        for j in range(len(data[i]['authors'])):
            authors.append(data[i]['authors'][j]['author_id'])
    return list(set(authors))

# Create a list of IDs for the authors that have partecipated to a conference
# (in input):

def authors_for_conference(data, conferenceInput):
    authorsList = []
    for i in range(len(data)):
        if data[i]['id_conference_int'] == conferenceInput :
            for j in range(len(data[i]['authors'])):
                data[i]['authors'][j]['author_id']
                authorsList.append(data[i]['authors'][j]['author_id'])
    return authorsList
