import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import geopandas as gpd
import folium as fm

from shapely.geometry import Point
from random import randint

senators = pd.read_csv("Data/senators.csv")

senator_co = pd.read_csv("Data/senateCosponsorship.csv")

G = nx.from_pandas_edgelist(senator_co, "V1", "V2")
G.add_nodes_from([60,86])

map = fm.Map(location=[40, -100], zoom_start=4)

for index, row in senators.iterrows():
    fm.Marker(location=[row['y'], row['x']], 
                  tooltip=row['name'], 
                  icon=fm.Icon(color='blue')
                 ).add_to(map)

# Social Network Visualization
''' Since we don't have any real sense of structure in the data, let's start by
viewing the graph with `random_layout`, which is among the fastest of the layout
functions.'''

fig, ax = plt.subplots(figsize=(15, 9))
ax.axis("off")
plot_options = {"node_size": 10, "with_labels": False, "width": 0.15}
nx.draw_networkx(G, pos=nx.random_layout(G), ax=ax, **plot_options)
plt.title("Social Network of the United States Senate")
plt.savefig('Network.png')

# Bill Cosponsorship Visualization
'''we can use the `spring_layout`
function which is the default layout function for the networkx drawing module.
The `spring_layout` function has the advantage that it takes into account the
nodes and edges to compute locations of the nodes. The downside however, is
that this process is much more computationally expensive, and can be quite
slow for graphs with 100's of nodes and 1000's of edges.'''


pos = nx.spring_layout(G, iterations=15, seed=1721)
fig, ax = plt.subplots(figsize=(15, 9))
ax.axis("off")
nx.draw_networkx(G, pos=pos, ax=ax, **plot_options)
plt.title("Bill Cosponsorship Network")
plt.savefig("Bill Cosponsorship.png")

# The number of nodes on an average each node is connected to

mean_nodes = np.mean([d for _, d in G.degree()])

# Degree Centrality
'''Degree centrality assigns an importance score based simply on the number of links held by each node.
 In this analysis, that means that the higher the degree centrality of a node is, the more edges are 
 connected to the particular node and thus the more neighbor nodes this node has.'''

degree_centrality = nx.centrality.degree_centrality(G)  
(sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True))[:8]

# This is the senator with the highest degree centrality

(senators.loc[senators['id'] == 53]) 

# This is the senator with the lowest degree centrality

degree_centrality = nx.centrality.degree_centrality(G)  
(sorted(degree_centrality.items(), key=lambda item: item[1], reverse=False))[:8]

(senators.loc[senators['id'] == 60]) 
(senators.loc[senators['id'] == 86])

# Closeness Centrality
'''Closeness centrality scores each node based on their ‘closeness’ to all other nodes 
in the network. For a node $v$, its closeness centrality measures the average farness to 
all other nodes. In other words, the higher the closeness centrality of $v$, the closer 
it is located to the center of the network.'''

closeness_centrality = nx.centrality.closeness_centrality(
    G
)  # save results in a variable to use again
(sorted(closeness_centrality.items(), key=lambda item: item[1], reverse=True))[:8]

# Betweenness Centrality

'''Betweenness centrality measures the number of times a node lies on the shortest path 
between other nodes, meaning it acts as a bridge. In detail, betweenness centrality of 
a node $v$ is the percentage of all the shortest paths of any two nodes (apart from $v$),
which pass through $v$. '''

betweenness_centrality = nx.centrality.betweenness_centrality(G)  # save results in a variable to use again
(sorted(betweenness_centrality.items(), key=lambda item: item[1], reverse=True))[:8]

