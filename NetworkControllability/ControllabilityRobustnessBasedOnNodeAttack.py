"""
Node-based attack strategy, including:
    * Random Node Attack
    * Initial Node Degree Attack
    * Recalculated Node Degree Attack
    * Initial Node Betweenness Attack
    * Recalculated Node Betweenness Attack
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

def RandomNodeAttack(G):
    """ Random Node Attack
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()

    tot_ND = [0] * (m + 1)
    tot_T = [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    # random all nodes of G
    all_nodes = G.nodes()
    random.shuffle(all_nodes)

    # remove node one by one
    for i in range(n):
        node = all_nodes[i]
        G.remove_node(node)
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)



def InitialNodeDegreeAttack(G):
    """Initial Node Degree Attack
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()

    tot_ND = [0] * (m + 1)
    tot_T = [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    all_nodes = G.nodes()
    all_degrees = G.degree(all_nodes)
    # sort node by degree decending
    sorted_degrees = sorted(all_degrees.items(), key = operator.itemgetter(1), reverse=True)
    
    for i in range(len(sorted_degrees)):
        node, degree = sorted_degrees[i]
        # remove node
        G.remove_node(node)
        # calcluate and save ND
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)



def RecalculatedNodeDegreeAttack(G):
    """Recalculated Node Degree Attack
    """
    
    n = G.number_of_nodes()
    m = G.number_of_edges()

    tot_ND = [0] * (m + 1)
    tot_T = [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    for i in range(n):
        all_degrees = G.degree(G.nodes())
        max_degree_node = max(all_degrees, key = all_degrees.get)
        G.remove_node(max_degree_node)
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)


def InitialNodeBetweennessAttack(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()

    tot_ND = [0] * (m + 1)
    tot_T =  [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T [0] = 0

    all_betweenness = nx.betweenness_centrality(G)
    sorted_betweenness = sorted(all_betweenness.items(), key = operator.itemgetter(1), reverse=True)

    for i in range(n):
        node, betweenness = sorted_betweenness[i]
        G.remove_node(node)
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)



def RecalculatedNodeBetweennessAttack(G):
    """ Recalculated Node Betweenness Attack
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()

    tot_ND = [0] * (m + 1)
    tot_T =  [0] * (m + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T [0] = 0

    for i in range(n):
        # caclulate the max-betweenness node
        all_betweenness = nx.betweenness_centrality(G)
        max_betweenness_node = max(all_betweenness, key = all_betweenness.get)
        # remove node
        G.remove_node(max_betweenness_node)
        # recalcualte & save ND
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)
        
       

if __name__ == "__main__":
    pass
 