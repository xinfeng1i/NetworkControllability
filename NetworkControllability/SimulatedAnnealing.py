import networkx as nx
import matplotlib.pyplot as plt
import exact_controllability as ECT
from networkx.utils import powerlaw_sequence
import operator
import random
import csv
import copy
import subprocess, os
import time
import math
import sys
import strutral_controllability as SCT
import NetworkModels as NM
import UtilityFunctions as UF

def test_cost_function(G, target):
    H = G.to_undirected()
    return math.fabs(nx.transitivity(H) - target)

def betweenness_centrality_cost_function(G, target):
    return math.fabs(UF.average_betweenness_centrality(G) - target)

def closeness_centrality_cost_function(G, target):
    return math.fabs(UF.average_closeness_centrality(G) - target)

def eigenvector_centrality_cost_function(G, target):
    return math.fabs(UF.average_eigenvector_centrality(G) - target)

def combination_betweenness_closeness_centrality_cost_function(G, target):
    return math.fabs(UF.closeness_betweenness_combination_centrality(G) - target)

#
# We use degree preserving rewiring to add each network characteristic. Suppose
# that the chosen network characteristic is quantified by a metric 'X'. To set its
# value to be 'X*', we define the E(X) = |X-X*| energy, so E(X*) is a global minimum.
# we minimize this energy by simulating annealing: 
# (1) choose two links at random with uniform probability;
# (2) rewire the two links and calculate the energy E(x) of the resulted network;
# (3) accept the new configuration with probability
#     p = {1} if \Delta E <= 0
#       = e^{-\beta \Delta E}, if Delta E > 0
# where the beta parameter is the inverse temperature
# (4) repeat from step (1) and gradually increasing \beta
# Stop if |E(x) - E(x*)| is smaller than a predefined value    
def SimulatedAnnealing(G, target, cost_functon):
    X = []
    Y = []
    Y2 = []
    T_MAX = 0.01
    #T_MIN = 0.0001
    T_MIN = 0.00001
    ERROR_EPS = 1E-4
    #cooling_rate = 0.995
    cooling_rate = 0.99
    T = T_MAX
    g_best_cost = cost_functon(G, target)
    g_best_graph = G.copy()

    iteration_times = 0
    old_cost = cost_functon(G, target)
    while T > T_MIN:       
        #print 'T = ', T, 'iter = ', iteration_times, 'clustering = ', nx.transitivity(G)
        #print 'iteration = ', iteration_times, ' cost = ', old_cost
        X.append(iteration_times)
        Y.append(old_cost)
        H = G.to_undirected()
        Y2.append(nx.transitivity(H))
        
        found_best_cost = False        
        # Step 1: rewiring two links       
        for inner_loop_cnt in range(1):
            while True:
                edges = G.edges()
                random.shuffle(edges)
                (u1, v1) = edges[0]
                (u2, v2) = edges[1]
                if u1 != v1 and u1 != u2 and u1 != v2 \
                    and v1 != u2 and v1 != v2 \
                    and u2 != v2 \
                    and (not G.has_edge(u1, v2)) and (not G.has_edge(u2, v1)):
                    G.remove_edge(u1, v1)
                    G.remove_edge(u2, v2)
                    G.add_edge(u1, v2)
                    G.add_edge(u2, v1)
                    break
                #if G.has_edge(u2, v1) or G.has_edge(u1, v2):
                #    continue
                #else:
                #    G.remove_edge(u1, v1)
                #    G.remove_edge(u2, v2)
                #    G.add_edge(u1, v2)
                #    G.add_edge(u2, v1)
                #    break
            
            # Step 2: calcualte new configuration energy E(x) = |X-X*|
            new_cost = cost_functon(G, target)
            if new_cost < g_best_cost:
                g_best_cost = new_cost
                g_best_graph = G.copy()

            # Step 3: if find acceptable best solution, return
            if new_cost < ERROR_EPS:
                found_best_cost = True
                break
            
            diff_cost = new_cost - old_cost
            # Step 4: if current solution is better than last solution, accept 
            #         else accept worse solution with P = exp(-deltaE / T)
            if diff_cost < 0:
                old_cost = new_cost
            else:
                accept_prob = math.exp(-(diff_cost + 0.0) / (T * (inner_loop_cnt + 1)))
                r = random.random()
                #print 'accept probability = ', accept_prob
                #print 'r = ', r
                if r < accept_prob:
                    old_cost = new_cost
                else: # reject this solution
                    G.add_edge(u1, v1)
                    G.add_edge(u2, v2)
                    G.remove_edge(u1, v2)
                    G.remove_edge(u2, v1)               
        
        if found_best_cost == True:
            break                             
        # Step 5: update temperature T = annealing_rate * T
        #         if T >= T_min, goto step 1; else terminate algorithm
        iteration_times = iteration_times + 1
        T = cooling_rate * T
    if found_best_cost == True:
        return G
    else:
        return g_best_graph

