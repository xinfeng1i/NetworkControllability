"""
Node-based attack strategy, including:
    * random attack
    * max degree based attack
    * max betweenness based attack
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
import copy
import subprocess, os # for run matlab to plot the figure

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

    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    tot_ND[0] = ND
    tot_T[0] = 0

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
def attack_based_max_betweenness(G):
    """ Recalculate betweenness attack

    Basic Idea:
    ----------
    Every time we remove the node with max betweeneness-centrality, then 
    recalcuate all nodes' betweenness NOTE that here remove a node only 
    remove all the edges adjacent to it.

    Parameters:
    ----------
    G: graph (directed or undirected)

    Returns:
    -------
    tot_ND:     the number of driver nodes after every node removed
    tot_T:      the number of removed nodes
    Max_Betweenness_Zero_T: the number of removed nodes such that 
                            all nodes' betweenness centrality have been zeros
    """
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

# TODO test this function
def node_load_cascade_attack(G, c):
    """ Cascade attack based on node-capacity
    """
    # initial ND, attack time T = 0
    ret_ND = []
    ret_T = []
    T = 0
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    ret_ND.append(ND)
    ret_T.append(T)

    # calculate the init load of each node
    loads = nx.load_centrality(G)
    # calculate the capacity of each node
    capacities = copy.deepcopy(loads)
    capacities.update((x, y * c) for x, y in capacities.items())
    # add node attribute capacity and node
    nx.set_node_attributes(G, 'capacity', capacities)
    nx.set_node_attributes(G, 'load', loads)

    # find the max load node
    node = max(loads, key=loads.get)
    # remove the max-load node
    nbrs = [i for i in nx.all_neighbors(G, node)]
    if nx.is_directed(G):
        for i in nbrs:
            if G.has_edge(i, node):
                G.remove_edge(i, node)
            if G.has_edge(node, i):
                G.remove_edge(node, i)
    else:
        for i in nbrs:
            G.remove_edge(i, node)
    
    # ND value after remove the max-load node
    T = 1
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    ret_T.append(T)
    ret_ND.append(ND)    
    # recaculate all loads of a node
    new_loads = nx.load_centrality(G)
    nx.set_node_attributes(G, 'load', new_loads)
    
    # cascade attack
    while True:
        # check all the nodes to find whether exist overloaded node
        has_overload_node = False
        node = None
        for x in G.nodes():
            if G.node[x]['load'] > G.node[x]['capacity']:
                # have over load node x
                has_overload_node = True
                # remove node (all edges adjacent to it)
                node = x
                break
        
        # if there is no overloaded node, cascade ends
        if not has_overload_node:
            break

        # else remove this node and recalucated all nodes' load
        nbrs = [i for i in nx.all_neighbors(G, node)]
        if nx.is_directed(G):
            for i in nbrs:
                if G.has_edge(i, node):
                    G.remove_edge(i, node)
                if G.has_edge(node, i):
                    G.remove_edge(node, i)
        else:
            for i in nbrs:
                G.remove_edge(i, node)
        # caluate ND after remove this node, attack time plus 1
        T = T + 1
        ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
        ret_T.append(T)
        ret_ND.append(ND)
        # update loads
        update_loads = nx.load_centrality(G)
        nx.set_node_attributes(G, 'load', update_loads)

    return (ret_ND, ret_T)


if __name__ == "__main__":
   
    ################################################################
    # test max-betweenness attack
    #G = nx.Graph()
    #G.add_nodes_from([0, 1, 2, 3])
    #G.add_edge(0, 1)
    #G.add_edge(0, 2)
    #G.add_edge(0, 3)
    #G.add_edge(1, 2)
    #G.add_edge(2, 3)
    #betweenness = nx.betweenness_centrality(G)
    #print 'betweenness:', betweenness

    G11 = nx.erdos_renyi_graph(100, 0.90)
    #G11 = nx.barabasi_albert_graph(100, 3)
    print 'Graph info:\n', nx.info(G11)
    G12 = G11.copy()
    G13 = G11.copy()
    G14 = G11.copy()

    (ND, T) = attack_based_random(G11)
    with open("results/RT.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(T, ND))

    (ND_degree, T_degree) = attack_based_max_degree(G12)
    with open("results/DT.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(T_degree, ND_degree))

    (ND_betweenness, T_betweenness, index_betweenness) = attack_based_max_betweenness(G13)
    with open("results/BT.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(T_betweenness, ND_betweenness))
    print 'index_betweenness = ', index_betweenness
    print 'After betweenness attack:', nx.info(G13)

    ND_capacity, T_capacity = node_load_cascade_attack(G14, 1.15)
    with open("results/CT.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(T_capacity, ND_capacity))

    os.chdir(r'D:\Program Files\MATLAB\R2010b\ComplexNetwork2015')
    print os.listdir(os.curdir)
    #subprocess.Popen(['matlab', 'attacktest.m'])