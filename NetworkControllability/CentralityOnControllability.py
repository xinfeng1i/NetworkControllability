# -*- coding: utf-8 -*-
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
import NetworkModels as NM
import math
import sys
import numpy as np
import strutral_controllability as LBSC # short for Liu & Barabasi Structural Controllability

def RandomNumber01():
    """ Generate a random number in (0, 1)
    """
    while True:
        r = random.random()
        if math.fabs(r) > 1E-8:
            return r


def set_random_weight(G):
    myWeights = {}
    for (u, v) in G.edges_iter():
        myWeights[(u, v)] = RandomNumber01()
    nx.set_edge_attributes(G, 'EdgeWeight', myWeights)
    return G

def low_middle_high_degree_ratio(G):
    """ Return the ratio of driver nodes in low-, middle-, high-degree nodes
    """
    if not nx.is_directed(G):
        raise nx.NetworkXError("control_nodes() is not defined for undirected graphs.")

    # 
    drivers = LBSC.control_nodes(G)
    degree = nx.degree(G)
    temp_degree = sorted(degree.items(), key=operator.itemgetter(1))
    my_degree = [x for (x, deg) in temp_degree]

    third = len(my_degree) / 3
    two_third = len(my_degree) * 2 / 3
    last_remain = len(my_degree) - two_third
    low_degree = set(my_degree[0:third])
    middle_degree = set(my_degree[third:two_third])
    
    low_cnt = 0
    middle_cnt = 0
    high_cnt = 0
    for node in drivers:
        if node in low_degree:
            low_cnt += 1
        elif node in middle_degree:
            middle_cnt += 1
        else:
            high_cnt += 1

    low_ratio = float(low_cnt) / len(low_degree)
    middle_ratio = float(middle_cnt) / len(middle_degree)
    high_ratio = float(high_cnt) / (last_remain)
    return (low_ratio, middle_ratio, high_ratio)

def low_middle_high_in_degree_ratio(G):
    """ Return the ratio of driver nodes in low-, middle-, high- in-degree nodes
    """
    all_in_degrees = {}
    all_in_degrees = nx.in_degree_centrality(G)

    sorted_all_in_degrees = sorted(all_in_degrees.items(), key=operator.itemgetter(1))
    sorted_nodes = [k for (k, v) in sorted_all_in_degrees]
    
    n = nx.number_of_nodes(G)
    third = n / 3
    two_third = n * 2 / 3
    last = n - two_third

    low_nodes = set(sorted_nodes[0:third])
    middle_nodes = set(sorted_nodes[third:two_third])

    drivers = LBSC.control_nodes(G)
    low_cnt = 0
    middle_cnt = 0
    high_cnt = 0
    for node in drivers:
        if node in low_nodes:
            low_cnt += 1
        elif node in middle_nodes:
            middle_cnt += 1
        else:
            high_cnt += 1
    low_ratio = float(low_cnt) / len(low_nodes)
    middle_ratio = float(middle_cnt) / len(middle_nodes)
    high_ratio = float(high_cnt) / last

    return (low_ratio, middle_ratio, high_ratio)

def low_middle_high_out_degree_ratio(G):
    """ Return the ratio of driver nodes in low-, middle-, high- out-degree nodes
    """
    all_out_degrees = {}
    all_out_degrees = nx.out_degree_centrality(G)

    sorted_all_out_degrees = sorted(all_out_degrees.items(), key=operator.itemgetter(1))
    sorted_nodes = [k for (k, v) in sorted_all_out_degrees]
    
    n = nx.number_of_nodes(G)
    third = n / 3
    two_third = n * 2 / 3
    last = n - two_third

    low_nodes = set(sorted_nodes[0:third])
    middle_nodes = set(sorted_nodes[third:two_third])

    drivers = LBSC.control_nodes(G)
    low_cnt = 0
    middle_cnt = 0
    high_cnt = 0
    for node in drivers:
        if node in low_nodes:
            low_cnt += 1
        elif node in middle_nodes:
            middle_cnt += 1
        else:
            high_cnt += 1
    low_ratio = float(low_cnt) / len(low_nodes)
    middle_ratio = float(middle_cnt) / len(middle_nodes)
    high_ratio = float(high_cnt) / last

    return (low_ratio, middle_ratio, high_ratio)

