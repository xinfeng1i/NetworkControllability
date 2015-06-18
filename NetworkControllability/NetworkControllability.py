import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_pajek("dataset/Erdos971.net")
print nx.info(G)
isolated_nodes = nx.isolates(G)
print 'isolated_nodes:', G
G.remove_nodes_from(isolated_nodes)
print nx.info(G)