import numpy as np
import networkx as nx
import exact_controllability as ECT
import strutral_controllability as SCT
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import csv
import operator
import random
import os
import subprocess
import threading
import time


def exact_controllability_run_on_ER_one_time(n, prob_start, prob_end, data_cnt):
    probs = np.linspace(prob_start, prob_end, num = data_cnt);
    driver_nodes = [0.0] * len(probs)
    driver_dense = [0.0] * len(probs)
    for i in range(len(probs)):
        p = probs[i]
        G = nx.erdos_renyi_graph(n, p)
        (ND, ND_lambda) = exact_controllability.get_number_of_driver_nodes(G)
        driver_nodes[i] = ND
        driver_dense[i] = (ND + 0.0) / (n + 0.0)
    return (probs, driver_dense)

def exact_controllability_run_on_ER(n, prob_start, prob_end, data_cnt, runcnt):
    tot_probs = [0.0] * data_cnt
    tot_dense = [0.0] * data_cnt
    for run_cnt in range(runcnt):
        (probs, driver_dense) = exact_controllability_run_on_ER_one_time(n, prob_start, prob_end, data_cnt)
        tot_probs = map(operator.add, tot_probs, probs)
        tot_dense = map(operator.add, tot_dense, driver_dense)
    
    tot_probs = [x / (runcnt + 0.0)  for x in tot_probs]
    tot_dense = [x / (runcnt + 0.0)  for x in tot_dense]
    with open("ER_Result.csv", "w") as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(tot_probs, tot_dense))

    plt.plot(tot_probs, tot_dense, 'ro')
    plt.title('Exact Controllability Run on ER network')
    plt.xlabel('$p$')
    plt.ylabel('$n_D$')
    plt.show()

def struct_controllability_on_ER():
    N = 1000
    k = []
    nD = []
    for avg_k in range(0, 80, 2):
        G = nx.erdos_renyi_graph(N, (avg_k + 0.0) / (N + 0.0), directed = True)
        #H = nx.barabasi_albert_graph(1000, 3);
        #print nx.info(H)
        #G = nx.DiGraph()
        #G.add_nodes_from(H.nodes())
        #for (a, b) in H.edges():
        #    r = random.randint(0, 1)
        #    w = random.uniform(0, 1)
        #    if r == 0:
        #        G.add_edge(a, b, weight = w)
        #    else:
        #        G.add_edge(b, a, weight = w)
        (isperfected, ND, driverNodes) = SCT.get_driver_nodes(G)
        nD.append(ND / (N + 0.0))
        k.append(avg_k / 1.0)
    #plt.plot(k, nD, '-o')
    plt.semilogy(k, nD, '-o')
    plt.xlabel('$k$')
    plt.ylabel('$n_D$')
    plt.show()


def correlation_betweenness_degree_on_ER():
    N = 1000
    p = 0.004
    G = nx.erdos_renyi_graph(N, p)
    print nx.info(G)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    ND, driverNodes = ECT.get_driver_nodes(G)

    degrees = []
    betweenness = []
    tot_degree = nx.degree_centrality(G)
    tot_betweenness = nx.betweenness_centrality(G,weight=None)

    for node in driverNodes:
        degrees.append(tot_degree[node])
        betweenness.append(tot_betweenness[node])

    with open("results/driver_degree_ER.txt", "w") as f:
        for x in degrees:
            print >> f, x
    with open("results/driver_betweenness_ER.txt", "w") as f:
        for x in betweenness:
            print >> f, x

    with open("results/tot_degree_ER.txt", "w") as f:
        for key, value in tot_degree.iteritems():
            print >> f, value

    with open("results/tot_betweenness_ER.txt", "w") as f:
        for key, value in tot_betweenness.iteritems():
            print >> f, value

def correlation_betweenness_degree_on_WS():
    n = 1000
    k = 4
    p = 0.01
    G = nx.watts_strogatz_graph(n, k, p)

    print nx.info(G)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    ND, driverNodes = ECT.get_driver_nodes(G)

    degrees = []
    betweenness = []

    tot_degree = nx.degree_centrality(G)
    tot_betweenness = nx.betweenness_centrality(G,weight=None)

    for node in driverNodes:
        degrees.append(tot_degree[node])
        betweenness.append(tot_betweenness[node])

    with open("results/driver_degree_WS.txt", "w") as f:
        for x in degrees:
            print >> f, x
    with open("results/driver_betweenness_WS.txt", "w") as f:
        for x in betweenness:
            print >> f, x

    with open("results/tot_degree_WS.txt", "w") as f:
        for key, value in tot_degree.iteritems():
            print >> f, value

    with open("results/tot_betweenness_WS.txt", "w") as f:
        for key, value in tot_betweenness.iteritems():
            print >> f, value