def low_middle_high_betweenness_ratio(G):
    """ Return the ratio of driver nodes in low-, middle-, high-betweenness nodes
    """
    all_bets = {}
    if not nx.get_edge_attributes(G, 'EdgeWeight'):
        all_bets = nx.betweenness_centrality(G)
    else:
        all_bets = nx.betweenness_centrality(G, weight='EdgeWeight')
    sorted_all_bets = sorted(all_bets.items(), key=operator.itemgetter(1))
    sorted_nodes = [k for (k, v) in sorted_all_bets]
    
    n = nx.number_of_nodes(G)
    third = n / 3
    two_third = n * 2 / 3
    last = n - two_third

    low_nodes = set(sorted_nodes[0:third])
    middle_nodes = set(sorted_nodes[third:two_third])

    drivers = LBSC.control_nodes(G)
    low_cnt = 0
    middle_cnt = 0
    high_cnt = 0
    for node in drivers:
        if node in low_nodes:
            low_cnt += 1
        elif node in middle_nodes:
            middle_cnt += 1
        else:
            high_cnt += 1
    low_ratio = float(low_cnt) / len(low_nodes)
    middle_ratio = float(middle_cnt) / len(middle_nodes)
    high_ratio = float(high_cnt) / last

    return (low_ratio, middle_ratio, high_ratio)


def low_middle_high_closeness_ratio(G):
    """ Return the ratio of driver nodes in low-, middle-, high-closeness nodes
    """
    all_clos = {}
    if not nx.get_edge_attributes(G, 'EdgeWeight'):
        all_clos = nx.closeness_centrality(G)
    else:
        all_clos = nx.closeness_centrality(G, distance='EdgeWeight')
    sorted_all_clos = sorted(all_clos.items(), key=operator.itemgetter(1))
    sorted_nodes = [k for (k, v) in sorted_all_clos]
    
    n = nx.number_of_nodes(G)
    third = n / 3
    two_third = n * 2 / 3
    last = n - two_third

    low_nodes = set(sorted_nodes[0:third])
    middle_nodes = set(sorted_nodes[third:two_third])

    drivers = LBSC.control_nodes(G)
    low_cnt = 0
    middle_cnt = 0
    high_cnt = 0
    for node in drivers:
        if node in low_nodes:
            low_cnt += 1
        elif node in middle_nodes:
            middle_cnt += 1
        else:
            high_cnt += 1
    low_ratio = float(low_cnt) / len(low_nodes)
    middle_ratio = float(middle_cnt) / len(middle_nodes)
    high_ratio = float(high_cnt) / last

    return (low_ratio, middle_ratio, high_ratio)


def low_middle_high_eigenvector_ratio(G):
    """ Return the ratio of driver nodes in low-, middle-, high-eigenvector nodes
        eigenvecot centrality is defined as: x_i = 1/\lambda \sum_{j}(A_{ij}x_j)
    """
    all_eigvs = {}
    if not nx.get_edge_attributes(G, 'EdgeWeight'):
        all_eigvs = nx.eigenvector_centrality(G, max_iter=1000)
    else:
        all_eigvs = nx.eigenvector_centrality(G, max_iter=1000, weight='EdgeWeight')
    sorted_all_eigvs = sorted(all_eigvs.items(), key=operator.itemgetter(1))
    sorted_nodes = [k for (k, v) in sorted_all_eigvs]
    
    n = nx.number_of_nodes(G)
    third = n / 3
    two_third = n * 2 / 3
    last = n - two_third

    low_nodes = set(sorted_nodes[0:third])
    middle_nodes = set(sorted_nodes[third:two_third])

    drivers = LBSC.control_nodes(G)
    low_cnt = 0
    middle_cnt = 0
    high_cnt = 0
    for node in drivers:
        if node in low_nodes:
            low_cnt += 1
        elif node in middle_nodes:
            middle_cnt += 1
        else:
            high_cnt += 1
    low_ratio = float(low_cnt) / len(low_nodes)
    middle_ratio = float(middle_cnt) / len(middle_nodes)
    high_ratio = float(high_cnt) / last

    return (low_ratio, middle_ratio, high_ratio)


