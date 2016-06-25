#coding=utf-8

import networkx as nx
import matplotlib.pyplot as plt
import exact_controllability as ECT
from networkx.utils import powerlaw_sequence
import operator
import random
import csv
import copy
import subprocess, os 
import numpy as np

if __name__ == "__main__":
    G_IEEE118 = nx.read_pajek("dataset/IEEE118.net")
    #(nd, driver_nodes) = ECT.get_driver_nodes(G_IEEE118)
    #nd = ECT.get_number_of_drivers_fast_rank(G_IEEE118)
    #print "nd = ", nd
    #with open("results/IEEE118_drivernodes.txt", "w") as f:
    #    for x in driver_nodes:
    #        print >> f, x


    G_NorthEast = nx.read_pajek("dataset/NorthEast.net")
    #(nd, driver_nodes) = ECT.get_driver_nodes(G_NorthEast)
    #print "nd = ", nd
    #with open("results/NorthEast_drivernodes.txt", "w") as f:
    #    for x in driver_nodes:
    #        print >> f, x

    G_CentralChina = nx.read_pajek("dataset/CentralChina.net")
    #(nd, driver_nodes) = ECT.get_driver_nodes(G_CentralChina)
    #print "nd = ", nd
    #with open("results/CentralChina_drivernodes.txt", "w") as f:
    #    for x in driver_nodes:
    #        print >> f, x


    G_IEEE30 = nx.read_pajek("dataset/IEEE30.net")
    #(nd, driver_nodes) = ECT.get_driver_nodes(G_IEEE30)
    #print "nd = ", nd
    #with open("results/IEEE30_drivernodes.txt", "w") as f:
    #    for x in driver_nodes:
    #        print >> f, x


    G_IEEE57 = nx.read_pajek("dataset/IEEE57.net")
    #(nd, driver_nodes) = ECT.get_driver_nodes(G_IEEE57)
    #print "nd = ", nd
    #with open("results/IEEE57_drivernodes.txt", "w") as f:
    #    for x in driver_nodes:
    #        print >> f, x

    G_IEEE145 = nx.read_pajek("dataset/IEEE145.net")
    #(nd, driver_nodes) = ECT.get_driver_nodes(G_IEEE145)
    #print "nd = ", nd
    #with open("results/IEEE145_drivernodes.txt", "w") as f:
    #    for x in driver_nodes:
    #        print >> f, x



    G_IEEE162 = nx.read_pajek("dataset/IEEE162.net")
    #(nd, driver_nodes) = ECT.get_driver_nodes(G_IEEE162)
    #print "nd = ", nd
    #with open("results/IEEE162_drivernodes.txt", "w") as f:
    #    for x in driver_nodes:
    #        print >> f, x

    G_IEEE300 = nx.read_pajek("dataset/IEEE300.net")
    #(nd, driver_nodes) = ECT.get_driver_nodes(G_IEEE300)
    #print "nd = ", nd
    #with open("results/IEEE300_drivernodes.txt", "w") as f:
    #    for x in driver_nodes:
    #        print >> f, x

    # configure model test result
    # '''计算CM模型的基本网络参数，主要是网络直径D和平均最短距离L'''
    #deg = nx.degree(G_CentralChina);
    #degseq = deg.values();
    #G = nx.configuration_model(degseq, create_using=G_CentralChina, seed=r);
    #N = nx.number_of_nodes(G);
    #M = nx.number_of_edges(G);
    #k = sum(nx.degree(G).values()) / (N + 0.0);
    ## '''转换多图到单图以计算聚集系数'''
    #G2 = nx.Graph(G);
    #C = sum(nx.clustering(G2).values()) / (G2.number_of_nodes() + 0.0);
    #D = nx.diameter(G)
    #L =nx.average_shortest_path_length(G2)
    #print "N = ", N;
    #print "M = ", M;
    #print "<k> = ", k;
    #print "C = ", C;
    #print "D = ", D;
    #print "L = ", L;

    #(nd, driver_nodes) = ECT.get_number_of_driver_nodes(G);
    ##nd = ECT.get_number_of_drivers_fast_rank(G);
    #print "configure model: nd = ", nd;


    #A = (nx.adjacency_matrix(G_ER30)).todense()   
    #print np.linalg.matrix_rank(A);

    ##########################################################################
	# The mean betweenness centrality and closeness centrality of driver nodes
	# and the whole network
    ########################################################################## 
    #G = G_IEEE118;
    #print "nd:", nd;
    #print "driver nodes:", driver_nodes
    #print "size of driver nodes: ", len(driver_nodes)
    #bc = nx.betweenness_centrality(G)
    #cc = nx.closeness_centrality(G)
    #print "bc : ", bc
    #print "cc : ", cc

    
    #mean_betweenness = 0.0;
    #mean_closeness = 0.0;
    #for x in driver_nodes:
    #    mean_betweenness = mean_betweenness + bc[x]
    #    mean_closeness = mean_closeness + cc[x]
    #print " =====", mean_betweenness;
    #mean_betweenness = mean_betweenness / len(driver_nodes);
    #mean_closeness = mean_closeness / len(driver_nodes);
    #print "mean betweenness: ", mean_betweenness;
    #print "mean closeness: ", mean_closeness;

    #mean_global_betweenness = sum(bc.values()) / nx.number_of_nodes(G);
    #mean_global_closeness = sum(cc.values()) / nx.number_of_nodes(G);
    #print "global mean betweenness: ", mean_global_betweenness
    #print "global mean closeness: ", mean_global_closeness
    
    ##############################################################################
    # mean degree of driver nodes and mean degree of the neighbors of driver nodes
	############################################################################## 
    #mean_driver = 0.0;
    #for x in driver_nodes:
    #    mean_driver = mean_driver + nx.degree(G_CentralChina, x)
    #mean_driver = mean_driver / len(driver_nodes)
    #print "avg driver nodes : ", mean_driver

    #mean_neighbor = 0.0
    #neighbors = [];
    #for x in driver_nodes:
    #    ylist = nx.neighbors(G, x)
    #    neighbors.extend(ylist)
    #for y in neighbors:
    #    mean_neighbor = mean_neighbor + nx.degree(G, y)
    #mean_neighbor = mean_neighbor / len(neighbors) 
    #print "avg neighbor nodes: ", mean_neighbor
    
    # '''20150929新加网络的平均邻居节点度'''
    # "单个节点的邻居节点平均度定义为：" k_{nn, i} = \frac{\sum_{j \in N_i} k_j}{N_i}
    # "对其作全网络平均值即可", <k>_nn = \sum_{i = 1}^{N} k_{nn, i} / N
    #G = G_IEEE162;
    #N = nx.number_of_nodes(G);
    #print "<k> = ", sum(nx.degree(G).values()) / (N + 0.0)
    #lst = nx.average_neighbor_degree(G).values();
    ##print lst;
    #print u"邻居节点平均度：", sum(lst) / (N + 0.0);

    #(nd, driver_nodes) = ECT.get_driver_nodes(G)
    #print "driver nodes:", driver_nodes;
    #print "nd = ", nd; 
    #print "number of driver nodes", len(driver_nodes);
    #nd_neighbor_degree = sum(nx.average_neighbor_degree(G, nodes=driver_nodes).values()) / len(driver_nodes);
    #print u"驱动节点邻居平局度：", nd_neighbor_degree



    ###############################################################################
    # Model networks H and <k> with n_D
    ###############################################################################
    
    ###############################################################################
    # Test <k>, H and H/<k> for ER, BA, WS model networks
    ###############################################################################
    #n = 302
    #m = 2
    #G = nx.barabasi_albert_graph(n, m);
    #(nd, driver_nodes) = ECT.get_driver_nodes(G)
    #deg = nx.degree(G).values()
    #avg_deg = (sum(deg) + 0.0) / G.number_of_nodes()
    #H = np.std(deg)
    #print 'nd = ', nd;
    #print "nD = ", (nd + 0.0) / G.number_of_nodes()
    #print "<k> = ", avg_deg;
    #print "H = ", H

    G = G_IEEE300
    deg = nx.degree(G).values();
    G2 = nx.configuration_model(deg, seed=123);
    (nd, driver_nodes) = ECT.get_driver_nodes(G2)
    deg2 = G2.degree().values();
    avg_deg = (sum(deg2) + 0.0) / G2.number_of_nodes()
    H = np.std(deg2)
    print 'nd = ', nd;
    print "nD = ", (nd + 0.0) / G2.number_of_nodes()
    print "<k> = ", avg_deg;
    print "H = ", H