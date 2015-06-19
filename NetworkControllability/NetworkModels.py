import networkx as nx
import matplotlib.pyplot as plt
from networkx.utils import powerlaw_sequence
import operator
import random
import csv
import copy
import subprocess, os
import time
import UtilityFunctions as UF

def directed_watts_strogatz_graph(n, k, p):
    G = nx.watts_strogatz_graph(n, k, p)
    DG = nx.DiGraph()
    DG.add_nodes_from(G.nodes())
    for (u, v) in G.edges_iter():
        r = random.randint(0, 1)
        if r == 0:
            DG.add_edge(u, v)
        else:
            DG.add_edge(v, u)
    return DG

def directed_newman_watts_strogatz_graph(n, k, p):
    G = nx.newman_watts_strogatz_graph(n, k, p)
    DG = nx.DiGraph()
    DG.add_nodes_from(G.nodes())
    for (u, v) in G.edges_iter():
        r = random.randint(0, 1)
        if r == 0:
            DG.add_edge(u, v)
        else:
            DG.add_edge(v, u)
    return DG

def directed_barabasi_albert_graph(n, m):
    DG = nx.DiGraph()

    G = nx.barabasi_albert_graph(n, m)
    DG.add_nodes_from(G.nodes())
    for (u, v) in G.edges_iter():
        r = random.randint(0, 1)
        if r == 0:
            DG.add_edge(u, v)
        else:
            DG.add_edge(v, u)
    return DG


#def SelfSimilarityGrowingTreeNetwork(iteration_times):
#    # initialize
#    G = nx.Graph()
#    G.add_node(0)
#    G.add_node(1)
#    G.add_edge(0, 1)
    
#    added_edge = set()
#    added_edge.add((0, 1))

#    cur_iteration_times = 0
#    while cur_iteration_times < iteration_times:
#        new_added_edge = set()
#        for (u, v) in added_edge:         
#            n = G.number_of_nodes()
#            # add middle nodes
#            G.add_node(n)
#            G.add_node(n+1)
#            G.add_node(n+2)
#            G.remove_edge(u, v)
#            G.add_edge(u, n)
#            G.add_edge(v, n)
#            # add new branch nodes and edges
#            G.add_edge(n, n+1)
#            G.add_edge(n, n+2)
#            # update new added edge
#            new_added_edge.add((n, n+1))
#            new_added_edge.add((n, n+2))
#        added_edge = set()
#        added_edge = new_added_edge
#        cur_iteration_times += 1
#    return G 


if __name__ == "__main__":
    #G = nx.watts_strogatz_graph(20, 4, 0.1)
    #G = nx.newman_watts_strogatz_graph(20, 4, 0.1)
    #closeness_dict = nx.closeness_centrality(G)
    #print closeness_dict

    #DG = directed_watts_strogatz_graph(20, 4, 0.2)
    #DG = directed_newman_watts_strogatz_graph(20, 4, 0.2)
    DG = directed_barabasi_albert_graph(20, 2)
    eigenvector_dict = nx.eigenvector_centrality(DG, max_iter=1000)