def ClusteringCoefficientCentralityExperiment(G, min_target, max_target, filename):
    print nx.info(G)
    print 'Global Clustering Coefficient:', nx.transitivity(G.to_undirected())

    X_Clustering_Coefficient = []
    Y_nD = []
    target = min_target
    while target <= max_target:       
        copyG = G.copy()
        new_G = SimulatedAnnealing(copyG, target, test_cost_function)
        clustering_coeff = nx.transitivity(new_G.to_undirected())
        nD = SCT.controllability(new_G)
        X_Clustering_Coefficient.append(clustering_coeff)
        Y_nD.append(nD)
        print "target = ", target, " CC = ", clustering_coeff, 'nD = ', nD      
        target += 0.05
    
    s = 'results/' + filename;
    with open(s, "w") as f:
        for i in range(len(Y_nD)):
            print >> f, "%f %f"%(X_Clustering_Coefficient[i], Y_nD[i])
    return (X_Clustering_Coefficient, Y_nD)

def BetweennessCentralityExperiment(G, min_target, max_target, filename):
    print nx.info(G)
    print 'average betweenness centrality: ', UF.average_betweenness_centrality(G)

    X_betweenness_centrality = []
    Y_nD = []

    target = min_target
    while target <= max_target:       
        copyG = G.copy()
        new_G = SimulatedAnnealing(copyG, target, betweenness_centrality_cost_function)
        betweenness_centrality = UF.average_betweenness_centrality(new_G)
        nD = SCT.controllability(new_G)

        X_betweenness_centrality.append(betweenness_centrality)
        Y_nD.append(nD)

        print "target = ", target, " BC = ", betweenness_centrality, 'nD = ', nD
        
        target += 0.01

    s = 'results/' + filename
    with open(s, "w") as f:
        for i in range(len(Y_nD)):
            print >> f, "%f %f"%(X_betweenness_centrality[i], Y_nD[i])

    return (X_betweenness_centrality, Y_nD)

def ClosenessCentralityExperiment(G, min_target, max_target, filename):
    print nx.info(G)
    print 'average closeness centrality: ', UF.average_closeness_centrality(G)

    X_closeness_centrality = []
    Y_nD = []

    target = min_target
    while target <= max_target:       
        copyG = G.copy()
        new_G = SimulatedAnnealing(copyG, target, closeness_centrality_cost_function)
        closeness_centrality = UF.average_closeness_centrality(new_G)
        nD = SCT.controllability(new_G)

        X_closeness_centrality.append(closeness_centrality)
        Y_nD.append(nD)

        print "target = ", target, " ClosenessC = ", closeness_centrality, 'nD = ', nD       
        target += 0.05

    s = 'results/' + filename
    with open(s, "w") as f:
        for i in range(len(Y_nD)):
            print >> f, "%f %f"%(X_closeness_centrality[i], Y_nD[i])
    return (X_closeness_centrality, Y_nD)

def EigenvectorCentralityExperiment(G, min_target, max_target, filename):
    print nx.info(G)
    print 'average eigenvector centrality: ', UF.average_eigenvector_centrality(G)

    X_eigenvector_centrality = []
    Y_nD = []

    target = min_target
    while target <= max_target:       
        copyG = G.copy()
        new_G = SimulatedAnnealing(copyG, target, eigenvector_centrality_cost_function)
        eigenvector_centrality = UF.average_eigenvector_centrality(new_G)
        nD = SCT.controllability(new_G)

        X_eigenvector_centrality.append(eigenvector_centrality)
        Y_nD.append(nD)

        print "target = ", target, " EC = ", eigenvector_centrality, 'nD = ', nD
        
        target += 0.01

    s = 'results/' + filename
    with open(s, "w") as f:
        for i in range(len(Y_nD)):
            print >> f, "%f %f"%(X_eigenvector_centrality[i], Y_nD[i])

    return (X_eigenvector_centrality, Y_nD)

def CombinationBetweennessClosenessExperiments(G, min_target, step, max_target, filename):
    print nx.info(G)
    print "Combination Indicator X :", UF.closeness_betweenness_combination_centrality(G)

    X_centrality = []
    Y_nD = []

    target = min_target
    while target <= max_target:
        copyG = G.copy()
        new_G = SimulatedAnnealing(G, target, combination_betweenness_closeness_centrality_cost_function)
        centrality = UF.closeness_betweenness_combination_centrality(new_G)
        nD = SCT.controllability(G)
        X_centrality.append(centrality)
        Y_nD.append(nD)
        print 'target = ', target, "X = ", centrality, "nD = ", nD
        target += step

    s = 'results/' + filename
    with open(s, "w") as f:
        for i in range(len(Y_nD)):
            print >> f, "%f %f"%(X_centrality[i], Y_nD[i])

    return (X_centrality, Y_nD)


