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

def dfs_augmenting_paths_with_flow(matrix, source, sink, path=None, current_flow=float('inf')):
    if path is None:
        path = [(source, current_flow)]
    else:
        path.append((source, current_flow))

    if source == sink:
        print("Augmenting Path:", path)
    else:
        for neighbor, capacity, cost, _ in get_neighbors(matrix, source):
            if capacity > 0 and neighbor not in [node for node, _, _, _ in path]:
                new_flow = min(current_flow, capacity)
                dfs_augmenting_paths_with_flow(matrix, neighbor, sink, path.copy(), new_flow)

def get_neighbors(matrix, node):
    n = len(matrix)
    neighbors = []
    for i in range(n):
        if matrix[node][i] > 0:
            neighbors.append((i, matrix[node][i], 0, 0))
    return neighbors

# Example usage:
adjacency_matrix_with_flow = lst

source_node = 0
sink_node = 8

dfs_augmenting_paths_with_flow(adjacency_matrix_with_flow, source_node, sink_node)
