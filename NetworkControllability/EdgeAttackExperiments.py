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
import numpy as np
from ControllabilityRobustnessBasedOnEdgeAttack import RandomEdgeAttack
from ControllabilityRobustnessBasedOnEdgeAttack import InitialEdgeDegreeAttack
from ControllabilityRobustnessBasedOnEdgeAttack import RecalculatedEdgeDegreeAttack
from ControllabilityRobustnessBasedOnEdgeAttack import InitialEdgeBetweennessAttack
from ControllabilityRobustnessBasedOnEdgeAttack import RecalculatedEdgeBetweennessAttack

def EdgeAttackER():
    start_time = time.time()
  
    n = 200
    fraction = 0.2
    E = 400
    E_rm = 80
    p = 0.02
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RandomEdgeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack1_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack2_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack3_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack4_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.erdos_renyi_graph(n, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack5_ER.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def EdgeAttackSW():
    start_time = time.time()

    n = 200
    k = 4
    p = 0.1
    fraction = 0.2
    E = 400
    E_rm = 80
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RandomEdgeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack1_WS.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack2_WS.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack3_WS.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack4_WS.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack5_WS.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def EdgeAttackNW():
    start_time = time.time()

    n = 200
    k = 4
    p = 0.1
    fraction = 0.2
    E = 440
    E_rm = 88
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RandomEdgeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack1_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack2_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack3_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack4_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.newman_watts_strogatz_graph(n, k, p, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack5_NW.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def EdgeAttackBA():
    start_time = time.time()

    n = 200
    m = 3
    fraction = 0.2
    E = 591
    E_rm = 118
    run_cnt = 100

    #******** Run Node Attack 1 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RandomEdgeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack1_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 2 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack2_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 3 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack3_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))


    #******** Run Node Attack 4 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack4_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    #******** Run Node Attack 5 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 0
    for i in range(run_cnt):
        G1 = nx.barabasi_albert_graph(n, m, seed=rndseed)
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack5_BA.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def EdgeAttackUSAir():
    start_time = time.time()
  
    n = 332
    fraction = 0.2
    E = 2126
    E_rm = int(0.2 * E)
    run_cnt = 100

    #******** Run Edge Attack 1 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 1;
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        random.seed(rndseed)
        ND1, T1 = RandomEdgeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1;

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack1_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 3
    #******** Run Edge Attack 2 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack2_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 3
    #******** Run Edge Attack 3 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack3_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 3
    #******** Run Edge Attack 4 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack4_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 3
    #******** Run Edge Attack 5 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    for i in range(run_cnt):
        G1 = nx.read_pajek("dataset/USAir97.net")
        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack5_USAir.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)

def EdgeAttackErdosNetwork():
    start_time = time.time()
  
    n = 429
    fraction = 0.2
    E = 1312
    E_rm = int(0.2 * E)
    run_cnt = 100

    #******** Run Edge Attack 1 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    rndseed = 1
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)
        print ">>>>>>>>>>>>>>> Random Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        random.seed(rndseed)
        ND1, T1 = RandomEdgeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]
        rndseed += 1

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack1_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 3
    #******** Run Edge Attack 2 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)
        print ">>>>>>>>>>>>>>> Initial Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack2_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 3
    #******** Run Edge Attack 3 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)
        print ">>>>>>>>>>>>>>> Recalculated Degree Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeDegreeAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack3_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 3
    #******** Run Edge Attack 4 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)
        print ">>>>>>>>>>>>>>> Initial Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = InitialEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack4_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    run_cnt = 3
    #******** Run Edge Attack 5 ********#
    tot_ND1 = [0] * (E_rm + 1)
    tot_T1 = [0] * (E_rm + 1)
    for i in range(run_cnt):
        G = nx.read_pajek("dataset/Erdos971_revised.net")
        G1 = max(nx.connected_component_subgraphs(G),key=len)

        print ">>>>>>>>>>>>>>> Recalculated Betweenness Attack run time count: ", i + 1, "<<<<<<<<<<<<<<<<<<"
        print "graph info", nx.info(G1)
        ND1, T1 = RecalculatedEdgeBetweennessAttack(G1, remove_fraction=fraction)
        tot_ND1 = [x + y for x, y in zip(tot_ND1, ND1)]

    tot_ND1 = [((x + 0.0) / run_cnt) for x in tot_ND1]
    tot_T1 = T1
    tot_ND1 = [(x + 0.0) / (n + 0.0) for x in tot_ND1]
    tot_T1 = [(x + 0.0) / (E + 0.0) for x in tot_T1]

    with open("results2/edge_attack5_ErdosNetwork.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(tot_T1, tot_ND1))

    print "--- cost time %s seconds ---" %(time.time() - start_time)


def PlotNodeDegreeDistribution(G):
    deg = nx.degree(G).values()
    L = list(set(deg))
    cnt = {}
    for x in L:
        cnt[x] = deg.count(x)
    X = []
    Y = []
    for k, v in cnt.items():
        X.append(k)
        Y.append(v)
    print 'H = ', np.std(deg)
    print '<k> = ', sum(deg) / (G.number_of_nodes() + 0.0)
    #print 'Diameter = ', nx.diameter(G)
    #print 'APL = ', nx.average_shortest_path_length(G)
    print '<B> = ', sum (nx.betweenness_centrality(G).values()) / (G.number_of_nodes() + 0.0)
    print '<C> = ', sum (nx.closeness_centrality(G).values()) / (G.number_of_nodes() + 0.0)
    #print 'X = ', X
    #print 'Y = ', Y 
    plt.plot(X, Y, 'bo')
    plt.show()


if __name__ == "__main__":
    #EdgeAttackER()
    #EdgeAttackSW()
    #EdgeAttackNW()
    #EdgeAttackBA()
    #EdgeAttackUSAir()
    #EdgeAttackErdosNetwork()
    
    # """Plot betweenness-degree correlation"""
    #rndseed = 0
    #X = []
    #Y = []
    #for i in range(50):
    #    G = nx.erdos_renyi_graph(200, 0.02, seed=rndseed)
    #    rndseed += 1
    #    all_betweenness = nx.edge_betweenness_centrality(G)
    #    all_degree = nx.degree(G)
    #    for (u, v) in G.edges():
    #        betweenness = all_betweenness[(u, v)]
    #        edge_degree = all_degree[u] * all_degree[v]
    #        X.append(edge_degree)
    #        Y.append(betweenness)
    #plt.plot(X, Y, '*')
    #plt.show()

    # """Plot edge degree distribution"""
    #unique_deg = list(set(X))
    #count_dict = {}
    #for deg in unique_deg:
    #    count_dict[deg] = X.count(deg)
    #for (k, v) in count_dict.items():
    #    plt.plot(k, v, 'bo')
    #plt.show()
    #print count_dict

    # """Initial edge degree attack"""
    G = nx.erdos_renyi_graph(200, 4.0/199.0, seed=1)
    #G = nx.watts_strogatz_graph(200, 4, 0.1, seed=999)
    #G = nx.newman_watts_strogatz_graph(200, 4, 0.1, seed=999)
    #G = nx.barabasi_albert_graph(200, 3, seed=999)
    #G = nx.read_pajek("dataset/USAir97.net") # USAir97
    #G_origal = nx.read_pajek("dataset/Erdos971_revised.net") # Erdos971
    #G = max(nx.connected_component_subgraphs(G_origal),key=len) # Erdos971

    E = G.number_of_edges()
    print 'N = ', G.number_of_nodes(), 'E=', G.number_of_edges()
    all_betweenness = nx.edge_betweenness_centrality(G)
    all_degree = nx.degree(G)
    all_edge_degree = {}
    PlotNodeDegreeDistribution(G)
    
    #Calculate the initial edge degree
    for (u, v) in G.edges():
        tmp = all_degree[u] * all_degree[v]
        all_edge_degree[(u, v)] = tmp
    sorted_edge_degree = sorted(all_edge_degree, key=all_edge_degree.get, reverse=True)

    # Calculate the initial Edge Betweenness
    all_edge_betweenness = nx.edge_betweenness_centrality(G)
    sorted_edge_betweenness = sorted(all_edge_betweenness, key=all_edge_betweenness.get, reverse=True)  
    #print sorted_edge_betweenness
    #for (u, v) in sorted_edge_betweenness:
    #    print ' (', u, ',', v, '):', all_edge_betweenness[(u, v)],



    i = 0
    shortcut = 0
    random_edges = copy.deepcopy(G.edges())
    random.shuffle(random_edges)
    #print random_edges
    
    print '\n', '-' * 10, 'f = 5%', '-' * 10
    while (i < int(0.05 * E)):
        # "IDA Attack"
        #u, v = sorted_edge_degree[i]
        ##print 'u = ', u, 'v = ', v, \
        ##      'k_u = ', all_degree[u], 'k_v = ', all_degree[v], \
        ##      'k_u * k_v = ', all_degree[u] * all_degree[v]
        #G.remove_edge(u, v)
        ##if abs(u-v) > 2:
        ##    print 'shortcut %d -- %d' %(u, v)
        ##    shortcut += 1

        # "RDA Attack"
        #cur_edge_degree = {}
        #for (u, v) in G.edges():
        #    cur_edge_degree[(u, v)] = G.degree(u) * G.degree(v)
        #max_edge_degree = max(cur_edge_degree.values())
        #for (u, v) in G.edges():
        #    if G.degree(u) * G.degree(v) == max_edge_degree:
        #        G.remove_edge(u, v)
        #        break

        #"IBA Attack"
        (u, v) = sorted_edge_betweenness[i]
        G.remove_edge(u, v)


        # "RBA Attack"
        #EdgeBet = nx.edge_betweenness_centrality(G)
        #MaxBet = max(EdgeBet.values())
        #u = -1
        #v = -1
        #for (u, v) in EdgeBet.keys():
        #    if EdgeBet[(u, v)] == MaxBet:
        #        G.remove_edge(u, v)
        #        break

        # "RA Attack"
        #TmpBet = nx.edge_betweenness_centrality(G)
        #u, v = random_edges[i]
        #G.remove_edge(u, v)
        #print 'u = ', u, 'v = ', v, 'C_B = ', TmpBet[(u, v)]
        i += 1
    PlotNodeDegreeDistribution(G)
    #nx.draw_circular(G, with_labels=True)
    #plt.show()
    #print 'shortcut counts : ', shortcut

    print '\n', '-' * 10, 'f = 10%', '-' * 10
    while (i < int(0.1 * E)):
        # "IDA Attack"
        #u, v = sorted_edge_degree[i]
        ##print 'u = ', u, 'v = ', v, \
        ##      'k_u = ', all_degree[u], 'k_v = ', all_degree[v], \
        ##      'k_u * k_v = ', all_degree[u] * all_degree[v]
        #G.remove_edge(u, v)
        ##if abs(u-v) > 2:
        ##    print 'shortcut %d -- %d' %(u, v)
        ##    shortcut += 1

        # "RDA Attack"
        #cur_edge_degree = {}
        #for (u, v) in G.edges():
        #    cur_edge_degree[(u, v)] = G.degree(u) * G.degree(v)
        #max_edge_degree = max(cur_edge_degree.values())
        #for (u, v) in G.edges():
        #    if G.degree(u) * G.degree(v) == max_edge_degree:
        #        G.remove_edge(u, v)
        #        break

        #"IBA Attack"
        (u, v) = sorted_edge_betweenness[i]
        G.remove_edge(u, v)

        # "RBA Attack"
        #EdgeBet = nx.edge_betweenness_centrality(G)
        #MaxBet = max(EdgeBet.values())
        #u = -1
        #v = -1
        #for (u, v) in EdgeBet.keys():
        #    if EdgeBet[(u, v)] == MaxBet:
        #        G.remove_edge(u, v)
        #        break

        # "RA Attack"
        #TmpBet = nx.edge_betweenness_centrality(G)
        #u, v = random_edges[i]
        #G.remove_edge(u, v)
        #print 'u = ', u, 'v = ', v, 'C_B = ', TmpBet[(u, v)]
        i += 1
    PlotNodeDegreeDistribution(G)
    #nx.draw_circular(G, with_labels=True)
    #plt.show()
    #print 'shortcut counts : ', shortcut

    print '\n', '-' * 10, 'f = 15%', '-' * 10
    while (i < int(0.15 * E)):
        # "IDA Attack"
        #u, v = sorted_edge_degree[i]
        ##print 'u = ', u, 'v = ', v, \
        ##      'k_u = ', all_degree[u], 'k_v = ', all_degree[v], \
        ##      'k_u * k_v = ', all_degree[u] * all_degree[v]
        #G.remove_edge(u, v)
        ##if abs(u-v) > 2:
        ##    print 'shortcut %d -- %d' %(u, v)
        ##    shortcut += 1

        # "RDA Attack"
        #cur_edge_degree = {}
        #for (u, v) in G.edges():
        #    cur_edge_degree[(u, v)] = G.degree(u) * G.degree(v)
        #max_edge_degree = max(cur_edge_degree.values())
        #for (u, v) in G.edges():
        #    if G.degree(u) * G.degree(v) == max_edge_degree:
        #        G.remove_edge(u, v)
        #        break

        #"IBA Attack"
        (u, v) = sorted_edge_betweenness[i]
        G.remove_edge(u, v)
        
        # "RBA Attack"
        #EdgeBet = nx.edge_betweenness_centrality(G)
        #MaxBet = max(EdgeBet.values())
        #u = -1
        #v = -1
        #for (u, v) in EdgeBet.keys():
        #    if EdgeBet[(u, v)] == MaxBet:
        #        G.remove_edge(u, v)
        #        break

        # "RA Attack"
        #TmpBet = nx.edge_betweenness_centrality(G)
        #u, v = random_edges[i]
        #G.remove_edge(u, v)
        #print 'u = ', u, 'v = ', v, 'C_B = ', TmpBet[(u, v)]
        i += 1
    PlotNodeDegreeDistribution(G)
    #nx.draw_circular(G, with_labels=True)
    #plt.show()
    #print 'shortcut counts : ', shortcut

    print '\n', '-' * 10, 'f = 20%', '-' * 10
    while (i < int(0.2 * E)):
        # "IDA Attack"
        #u, v = sorted_edge_degree[i]
        ##print 'u = ', u, 'v = ', v, \
        ##      'k_u = ', all_degree[u], 'k_v = ', all_degree[v], \
        ##      'k_u * k_v = ', all_degree[u] * all_degree[v]
        #G.remove_edge(u, v)
        ##if abs(u-v) > 2:
        ##    print 'shortcut %d -- %d' %(u, v)
        ##    shortcut += 1

        # "RDA Attack"
        #cur_edge_degree = {}
        #for (u, v) in G.edges():
        #    cur_edge_degree[(u, v)] = G.degree(u) * G.degree(v)
        #max_edge_degree = max(cur_edge_degree.values())
        #for (u, v) in G.edges():
        #    if G.degree(u) * G.degree(v) == max_edge_degree:
        #        G.remove_edge(u, v)
        #        break

        #"IBA Attack"
        (u, v) = sorted_edge_betweenness[i]
        G.remove_edge(u, v)

        # "RBA Attack"
        #EdgeBet = nx.edge_betweenness_centrality(G)
        #MaxBet = max(EdgeBet.values())
        #u = -1
        #v = -1
        #for (u, v) in EdgeBet.keys():
        #    if EdgeBet[(u, v)] == MaxBet:
        #        G.remove_edge(u, v)
        #        break

        # "RA Attack"
        #TmpBet = nx.edge_betweenness_centrality(G)
        #u, v = random_edges[i]
        #G.remove_edge(u, v)
        #print 'u = ', u, 'v = ', v, 'C_B = ', TmpBet[(u, v)]
        i += 1
    PlotNodeDegreeDistribution(G)
    #print 'shortcuts count = ', shortcut
    #nx.draw_circular(G, with_labels=True)
    #plt.show()
    #print 'shortcut counts : ', shortcut