if __name__ == "__main__":
    #sys.stdout = open("test.txt", "w")
    #H = nx.erdos_renyi_graph(100, 0.03, directed=True)
    #H = nx.erdos_renyi_graph(200, 0.015, directed=True)
    #H = NM.directed_newman_watts_strogatz_graph(100, 2, 0.3)
    #H = NM.directed_barabasi_albert_graph(100, 2)

    #X = [];
    #Y = [];
    #n = 10
    #for i in range(n):
    #    print 'i = ', i
    #    H = nx.erdos_renyi_graph(1000, 0.012, seed=i+1, directed=True)
    #    #target = 0.33
    #    #new_G = SimulatedAnnealing(H, target, betweenness_centrality_cost_function)

    #    combine = UF.closeness_betweenness_combination_centrality(H)
    #    nD = SCT.controllability(H)

    #    X.append(combine)
    #    Y.append(nD)
    #fh = open("test.txt", "w");
    #for i in range(n):
    #    print >> fh, '%f\t%f'%(X[i], Y[i])
    #fh.close();
    
    #####################################################################
    # Betweenness centrality on ND
    ######################################################################
    #print '************************ INIT INFO ************************\n'
    #print nx.info(H)
    #print 'average betweenness centrality: ', UF.average_betweenness_centrality(H)
    #print 'Init ND:', SCT.controllability(H)
    #print '************************ INIT INFO ************************\n'

    #target = 0.020
    #new_G = SimulatedAnnealing(H, target, betweenness_centrality_cost_function)
    #betweenness_centrality = UF.average_betweenness_centrality(new_G)
    #nD = SCT.controllability(new_G)
    #print 'Target = ', target
    #print 'Average Betweenness Centrality: ', betweenness_centrality
    #print 'nD: ', nD

    #X_betweenness_centrality = []
    #Y_nD = []

    #target = 0.01
    #while target <= 0.3:       
    #    G = H.copy()
    #    new_G = SimulatedAnnealing(G, target, betweenness_centrality_cost_function)
    #    betweenness_centrality = UF.average_betweenness_centrality(new_G)
    #    nD = SCT.controllability(new_G)

    #    X_betweenness_centrality.append(betweenness_centrality)
    #    Y_nD.append(nD)

    #    print "target = ", target, " BC = ", betweenness_centrality, 'nD = ', nD
        
    #    target += 0.01

    #with open('results/ND_BC.txt', "w") as f:
    #    for i in range(len(Y_nD)):
    #        print >> f, "%f %f"%(X_betweenness_centrality[i], Y_nD[i])

    ## ER Networks
    #n = 100
    #p = 0.04

    #prefix = 'ER_'
    #G = nx.erdos_renyi_graph(n, p, directed=True)

    #filename = prefix + 'Closeness_n%dp%f'%(n,p)
    #ClosenessCentralityExperiment(G, 0.1, 0.6, filename)

    #n = 100
    #for p in [0.01, 0.02, 0.03, 0.04, 0.05]:
    #    G = nx.erdos_renyi_graph(n, p, directed=True)       
    #    filename = "ER_CombinationX_n%dp%f"%(n,p)
    #    CombinationBetweennessClosenessExperiments(G, 0.05, 0.05, 0.8, filename)
    

    ### NW Networks
    #n = 100
    #for k in range(2, 8, 2):
    #    for p in [0.1, 0.2, 0.3]:
    #        G = NM.directed_newman_watts_strogatz_graph(n, k, p)
    #        filename = "NW_CombinationX_n%dK%dp%f"%(n,k,p)
    #        CombinationBetweennessClosenessExperiments(G, 0.05, 0.05, 0.99, filename)

    ## BA Networks
    #n = 100
    #for m in range(2, 6):
    #    G = NM.directed_barabasi_albert_graph(n, m)
    #    filename = "BA_CombinationX_n%dm%d"%(n, m)
    #    CombinationBetweennessClosenessExperiments(G, 0.05, 0.05, 0.99, filename)
    n = 1000;
    m = 3;
    G = NM.directed_barabasi_albert_graph(n, m)
    combine = UF.closeness_betweenness_combination_centrality(G)
    nD = SCT.controllability(G)
    print '************************ INIT INFO ************************\n'
    print nx.info(G)
    print 'average X: ', combine
    print 'Init ND:', nD
    print '************************ INIT INFO ************************\n'
    target = 0.15
    new_G = SimulatedAnnealing(G, target, betweenness_centrality_cost_function)
    combine = UF.closeness_betweenness_combination_centrality(new_G)
    nD = SCT.controllability(new_G)

