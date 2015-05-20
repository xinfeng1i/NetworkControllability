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

def RandomNodeAttack(G, remove_fraction = 1.0):
    """ Random Node Attack
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()
    N_rm = int(n * remove_fraction)

    tot_ND = [0] * (N_rm + 1)
    tot_T = [0] * (N_rm + 1)
    tot_SCC = [0] * (N_rm + 1)

    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    #giant_SCC = nx.number_connected_components(G)
    giant_SCC = max(nx.connected_component_subgraphs(G), key=len)
    tot_ND[0] = ND
    tot_T[0] = 0
    tot_SCC[0] = giant_SCC.number_of_nodes()

    # random all nodes of G
    all_nodes = G.nodes()
    random.shuffle(all_nodes)

    # remove node one by one until N_rm nodes are removed
    for i in range(N_rm):
        node = all_nodes[i]
        G.remove_node(node)
        if G.number_of_nodes() == 0:
            break
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        #giant_SCC = nx.number_connected_components(G)
        giant_SCC = max(nx.connected_component_subgraphs(G), key=len)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1
        tot_SCC[i+1] = giant_SCC.number_of_nodes()

    return (tot_ND, tot_T, tot_SCC)



def InitialNodeDegreeAttack(G, remove_fraction = 1.0):
    """Initial Node Degree Attack
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()
    N_rm = int(n * remove_fraction)

    tot_ND = [0] * (N_rm + 1)
    tot_T = [0] * (N_rm + 1)

    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    all_nodes = G.nodes()
    all_degrees = G.degree(all_nodes)
    # sort node by degree decending
    sorted_degrees = sorted(all_degrees.items(), key = operator.itemgetter(1), reverse=True)
    
    for i in range(N_rm):
        node, degree = sorted_degrees[i]
        # remove node
        G.remove_node(node)
        if G.number_of_nodes() == 0:
            break
        # calcluate and save ND
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)



def RecalculatedNodeDegreeAttack(G, remove_fraction = 1.0):
    """Recalculated Node Degree Attack
    """
    
    n = G.number_of_nodes()
    m = G.number_of_edges()
    N_rm = int(n * remove_fraction)

    tot_ND = [0] * (N_rm + 1)
    tot_T = [0] * (N_rm + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    for i in range(N_rm):
        all_degrees = G.degree(G.nodes())
        max_degree_node = max(all_degrees, key = all_degrees.get)
        G.remove_node(max_degree_node)
        if G.number_of_nodes() == 0:
            break
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)


def InitialNodeBetweennessAttack(G, remove_fraction = 1.0):
    """ Initial Node Betweenness Attack
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()
    N_rm = int(n * remove_fraction)

    tot_ND = [0] * (N_rm + 1)
    tot_T = [0] * (N_rm + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T [0] = 0

    all_betweenness = nx.betweenness_centrality(G)
    sorted_betweenness = sorted(all_betweenness.items(), key = operator.itemgetter(1), reverse=True)

    for i in range(N_rm):
        node, betweenness = sorted_betweenness[i]
        G.remove_node(node)
        if G.number_of_nodes() == 0:
            break
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)



def RecalculatedNodeBetweennessAttack(G, remove_fraction = 1.0):
    """ Recalculated Node Betweenness Attack
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()
    N_rm = int(n * remove_fraction)

    tot_ND = [0] * (N_rm + 1)
    tot_T = [0] * (N_rm + 1)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T [0] = 0

    for i in range(N_rm):
        # caclulate the max-betweenness node
        all_betweenness = nx.betweenness_centrality(G)
        max_betweenness_node = max(all_betweenness, key = all_betweenness.get)
        # remove node
        G.remove_node(max_betweenness_node)
        if G.number_of_nodes() == 0:
            break
        # recalcualte & save ND
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i+1] = ND
        tot_T [i+1] = i + 1

    return (tot_ND, tot_T)
        
       

if __name__ == "__main__":
    pass
    #G1 = nx.erdos_renyi_graph(n, 0.03)
    #G2 = G1.copy()
    #G3 = G1.copy()
    #G4 = G1.copy()
    #G5 = G1.copy()
    #print nx.info(G1)
    #G_USAIR = nx.read_pajek("dataset/USAir97.net")
    #print "US AIR Line:"
    #print nx.info(G_USAIR)

    #G_Erdos = nx.read_pajek("dataset/Erdos971.net")
    #print "Erdos Networks:"
    #print nx.info(G_Erdos)
    #print "isolates:"
    #isolates_nodes =  nx.isolates(G_Erdos)
    #G_Erdos.remove_nodes_from(isolates_nodes)
    #print nx.info(G_Erdos)




    #ND2, T2 = InitialNodeDegreeAttack(G2)


    #ND3, T3 = RecalculatedNodeDegreeAttack(G3)


    #ND4, T4 = InitialNodeBetweennessAttack(G4)


    #ND5, T5 = RecalculatedNodeBetweennessAttack(G5)




    #with open("results/node_test2.csv", "w") as f:
    #    writer = csv.writer(f, delimiter=',')
    #    writer.writerows(zip(T2, ND2))

    #with open("results/node_test3.csv", "w") as f:
    #    writer = csv.writer(f, delimiter=',')
    #    writer.writerows(zip(T3, ND3))


    #with open("results/node_test4.csv", "w") as f:
    #    writer = csv.writer(f, delimiter=',')
    #    writer.writerows(zip(T4, ND4))


    #with open("results/node_test5.csv", "w") as f:
    #    writer = csv.writer(f, delimiter=',')
    #    writer.writerows(zip(T5, ND5))