def correlation_betweenness_degree_on_NW():
    n = 1000
    k = 4
    p = 0.01
    G = nx.newman_watts_strogatz_graph(n, k, p)

    print nx.info(G)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    print "ND = ", ND
    print "ND lambda:", ND_lambda
    ND, driverNodes = ECT.get_driver_nodes(G)
    print "ND =", ND

    degrees = []
    betweenness = []

    tot_degree = nx.degree_centrality(G)
    tot_betweenness = nx.betweenness_centrality(G,weight=None)

    for node in driverNodes:
        degrees.append(tot_degree[node])
        betweenness.append(tot_betweenness[node])

    with open("results/driver_degree_NW.txt", "w") as f:
        for x in degrees:
            print >> f, x
    with open("results/driver_betweenness_NW.txt", "w") as f:
        for x in betweenness:
            print >> f, x

    with open("results/tot_degree_NW.txt", "w") as f:
        for key, value in tot_degree.iteritems():
            print >> f, value

    with open("results/tot_betweenness_NW.txt", "w") as f:
        for key, value in tot_betweenness.iteritems():
            print >> f, value

def correlation_betweenness_degree_on_BA():
    n = 1000
    m = 2
    G = nx.barabasi_albert_graph(n, m)

    print nx.info(G)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    print "ND = ", ND
    print "ND lambda:", ND_lambda
    ND, driverNodes = ECT.get_driver_nodes(G)
    print "ND =", ND

    degrees = []
    betweenness = []
    tot_degree = nx.degree_centrality(G)
    tot_betweenness = nx.betweenness_centrality(G,weight=None)

    for node in driverNodes:
        degrees.append(tot_degree[node])
        betweenness.append(tot_betweenness[node])

    with open("results/driver_degree_BA.txt", "w") as f:
        for x in degrees:
            print >> f, x
    with open("results/driver_betweenness_BA.txt", "w") as f:
        for x in betweenness:
            print >> f, x
    with open("results/tot_degree_BA.txt", "w") as f:
        for key, value in tot_degree.iteritems():
            print >> f, value

    with open("results/tot_betweenness_BA.txt", "w") as f:
        for key, value in tot_betweenness.iteritems():
            print >> f, value

def correlation_betweenness_degree_on_USAirNetwork():
    G = nx.read_pajek("dataset/USAir97.net")

    print nx.info(G)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    print "ND = ", ND
    print "ND lambda:", ND_lambda
    ND, driverNodes = ECT.get_driver_nodes(G)
    print "ND =", ND

    degrees = []
    betweenness = []
    tot_degree = nx.degree_centrality(G)
    tot_betweenness = nx.betweenness_centrality(G,weight=None)

    for node in driverNodes:
        degrees.append(tot_degree[node])
        betweenness.append(tot_betweenness[node])

    with open("results/driver_degree_USAir.txt", "w") as f:
        for x in degrees:
            print >> f, x
    with open("results/driver_betweenness_USAir.txt", "w") as f:
        for x in betweenness:
            print >> f, x
    with open("results/tot_degree_USAir.txt", "w") as f:
        for key, value in tot_degree.iteritems():
            print >> f, value

    with open("results/tot_betweenness_USAir.txt", "w") as f:
        for key, value in tot_betweenness.iteritems():
            print >> f, value

def correlation_betweenness_degree_on_ErdosNetwork():
    G = nx.read_pajek("dataset/Erdos971.net")
    isolated_nodes = nx.isolates(G)
    G.remove_nodes_from(isolated_nodes)

    print nx.info(G)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    print "ND = ", ND
    print "ND lambda:", ND_lambda
    ND, driverNodes = ECT.get_driver_nodes(G)
    print "ND =", ND

    degrees = []
    betweenness = []
    tot_degree = nx.degree_centrality(G)
    tot_betweenness = nx.betweenness_centrality(G,weight=None)

    for node in driverNodes:
        degrees.append(tot_degree[node])
        betweenness.append(tot_betweenness[node])

    with open("results/driver_degree_Erdos.txt", "w") as f:
        for x in degrees:
            print >> f, x
    with open("results/driver_betweenness_Erdos.txt", "w") as f:
        for x in betweenness:
            print >> f, x
    with open("results/tot_degree_Erdos.txt", "w") as f:
        for key, value in tot_degree.iteritems():
            print >> f, value

    with open("results/tot_betweenness_Erdos.txt", "w") as f:
        for key, value in tot_betweenness.iteritems():
            print >> f, value

if __name__ == "__main__":
    #print ">>> start run on USAir"
    #start_time = time.time()
    #correlation_betweenness_degree_on_USAirNetwork()
    #print ">>>cost time %s seconds" %(time.time() - start_time)

    #print ">>> start run on Erdos"
    #start_time = time.time()
    #correlation_betweenness_degree_on_ErdosNetwork()
    #print ">>>cost time %s seconds" %(time.time() - start_time)

    #print ">>> start run on ER"
    #start_time = time.time()
    #correlation_betweenness_degree_on_ER()
    #print ">>>cost time %s seconds" %(time.time() - start_time)

    print ">>> start run on WS"
    start_time = time.time()
    correlation_betweenness_degree_on_WS()
    print ">>>cost time %s seconds" %(time.time() - start_time)

    print ">>> start run on NW"
    start_time = time.time()
    correlation_betweenness_degree_on_NW()
    print ">>>cost time %s seconds" %(time.time() - start_time)

    print ">>> start run on BA"
    start_time = time.time()
    correlation_betweenness_degree_on_BA()
    print ">>>cost time %s seconds" %(time.time() - start_time)