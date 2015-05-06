"""
explore all kinds of attack on nodes
including
    * random attack
    * max degree based attack
    * node load based cascade attack
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

__author__ = """Xin-Feng Li (silfer.lee@gmail.com)"""

###################################################################
def attack_based_random(G):
    """ Random attack

    Basic Idea:
    -----------
    Every time we randomly choose a node to attack, when say'attack'
    we mean remove all the edges adjacent to the node

    Parameters:
    -----------
    G:  graph (directed or undirected)

    Returns:
    --------
    tot_ND: the number of driver nodes after every node-remove
    tot_T:  the attack time   
    """
    n = G.number_of_nodes()
    tot_ND = [0] * (n+1)
    tot_T = [0] * (n+1)

    all_nodes = G.nodes()
    random.shuffle(all_nodes)

    for i in range(0, n):
        node = all_nodes[i]

        # remove all the edges adjacent to this node
        if not nx.is_directed(G):   # undirected graph
            for key in G[node].keys():
                G.remove_edge(node, key)
        else:   # directed graph
            for x in [v for u, v in G.out_edges_iter(node)]:
                G.remove_edge(node, x)
            for x in [u for u, v in G.in_edges_iter(node)]:
                G.remove_edge(x, node)
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)

        tot_ND[i+1] = ND
        tot_T[i+1] = i+1

    return (tot_ND, tot_T)


##########################################################################
def attack_based_max_degree(G):
    """ Recaculated Max degree attack

    Basic Idea:
    -----------
    Every time we remove a node with max degree and recalculated all
    nodes' degree. NOTE that here remove a node only remove all the edges
    adjacent to it.

    Parameters:
    -----------
    G:  graph (directed or undirected)

    Returns:
    --------
    tot_ND: the number of driver nodes after every node-remove
    tot_T:  the attack time   
    """
    n = G.number_of_nodes()
    tot_ND = [0] * (n+1)
    tot_T = [0] * (n+1)

    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    # attack process, every time, we remove the node with
    # max degree (only remove all the edges adjacent to it)
    # then evaluate the N_D number
    for i in range(1, n+1):
        all_degrees = G.degree()
        # get node with max degree       
        node = max(all_degrees, key=all_degrees.get)
        # remove all the edges adjacent to node
        if not nx.is_directed(G):   # undirected graph
            for key in G[node].keys():
                G.remove_edge(node, key)
        else:   # directed graph
            for x in [v for u, v in G.out_edges_iter(node)]:
                G.remove_edge(node, x)
            for x in [u for u, v in G.in_edges_iter(node)]:
                G.remove_edge(x, node)
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i] = ND
        tot_T[i]  = i
    return (tot_ND, tot_T)


#####################################################################
# TODO:To check Rightness
def attack_based_max_betweenness(G):
    n = G.number_of_nodes()
    tot_ND = [0] * (n+1)
    tot_T = [0] * (n+1)

    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

    # remember when all the betweenness have been zero for all nodes
    Max_Betweenness_Zero_T = -1
    for i in range(1, n+1):
        all_betweenness = nx.betweenness_centrality(G)
        # get node with max betweenness       
        node = max(all_betweenness, key=all_betweenness.get)
        if Max_Betweenness_Zero_T == -1 and abs(all_betweenness[node] - 0.0) < 1E-8:
            Max_Betweenness_Zero_T = i

        # remove all the edges adjacent to node
        if not nx.is_directed(G):   # undirected graph
            for key in G[node].keys():
                G.remove_edge(node, key)
        else:   # directed graph
            for x in [v for u, v in G.out_edges_iter(node)]:
                G.remove_edge(node, x)
            for x in [u for u, v in G.in_edges_iter(node)]:
                G.remove_edge(x, node)
        # calculate driver node number ND
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        tot_ND[i] = ND
        tot_T[i]  = i
    return (tot_ND, tot_T, Max_Betweenness_Zero_T)


if __name__ == "__main__":
    #G1 = nx.erdos_renyi_graph(100, 0.05)
    #G2 = G1.copy()
    #G3 = G1.copy()

    #(ND_degree, T_degree) = attack_based_max_degree(G1)
    #with open("results/Degree_Attack_ER100005.csv", "w") as f:
    #    writer = csv.writer(f, delimiter='\t')
    #    writer.writerows(zip(T_degree, ND_degree))

    
    #(ND, T) = attack_based_random(G2)
    #with open("results/Random_Attack_ER100005.csv", "w") as f:
    #    writer = csv.writer(f, delimiter='\t')
    #    writer.writerows(zip(T, ND))

    #(ND, T, index) = attack_based_max_betweenness(G3)
    #with open("results/Betweenness_Attack_ER100005.csv", "w") as f:
    #    writer = csv.writer(f, delimiter='\t')
    #    writer.writerows(zip(T, ND))
    #print 'index = ', index

    #****************************************************************
    #G11 = nx.barabasi_albert_graph(100, 2);
    #G12 = G11.copy()
    #G13 = G11.copy()

    #(ND_degree, T_degree) = attack_based_max_degree(G11)
    #with open("results/Degree_Attack_SF15.csv", "w") as f:
    #    writer = csv.writer(f, delimiter='\t')
    #    writer.writerows(zip(T_degree, ND_degree))

    
    #(ND, T) = attack_based_random(G12)
    #with open("results/Random_Attack_SF15.csv", "w") as f:
    #    writer = csv.writer(f, delimiter='\t')
    #    writer.writerows(zip(T, ND))

    #(ND, T, index) = attack_based_max_betweenness(G13)
    #with open("results/Betweenness_Attack_SF15.csv", "w") as f:
    #    writer = csv.writer(f, delimiter='\t')
    #    writer.writerows(zip(T, ND))
    #print 'index = ', index