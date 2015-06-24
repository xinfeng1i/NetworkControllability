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
    
def SimulatedAnnealing(G, target, cost_functon):
    X = []
    Y = []
    Y2 = []
    T_MAX = 0.01
    T_MIN = 0.0001
    ERROR_EPS = 1E-4
    cooling_rate = 0.995
    T = T_MAX
    iteration_times = 0

    old_cost = cost_functon(G, target)
    while T > T_MIN:       
        #print 'T = ', T, 'iter = ', iteration_times, 'clustering = ', nx.transitivity(G)
        X.append(iteration_times)
        Y.append(old_cost)
        H = G.to_undirected()
        Y2.append(nx.transitivity(H))
        
        found_best_cost = False        
        # Step 1: rewiring two links       
        for inner_loop_cnt in range(10):
            while True:
                edges = G.edges()
                random.shuffle(edges)
                (u1, v1) = edges[0]
                (u2, v2) = edges[1]
                if G.has_edge(u2, v1) or G.has_edge(u1, v2):
                    continue
                else:
                    G.remove_edge(u1, v1)
                    G.remove_edge(u2, v2)
                    G.add_edge(u1, v2)
                    G.add_edge(u2, v1)
                    break
            
            # Step 2: calcualte new configuration energy E(x) = |X-X*|
            new_cost = cost_functon(G, target)

            # Step 3: if find acceptable best solution, return
            if new_cost < ERROR_EPS:
                found_best_cost = True
                break
            
            diff_cost = new_cost - old_cost
            # Step 4: if current solution is better than last solution, accept 
            #         else accept worse solution with P = exp(-deltaE / T)
            if (diff_cost - 0.0) < ERROR_EPS:
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
    return G

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

if __name__ == "__main__":
    #sys.stdout = open("test.txt", "w")
    #H = nx.erdos_renyi_graph(100, 0.03, directed=True)
    #H = NM.directed_newman_watts_strogatz_graph(100, 2, 0.3)
    H = NM.directed_barabasi_albert_graph(100, 2)
    
    #####################################################################
    # Betweenness centrality on ND
    ######################################################################
    #print nx.info(H)
    #print 'average betweenness centrality: ', UF.average_betweenness_centrality(H)

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
    

    ### NW Networks
    #prefix = 'NW_'
    #n = 100
    #k = 2
    #p = 0.2
    #while k <= 6:
    #    G = NM.directed_newman_watts_strogatz_graph(n, k, p)

    #    filename = prefix + 'Closeness_n%dk%dp%f'%(n,k,p)
    #    ClosenessCentralityExperiment(G, 0.01, 0.3,filename)
    #    k += 2;

    ## BA Networks
    prefix = 'BA_'
    n = 100
    m = 2
    while m <= 4:
        G = NM.directed_barabasi_albert_graph(n, m)
        filename = prefix + 'Betweenness_n%dm%d'%(n, m)
        BetweennessCentralityExperiment(G, 0.01,0.3,filename)
        m += 1