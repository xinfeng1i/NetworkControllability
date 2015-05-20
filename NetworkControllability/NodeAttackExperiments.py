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
from ControllabilityRobustnessBasedOnNodeAttack import RandomNodeAttack
from ControllabilityRobustnessBasedOnNodeAttack import InitialNodeDegreeAttack
from ControllabilityRobustnessBasedOnNodeAttack import RecalculatedNodeDegreeAttack
from ControllabilityRobustnessBasedOnNodeAttack import InitialNodeBetweennessAttack
from ControllabilityRobustnessBasedOnNodeAttack import RecalculatedNodeBetweennessAttack


def NodeAttackonER():
    start_time = time.time()
  
    n = 200
    fraction = 0.2
    N_rm = int(n * fraction)
    p = 0.02
    run_cnt = 30

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1, giant1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack1_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack2_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack3_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack4_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack5_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def NodeAttackonSW():
    start_time = time.time()
  
    n = 200
    k = 4
    fraction = 0.2
    N_rm = int(n * fraction)
    p = 0.02
    run_cnt = 30

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1, giant1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack1_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack2_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack3_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack4_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack5_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def NodeAttackonNW():
    start_time = time.time()
  
    n = 200
    fraction = 0.2
    N_rm = int(n * fraction)
    k = 4
    p = 0.02
    run_cnt = 30

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1, giant1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack1_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack2_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack3_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack4_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack5_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def NodeAttackonBA():
    start_time = time.time()
  
    n = 200
    fraction = 0.2
    N_rm = int(n * fraction)
    m = 3
    run_cnt = 30

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1, giant1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack1_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack2_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack3_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack4_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results/node_attack5_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

if __name__ == "__main__":
    NodeAttackonER()
    NodeAttackonSW()
    NodeAttackonNW()
    NodeAttackonBA() 