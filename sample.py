
import json
import pandas as pd
import networkx as nx
import networkx.algorithms.approximation as nx_app

f = open('C:\\Hackathon_2024\\Input data\\level0.json')


data = json.load(f)
	
json_data = json.dumps(data)
df_json_normalize = pd.json_normalize(json.loads(json_data))

df = pd.DataFrame(data)
 

lst=[[
        2495,
        1135,
        2117,
        623,
        1560,
        1641,
        1963,
        2210,
        788,
        1581,
        1533,
        1793,
        1241,
        510,
        1765,
        1442,
        875,
        1858,
        1401,
        2323
      ]]

for i in range(0,len(df['neighbourhoods'])-2):
    y=df['neighbourhoods'][i]
    #print(y['distances'])
    lst.append(y['distances'])

#print(lst)
#print(len(lst))

print(len(lst))

print(lst)

G = nx.random_geometric_graph(21, radius=0.4, seed=3)
pos = nx.get_node_attributes(G, "pos")



H = G.copy()


for i in range(len(lst)):
    for j in range(0, len(lst[0])):
        dist=lst[i]
        d=dist[j]
        G.add_edge(i, j, weight=d)


cycle = nx_app.christofides(G, weight="weight")


print("The route of the traveller is:", cycle)
"""
import sys
from itertools import permutations

def travelling_salesman_problem(graph, s):
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)
    min_path = sys.maxsize
    for i in permutations(vertex):
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        if current_pathweight < min_path:
            min_path = current_pathweight
            min_path_list = list(i)
            min_path_list.insert(0, s)
            min_path_list.append(s)
    print(f"The shortest path for the given graph is {min_path} and the corresponding path is {min_path_list}")

graph =lst
s = 0
travelling_salesman_problem(graph, s)
"""