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
import math
import sys

def directed_erdos_renyi_network(n, p, seed=None):
    G = nx.erdos_renyi_graph(n, p, seed, True)
    return G

def directed_watts_strogatz_graph(n, k, p, seed=None):
    G = nx.watts_strogatz_graph(n, k, p, seed)
    DG = nx.DiGraph()
    DG.add_nodes_from(G.nodes())
    for (u, v) in G.edges_iter():
        r = random.randint(0, 1)
        if r == 0:
            DG.add_edge(u, v)
        else:
            DG.add_edge(v, u)
    return DG

def directed_newman_watts_strogatz_graph(n, k, p, seed=None):
    G = nx.newman_watts_strogatz_graph(n, k, p, seed)
    DG = nx.DiGraph()
    DG.add_nodes_from(G.nodes())
    for (u, v) in G.edges_iter():
        r = random.randint(0, 1)
        if r == 0:
            DG.add_edge(u, v)
        else:
            DG.add_edge(v, u)
    return DG

def directed_barabasi_albert_graph(n, m, seed=None):
    DG = nx.DiGraph()
    G = nx.barabasi_albert_graph(n, m, seed)
    DG.add_nodes_from(G.nodes())
    for (u, v) in G.edges_iter():
        r = random.randint(0, 1)
        if r == 0:
            DG.add_edge(u, v)
        else:
            DG.add_edge(v, u)
    return DG

def undirected_scale_free_network(n, average_degree, exp):
    """ Return a undirected scale free network with average degree and
    degree exponent adjustable
    The network is generated from the static model.
    """
    if exp == 1.0:
        print >> sys.stderr, "ERROR: The degree exponent cannot equals 1.0 !!!";
        return;
    k = average_degree;
    r = math.fabs(exp);
    alpha = 1.0 / (r - 1.0);

    G = nx.Graph()
    nodes = range(n);
    G.add_nodes_from(nodes);

    weight = [math.pow(i+1, -alpha) for i in nodes]
    tot_weight = sum(weight)
    weight = [(x+0.0) / tot_weight for x in weight]
    accu_weight = [sum(weight[0:i+1]) for i in range(n)]
    nedges = 0;
    totedges = (k+0.0) * n / 2.0;
    while nedges < totedges:
        r1 = random.random();
        for nodei in range(n):
            if accu_weight[nodei] > r1:
                break;
        r2 = random.random();
        for nodej in range(n):
            if accu_weight[nodej] > r2:
                break;
        if nodei != nodej and (not G.has_edge(nodei, nodej)):
            G.add_edge(nodei, nodej)
            nedges += 1;
    return G;




if __name__ == "__main__":
    #G = nx.watts_strogatz_graph(20, 4, 0.1)
    #G = nx.newman_watts_strogatz_graph(20, 4, 0.1)

    #DG = directed_watts_strogatz_graph(20, 4, 0.2)
    #DG = directed_newman_watts_strogatz_graph(20, 4, 0.2)
    #DG = directed_barabasi_albert_graph(20, 2)
    #eigenvector_dict = nx.eigenvector_centrality(DG, max_iter=1000)
    #G = undirected_scale_free_network(100, 6.0, 4.0);

    G = directed_erdos_renyi_network(20, 0.1)
    print G.edges()
    print G.nodes()
    nx.draw(G, with_labels=True)
    plt.show()