def low_middle_high_kats_ratio(G):
    """ Return the ratio of driver nodes in low-, middle-, 
        high-kats centrality nodes

      Note: kats centrality is a generalization of the eigenvector centrality.
      Defined as: x_i = \alpha \sum_{j}(A_{ij}x_j) + \beta
    """
    all_kats = {}
    if not nx.get_edge_attributes(G, 'EdgeWeight'):
        all_kats = nx.katz.katz_centrality(G)
    else:
        all_kats = nx.katz.katz_centrality(G, weight='EdgeWeight')
    sorted_all_kats = sorted(all_kats.items(), key=operator.itemgetter(1))
    sorted_nodes = [k for (k, v) in sorted_all_kats]
    
    n = nx.number_of_nodes(G)
    third = n / 3
    two_third = n * 2 / 3
    last = n - two_third

    low_nodes = set(sorted_nodes[0:third])
    middle_nodes = set(sorted_nodes[third:two_third])

    drivers = LBSC.control_nodes(G)
    low_cnt = 0
    middle_cnt = 0
    high_cnt = 0
    for node in drivers:
        if node in low_nodes:
            low_cnt += 1
        elif node in middle_nodes:
            middle_cnt += 1
        else:
            high_cnt += 1
    low_ratio = float(low_cnt) / len(low_nodes)
    middle_ratio = float(middle_cnt) / len(middle_nodes)
    high_ratio = float(high_cnt) / last

    return (low_ratio, middle_ratio, high_ratio)

def low_middle_high_pagerank_ratio(G):
    """ Return the ratio of driver nodes in low, middle, high-pagerank nodes
    """
    all_pageranks = {}
    if not nx.get_edge_attributes(G, 'EdgeWeight'):
        all_pageranks = nx.pagerank_alg.pagerank_numpy(G)
    else:
        all_pageranks = nx.pagerank_alg.pagerank_numpy(G, weight='EdgeWeight')

    sorted_all_pageranks = sorted(all_pageranks.items(), key=operator.itemgetter(1))
    sorted_nodes = [k for (k, v) in sorted_all_pageranks]
    
    n = nx.number_of_nodes(G)
    third = n / 3
    two_third = n * 2 / 3
    last = n - two_third

    low_nodes = set(sorted_nodes[0:third])
    middle_nodes = set(sorted_nodes[third:two_third])

    drivers = LBSC.control_nodes(G)
    low_cnt = 0
    middle_cnt = 0
    high_cnt = 0
    for node in drivers:
        if node in low_nodes:
            low_cnt += 1
        elif node in middle_nodes:
            middle_cnt += 1
        else:
            high_cnt += 1
    low_ratio = float(low_cnt) / len(low_nodes)
    middle_ratio = float(middle_cnt) / len(middle_nodes)
    high_ratio = float(high_cnt) / last

    return (low_ratio, middle_ratio, high_ratio)



