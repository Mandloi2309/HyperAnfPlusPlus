import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np
import math
import hashlib
import project.hllpp_anf as HyperPpAnf

from project.hllpp_counter import HllppCounter

k = 10

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../project/twitter-small2911.csv')

graph = nx.cycle_graph(10)  # nx.read_edgelist(filename, create_using=nx.DiGraph())

print("Number of nodes: {0}".format(len(graph.nodes())))
print("Number of edges: {0}".format(len(graph.edges())))

# nx.draw(graph)
# plt.show()

HyperPpAnf.init(graph)
HyperPpAnf.run(graph)