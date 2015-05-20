import numpy as np
import networkx as nx
import exact_controllability as ECT
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import csv
import operator
import random
import os
import subprocess
import threading


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


if __name__ == "__main__":
    #G = nx.erdos_renyi_graph(50, 0.99)
    G = nx.barabasi_albert_graph(1000, 2)
    #G = nx.watts_strogatz_graph(50, 4, 0.3)
    #G = nx.newman_watts_strogatz_graph(100, 6, 0.5)
    print nx.info(G)
    ND, ND_lambda = ECT.get_number_of_driver_nodes(G)
    print "ND = ", ND
    print "ND lambda:", ND_lambda
    ND, driverNodes = ECT.get_driver_nodes(G)
    print "ND =", ND
    #print "driver nodes", driverNodes

    degrees = []
    betweenness = []
    closeness = []
    eigenvectorcentrality = []

    tot_degree = nx.degree_centrality(G)
    tot_betweenness = nx.betweenness_centrality(G,weight=None)
    #tot_closeness = nx.closeness_centrality(G)

    #tot_eigenvector = nx.eigenvector_centrality(G, max_iter=1000, weight=None)
    for node in driverNodes:
        degrees.append(tot_degree[node])
        betweenness.append(tot_betweenness[node])
        #closeness.append(tot_closeness[node])
        #eigenvectorcentrality.append(tot_eigenvector[node])

    #print degrees
    #print betweenness
    #print closeness
    #print eigenvectorcentrality
    with open("results/degree.txt", "w") as f:
        for x in degrees:
            print >> f, x
    with open("results/betweenness.txt", "w") as f:
        for x in betweenness:
            print >> f, x
    #with open("results/closeness.txt", "w") as f:
    #    for x in closeness:
    #        print >> f, x
    #with open("results/eigenvectorcentrality.txt", "w") as f:
    #    for x in eigenvectorcentrality:
    #        print >> f, x
    #print tot_degree
    with open("results/tot_degree.txt", "w") as f:
        for key, value in tot_degree.iteritems():
            print >> f, value

    with open("results/tot_betweenness.txt", "w") as f:
        for key, value in tot_betweenness.iteritems():
            print >> f, value