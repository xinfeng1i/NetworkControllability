"""
Edge-based attack strategy, including:
    * Random Edge Attack
    * Initial Edge Degree Attack
    * Recalculated Edge Degree Attack
    * Initial Edge Betweenness Attack
    * Recalculated Edge Betweenness Attack
"""
#   Copyright (C) 2015 by
#   Xin-Feng Li <silfer.lee@gmail.com>
#   All rights reserved
#   BSD license

import networkx as nx
import matplotlib.pyplot as plt
import exact_controllability as ECT
from networkx.utils import powerlaw_sequence
import operator
import random
import csv
import copy
import subprocess, os # for run matlab to plot the figure

__author__ = """Xin-Feng Li (silfer.lee@gmail.com)"""

# check pass
def RandomEdgeAttack(G, remove_fraction = 1.0):
    """ Random Edge Attack
    """
    n = G.number_of_nodes()
    m = int(G.number_of_edges() * (remove_fraction + 0.0))
    
    tot_ND = [0] * (m+1)
    tot_T = [0] * (m+1)
    # initial ND
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0
    # get all edges of G, shuffle to form a random removed list
    all_edges = G.edges()
    random.shuffle(all_edges)
    # remove edge one by one
    for i in range(m):
        # remove edge
        u, v = all_edges[i]
        G.remove_edge(u, v)
        # calculate ND
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T[i+1] = i + 1

    return (tot_ND, tot_T)


# check pass
def InitialEdgeDegreeAttack(G, remove_fraction = 1.0):
    """ Initial Edge Degree Attack
    """
    n = G.number_of_nodes()
    m = int(G.number_of_edges() * (remove_fraction + 0.0))

    tot_ND = [0] * (m + 1)
    tot_T = [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    # calculate edge degree of each node
    all_edge_degrees = {}
    for u, v in G.edges():
        edge_degree = G.degree(u) * G.degree(v)
        all_edge_degrees[(u, v)] = edge_degree
    # sort the edge degree decending
    sorted_degrees = sorted(all_edge_degrees.items(), key = operator.itemgetter(1), reverse=True)
    for i in range(m):
        (u, v), d = sorted_degrees[i]
        G.remove_edge(u, v)
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1
    
    return (tot_ND, tot_T)


# check pass
def RecalculatedEdgeDegreeAttack(G, remove_fraction = 1.0):
    """ Recalculated Edge Degree Attack
    """
    n = G.number_of_nodes()
    m = int(G.number_of_edges() * (remove_fraction+0.0) )

    tot_ND = [0] * (m + 1)
    tot_T = [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    for i in range(m):
        # calculate max edge degree
        cur_max_edge_degree = -1
        cur_max_u = -1
        cur_max_v = -1
        for u, v in G.edges():
            temp = G.degree(u) * G.degree(v)
            if temp > cur_max_edge_degree:
                cur_max_edge_degree = temp
                cur_max_u = u
                cur_max_v = v
               
        # remove edge
        G.remove_edge(cur_max_u, cur_max_v)
        
        # calculate and save ND
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)


# check pass
def InitialEdgeBetweennessAttack(G, remove_fraction = 1.0):
    """ Initial Edge Betweenness Attack
    """
    n = G.number_of_nodes()
    m = int(G.number_of_edges() * (remove_fraction + 0.0))

    tot_ND = [0] * (m + 1)
    tot_T = [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    all_edgeBetweenness = nx.edge_betweenness(G)
    sorted_betweenness = sorted(all_edgeBetweenness.items(), key = operator.itemgetter(1), reverse=True)
    for i in range(m):
        (u, v), b = sorted_betweenness[i]
        G.remove_edge(u, v)
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T[i+1] = i + 1

    return (tot_ND, tot_T)


# check pass
def RecalculatedEdgeBetweennessAttack(G, remove_fraction = 1.0):
    """ Recalculated Edge Betweenness Attack
    """
    n = G.number_of_nodes()
    m = int(G.number_of_edges() * (remove_fraction + 0.0))

    tot_ND = [0] * (m + 1)
    tot_T = [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    for i in range(m):
        all_edgeBetweenness = nx.edge_betweenness(G)
        (u, v) = max(all_edgeBetweenness, key = all_edgeBetweenness.get)
        G.remove_edge(u, v)
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1
        
    return (tot_ND, tot_T) 


if __name__ == "__main__":
    #G1 = nx.erdos_renyi_graph(100, 0.05)

    #for run_cnt in range(10):
    #    G1 = nx.barabasi_albert_graph(100, 2)
    #    G2 = G1.copy()
    #    G3 = G1.copy()
    #    G4 = G1.copy()
    #    G5 = G1.copy()

    #    ND1, T1 = RandomEdgeAttack(G1)
    #    with open("results/test1_run%d.csv"%(run_cnt), "w") as f:
    #        writer = csv.writer(f, delimiter=',')
    #        writer.writerows(zip(T1, ND1))

    #    ND2, T2 = InitialEdgeBetweennessAttack(G2)
    #    with open("results/test2.csv", "w") as f:
    #        writer = csv.writer(f, delimiter=',')
    #        writer.writerows(zip(T, ND))

    #    ND3, T3 = RecalculatedEdgeBetweennessAttack(G3)
    #    with open("results/test3.csv", "w") as f:
    #        writer = csv.writer(f, delimiter=',')
    #        writer.writerows(zip(T, ND))

    #    ND4, T4 = InitialEdgeDegreeAttack(G4)
    #    with open("results/test4.csv", "w") as f:
    #        writer = csv.writer(f, delimiter=',')
    #        writer.writerows(zip(T, ND))
        
    #    ND5, T5 = RecalculatedEdgeDegreeAttack(G5)
    #    with open("results/test5.csv", "w") as f:
    #        writer = csv.writer(f, delimiter=',')
    #        writer.writerows(zip(T, ND))

    G = nx.Graph()
    G.add_edges_from([(0, 1), (0, 2), (2, 3)])
    d = G.degree(G.nodes())
    b = nx.edge_betweenness(G)
    print d
    print b

    d = {}
    for u, v in G.edges():
        edge_degree = G.degree(u) * G.degree(v)
        d[(u, v)] = edge_degree
    print 'initial degrees:', d

    sorted_degrees = sorted(d.items(), key = operator.itemgetter(1), reverse=True)
    print 'sorted_degrees:', sorted_degrees

    G1 = nx.barabasi_albert_graph(200, 3)
    print 'edge num:', G1.number_of_edges()

