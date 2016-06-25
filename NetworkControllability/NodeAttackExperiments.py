

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
import NetworkModels as NM


def NodeAttackonER():
    start_time = time.time()
  
    n = 200
    fraction = 0.2
    N_rm = int(n * fraction)
    p = 0.02
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack1_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack2_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack3_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack4_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack5_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def NodeAttackonSW():
    start_time = time.time()
  
    n = 200
    k = 4
    fraction = 0.2
    N_rm = int(n * fraction)
    p = 0.1
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack1_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack2_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack3_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack4_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack5_SW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def NodeAttackonNW():
    start_time = time.time()
  
    n = 200
    fraction = 0.2
    N_rm = int(n * fraction)
    k = 4
    p = 0.1
    run_cnt = 50

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack1_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack2_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack3_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack4_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack5_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def NodeAttackonBA():
    start_time = time.time()
  
    n = 200
    fraction = 0.2
    N_rm = int(n * fraction)
    m = 3
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack1_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack2_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack3_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack4_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed = rndseed + 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack5_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def NodeAttackonUSAir():
    start_time = time.time()
  
    n = 332
    fraction = 0.2
    N_rm = int(n * fraction)
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 1;
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        random.seed(rndseed)
        ND1, T1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1;

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack1_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 10
    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack2_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 10
    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack3_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    run_cnt = 10
    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack4_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 10
    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack5_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def NodeAttackonErdosNetwork():
    start_time = time.time()
  
    n = 429
    fraction = 0.2
    N_rm = int(n * fraction)
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    rndseed = 1
    for i in range(run_cnt):
        # u"????¡À???¡Á??¨®???¡§¡Á???¡Á¡Â??????????"
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)

        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        random.seed(rndseed)
        ND1, T1 = RandomNodeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack1_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 1
    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)

        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack2_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    run_cnt = 1
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)

        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack3_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    run_cnt = 1
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)

        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack4_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    run_cnt = 1
    tot_ND1 = [0] * (N_rm + 1)
    tot_T1 = [0] * (N_rm + 1)
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)

        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedNodeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (n + 0.0) for x in tot_T1]

    with open("results2/node_attack5_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)



if __name__ == "__main__":
    #NodeAttackonUSAir()
    #NodeAttackonErdosNetwork()
    #n = 200
    #fraction = 0.2
    #N_rm = int(n * fraction)
    #rndseed = 0
    #G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
    #all_nodes = nx.nodes(G1)
    #random.shuffle(all_nodes)
    #for i in range(N_rm):
    #    node = all_nodes[i]
    #    G1.remove_node(node)
    #    nx.connected.connected_component_subgraphs(G1)
    font = {'family' : 'Arial', 
        'weight' : 'normal',
        }  
    X = []
    Y = []
    #n = 200
    #k = 4
    #fraction = 0.2
    #N_rm = int(n * fraction)
    #p = 0.1
    #rndseed = 0
    #G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
    
    #degs = nx.degree(G1)
    #sorted_degs = sorted(degs, key=degs.get, reverse=True)
    #print sorted_degs;

    # u"?????????????¡Â????????"
    #node1 = sorted_degs[0];
    #sorted_degs.remove(node1);
    #print sorted_degs;
    #G1.remove_node(node1);
    # u"????????????¡Á??¨®?????¡Â????????"
    #for i in range(4):
    #    degs = nx.degree(G1)
    #    max_degree_node = max(degs, key = degs.get)
    #    print "max degree node ", max_degree_node
    #    G1.remove_node(max_degree_node)

    #nx.draw_circular(G1,with_labels=True);
    #plt.show();

    #for i in range(100):
    #    #G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
    #    #G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
    #    #G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
    #    G1 = nx.barabasi_albert_graph(n, 3, seed=rndseed)
    
    G1 = nx.read_pajek("dataset/USAir97.net")
    #G = nx.read_pajek("dataset/Erdos971_revised.net")
    #G1 = max(nx.connected_component_subgraphs(G),key=len)
    print "After remving: N =", nx.number_of_nodes(G1), "L = ", nx.number_of_edges(G1)
    nodes = nx.nodes(G1)
    degrees = nx.degree(G1)
    betweenness = nx.betweenness_centrality(G1)
    for node in nodes:
        X.append(degrees[node])
        Y.append(betweenness[node])
    #rndseed += 1


    # u"?????¨¦?????¨¤????"
    f = open("results2/USAir97degVsBC.txt", "w");
    print >> f, 'degree betweenness'
    for i in range(len(X)):
        print >> f, "%f %f"%(X[i], Y[i]);
    plt.plot(X, Y, 'b*')
    plt.title('USAir97')
    plt.xlabel('Degree', fontdict=font)
    plt.ylabel('BC', fontdict=font)
    plt.show()

    #APL = nx.average_shortest_path_length(G1)
    #print "APL: ", APL
    #Diameter = nx.diameter(G1)
    #print "Network diameter: ", Diameter;

    # '''plot?¨¦??¡¤???????'''
    #X2 = []
    #Y2 = []
    #betss = Y
    #s = set()
    #for i in Y:
    #    s.add(round(i, ndigits=6));

    #for i in s:
    #    cnti = betss.count(i)
    #    X2.append(i);
    #    Y2.append(cnti)
    #Y2 = [(x+0.0) / (1) for x in Y2]
    #plt.xlabel('BC')
    #plt.ylabel('Freq')
    #plt.title('BA')
    #plt.plot(X2, Y2, 'bo')
    #plt.show()

    # u"plot ??¡¤???"
    #degs = X
    #X2 = []
    #Y2 = []
    #L = list(set(degs))
    #for i in L:
    #    cnti = degs.count(i)
    #    X2.append(i)
    #    Y2.append(cnti)
    #Y2 = [(x+0.0) / (nx.number_of_nodes(G1)) for x in Y2]
    #fh = open("results2/temp.txt", "w")
    #for i in range(len(X2)):
    #    print >> fh, "%d %f"%(X2[i], Y2[i]);
    #plt.xlabel('k')
    #plt.ylabel('P(k)')
    #plt.title('BA')
    #plt.plot(X2, Y2, '-bo')
    #plt.show()

    

    #X3 = []
    #Y3 = []
    #nodes = nx.nodes(G1)
    #random.shuffle(nodes)
    #for i in range(14):
    #    G1.remove_node(nodes[i])
    #degs = nx.degree(G1).values()
    #mindeg = min(degs)
    #maxdeg = max(degs)
    #for i in range(mindeg,maxdeg+1):
    #    cnti = degs.count(i)
    #    X3.append(i)
    #    Y3.append(cnti)
    #plt.plot(X3, Y3, 'r-s')
    #plt.show()
    #NodeAttackonER()
    #NodeAttackonSW()
    #NodeAttackonNW()
    #NodeAttackonBA()
    #NodeAttackonUSAir()
    #NodeAttackonErdosNetwork()
    #G1 = nx.read_pajek("dataset/Erdos971.net")
    #isolated_nodes = nx.isolates(G1)
    #G1.remove_nodes_from(isolated_nodes)
    #nx.write_pajek(G1, "dataset/Erdos971_2.net")

    #G1 = nx.read_pajek("dataset/Erdos971_revised.net")
    #Gcc=sorted(nx.connected_component_subgraphs(G1), key = len, reverse=True)
    #G0=Gcc[0]

    #print "Max Component number : ", nx.number_of_nodes(G0);
    #print "Max Component edges: ", nx.number_of_edges(G0);

    # u"???????????¡Â??¡À¨º????????????r???????????¡ã?¨¬"
    #n = 200
    #k = 6.0
    #r = 2.9
    #fraction = 0.2;
    #Nrm = int(n * fraction);
    #totND = [0] * (Nrm + 1);
    #totT = [0] * (Nrm + 1)

    #runcnt = 5
    #for rndseed in range(runcnt):
    #    random.seed(rndseed)
    #    G = NM.undirected_scale_free_network(n, k, r)      
    #    ND1, T1 = RecalculatedNodeDegreeAttack(G, remove_fraction=fraction);
    #    totND = [x + y for x, y in zip(totND, ND1)]

    #totND = [(x + 0.0) / (runcnt * n) for x in totND];
    #totT = T1;
    #totT = [(x + 0.0) / n for x in totT]

    #plt.plot(totT, totND, '-bo');
    #plt.show();
