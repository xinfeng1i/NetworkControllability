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

def test_cost_function(G, target):
    H = G.to_undirected()
    return math.fabs(nx.transitivity(H) - target)
    
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
                print 'accept probability = ', accept_prob
                print 'r = ', r
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
    return (X, Y, Y2)


if __name__ == "__main__":
    #sys.stdout = open("test.txt", "w")
    H = nx.erdos_renyi_graph(100, 0.02, directed=True)
    print nx.info(H)
    target = 0.3
    (XX, YY, YY2) = SimulatedAnnealing(H, target, test_cost_function)
    plt.plot(XX, YY)
    plt.plot(XX, YY2, 'r')
    plt.show()
    
    #target = 0.002
    #while target < 0.02:
    #    G = H.copy()
    #    new_G = SimulatedAnnealing(G, target, test_cost_function)
    #    nD = SCT.controllability(new_G)
    #    print 'C = ', nx.transitivity(new_G), 'nD = ', nD

    #    target += 0.002
      
    #print 'final clustering:', nx.transitivity(G)