if __name__ == "__main__":
    n = 1000
    p = 0.2
    k = 6

    RunCnt = 50
    tot1 = 0.0
    tot2 = 0.0
    tot3 = 0.0
    for i in range(RunCnt):
        print "current run count:\t",i+1 
        #G = NM.directed_erdos_renyi_network(n, p, seed=i+1)
        #G = NM.directed_watts_strogatz_graph(n,k,p, seed=i+1)
        G = NM.directed_newman_watts_strogatz_graph(n,k,p,seed=i+1)
        #G = NM.directed_barabasi_albert_graph(n, 6, seed=i+1)
        print 'average degree:\t', UF.average_degree(G)        
       
        set_random_weight(G)
        #(temp1, temp2, temp3) = low_middle_high_degree_ratio(G)
        #(temp1, temp2, temp3) = low_middle_high_betweenness_ratio(G)
        #(temp1, temp2, temp3) = low_middle_high_closeness_ratio(G)
        #(temp1, temp2, temp3) = low_middle_high_eigenvector_ratio(G)
        #(temp1, temp2, temp3) = low_middle_high_kats_ratio(G)
        #(temp1, temp2, temp3) = low_middle_high_pagerank_ratio(G)
        #(temp1, temp2, temp3) = low_middle_high_in_degree_ratio(G)
        (temp1, temp2, temp3) = low_middle_high_out_degree_ratio(G)
        tot1 += temp1
        tot2 += temp2
        tot3 += temp3
    tot1 = tot1 / RunCnt
    tot2 = tot2 / RunCnt
    tot3 = tot3 / RunCnt

    print 'low ratio:\t', tot1
    print 'middle ratio:\t', tot2
    print 'high ratio:\t', tot3


    # 
    

    
    #drivers = LBSC.control_nodes(G)
    
    #total_avg_degree = sum(nx.degree(G).values()) / float(n);
    #driver_avg_degree = sum(nx.degree(G, nbunch=drivers).values()) / float(n)
    #print 'total average degree: ', total_avg_degree
    #print 'driver average degree: ', driver_avg_degree

    #total_avg_neighbor_degree = sum(nx.average_neighbor_degree(G).values()) / float(n)
    #drivers_avg_neighbor_degree = sum(nx.average_neighbor_degree(G, nodes=drivers).values())/float(n)
    #print 'total average neighbor degree: ', total_avg_neighbor_degree
    #print 'drivers average neighbor degree:', drivers_avg_neighbor_degree



    # 
    #X = []
    #Y1 = []
    #Y2 = []
    #cnt = 0
    #nbr_degree = nx.average_neighbor_degree(G, nodes=drivers)
    #print 'Number of driver nodes: ', len(drivers)
    #for node in drivers:
    #    X.append(node)
    #    Y1.append(G.degree(node))
    #    Y2.append(nbr_degree[node])
    #    if nbr_degree[node] > G.degree(node):
    #        cnt += 1
    #print 'cnt = ', cnt
    #print 'percent: ', float(cnt) * 100 / len(drivers), '%'

    #Line1, = plt.plot(X, Y1, 'bo', label='degree (driver node)')
    #Line2, = plt.plot(X, Y2, 'rs', label='neighbor degree (driver node)')
    #plt.legend(handles=[Line1, Line2])
    #plt.xlabel('driver node ID')
    #plt.ylabel('degree')
    #plt.show()

    #degree = nx.degree(G)
    #betweenness = nx.betweenness.betweenness_centrality(G, weight='EdgeWeight')
    #closeness = nx.closeness.closeness_centrality(G, distance='EdgeWeight')


    # 
    #Y_driver_deg = []
    #Y_driver_bet = []
    #Y_driver_clo = []
    #for node in drivers:
    #    Y_driver_deg.append(degree[node])
    #    Y_driver_bet.append(betweenness[node])
    #    Y_driver_clo.append(closeness[node])


    #plt.plot(Y_driver_deg, Y_driver_bet, 'ro')
    #plt.title('betweenness-degree correlationship (driver nodes)')
    #plt.xlabel('degree')
    #plt.ylabel('betweenness')
    #plt.show()

    #plt.plot(Y_driver_deg, Y_driver_clo, 'ro')
    #plt.title('closeness-degree correlationship (driver nodes)')
    #plt.xlabel('degree')
    #plt.ylabel('closeness')
    #plt.show()



    #X2 = []
    #driver_bet = []
    #driver_clo = []
    #for node in drivers:
    #    X2.append(node)
    #    driver_bet.append(betweenness[node])
    #    driver_clo.append(closeness[node])

    
    #plt.figure(100)
    #plt.plot(X2, 'ro')
    #plt.title('driver nodes')
    #plt.show()
    


    #driver_bet.sort()
    #plt.figure(2)
    #plt.plot(driver_bet, 'bo')
    #plt.xlabel('driver nodes')
    #plt.ylabel('betweenness')
    #plt.title('driver nodes betweenness')
    #plt.show()

    #allNodes_bet = []
    #allNodes_bet = betweenness.values()
    #allNodes_bet.sort()
    #plt.plot(allNodes_bet, 'ks')
    #plt.title('all nodes betweenness')
    #plt.show()
    



    #driver_clo.sort()
    #plt.figure(3)
    #plt.plot(driver_clo, 'bo')
    #plt.xlabel('driver nodes')
    #plt.ylabel('closeness')
    #plt.show()

    #allNodes_clo = []
    #allNodes_clo = closeness.values()
    #allNodes_clo.sort()
    #plt.plot(allNodes_clo, 'ks')
    #plt.title('all nodes closeness')
    #plt.show()