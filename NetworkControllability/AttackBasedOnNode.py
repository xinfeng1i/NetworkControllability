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
import copy

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
        
        print "remove node:", node
        # remove all the edges adjacent to node
        if not nx.is_directed(G):   # undirected graph
            for key in G[node].keys():
                G.remove_edge(node, key)
        else:   # directed graph
            for x in [v for u, v in G.out_edges_iter(node)]:
                G.remove_edge(node, x)
            for x in [u for u, v in G.in_edges_iter(node)]:
                G.remove_edge(x, node)
        print "after remove node betweenness:", nx.betweenness_centrality(G)
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
        has_overload_node = False
        for x in G.nodes():
            if G.node[x]['load'] > G.node[x]['capacity']:
                # have over load node x
                has_overload_node = True
                # remove node (all edges adjacent to it)
                node  = x
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
                break   # break the for loop
        # if hasn't any node overloaded, cascade end
        if not has_overload_node:
            break

    return (ret_ND, ret_T)


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

    G = nx.Graph()
    G.add_nodes_from([0, 1, 2, 3])
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 3)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    betweenness = nx.betweenness_centrality(G)
    print 'betweenness:', betweenness

    (ND, T, zeroIndex) = attack_based_max_betweenness(G)
    print "ND: ", ND
    print "T:", T;
    print "Zero Index:", zeroIndex
    plt.plot(T, ND, 'ro')
    plt.show()


    #loads = nx.load_centrality(G)
    #capacities = copy.deepcopy(loads)
    #capacities.update((a, b * 2) for a, b in capacities.items())
    #nx.set_node_attributes(G, 'capacity', capacities)
    #nx.set_node_attributes(G, 'load', loads)
    

    #print 'capacities:\n'
    #for i in G.nodes():
    #    print G.node[i]['capacity']

    #print 'loads:\n'
    #for i in G.nodes():
    #    print G.node[i]['load']

    #print 'update capacities:\n'
    #my_capacities = {0:0, 1:1, 2:2, 3:3}
    #nx.set_node_attributes(G, 'capacity', my_capacities)
    #for i in G.nodes():
    #    print G.node[i]['capacity']