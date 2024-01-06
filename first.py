import json
import pandas as pd
import networkx as nx
import networkx.algorithms.approximation as nx_app

f = open('C:\\Hackathon_2024\\Input data\\level1a.json')


data = json.load(f)
	
json_data = json.dumps(data)
df_json_normalize = pd.json_normalize(json.loads(json_data))

df = pd.DataFrame(data)
capacity=600


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

orders=[]
for i in range(0,len(df['neighbourhoods'])-2):
    y=df['neighbourhoods'][i]
    #print(y['distances'])
    lst.append(y['distances'])
    orders.append(y['order_quantity'])

#print(lst)

