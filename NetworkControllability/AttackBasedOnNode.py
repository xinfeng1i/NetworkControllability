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
import operator
import random
import csv

__author__ = """Xin-Feng Li (silfer.lee@gmail.com)"""

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

def attack_based_node_load_cascading():
    pass

if __name__ == "__main__":
    G = nx.erdos_renyi_graph(200, 0.05)
    G_deep = G.copy()

    (ND_degree, T_degree) = attack_based_max_degree(G)
    with open("Degree_Attack.csv", "w") as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(T_degree, ND_degree))

    
    (ND, T) = attack_based_random(G_deep)
    with open("Random_Attack.csv", "w") as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(T, ND))