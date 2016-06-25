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
import strutral_controllability as SC

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
    run_cnt = 30

    #******** Run Node Attack 1 ********#
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

    run_cnt = 1
    random.seed()
    #******** Run Node Attack 2 ********#
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

    run_cnt = 1
    random.seed()
    #******** Run Node Attack 3 ********#
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

    run_cnt = 1
    random.seed()
    #******** Run Node Attack 4 ********#
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

    run_cnt = 1
    random.seed()
    #******** Run Node Attack 5 ********#
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


def ReadPajek(filename):
    '''Read pajek file to construct DiGraph'''
    G = nx.DiGraph()
    fp = open(filename, 'r')
    line = fp.readline()
    while line:
        if line[0] == '*':
            line = line.strip().split()
            label = line[0]
            number = int(line[1])
            if label == '*Vertices' or label == '*vertices':
                NodeNum = number
                for i in range(NodeNum):
                    NodeLine = fp.readline()
                    NodeLine = NodeLine.strip().split()
                    NodeID = int(NodeLine[0])
                    NodeLabel = NodeLine[1]
                    G.add_node(NodeID)
            elif label == '*Arcs' or label == '*arcs':
                EdgeNum = number
                for i in range(EdgeNum):
                    EdgeLine = fp.readline()
                    EdgeLine = EdgeLine.strip().split()
                    u = int(EdgeLine[0])
                    v = int(EdgeLine[1])
                    #w = float(EdgeLine[2])
                    G.add_edge(u, v)
            else:
                pass
        line = fp.readline()
    fp.close()
    return G

def EdgeAttack(G):
    """ Edge attack experiments on real world networks
        
        Params:
        G: A directed network of networkx
        
        Returns:
        None. Print the network controllability n_D after
              5% 10% 15% 20% edges removed
    """
    NodesNum = G.number_of_nodes()
    EdgesNum = G.number_of_edges()

    # Edge remove fraction F0, F1, F2, F3, F4
    F1 = 0.05
    F2 = 0.10
    F3 = 0.15
    F4 = 0.20
    LRA = []
    LID = []
    LRD = []
    LIB = []
    LRB = []
    # Following is Edge Random Attack (RA)
    print '########## Edge RA ##########'
    G1 = copy.deepcopy(G)
    RandomEdges = copy.deepcopy(G1.edges())
    random.shuffle(RandomEdges)
    i = 0
    while i < int(F1 * EdgesNum):
        u, v = RandomEdges[i]
        G1.remove_edge(u, v)
        i += 1    
    nD = len(SC.control_nodes(G1)) / (NodesNum + 0.0)
    print F1, nD
    LRA.append(nD)
    
    while i < int(F2 * EdgesNum):
        u, v = RandomEdges[i]
        G1.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G1)) / (NodesNum + 0.0)
    print F2, nD
    LRA.append(nD)
    
    while i < int(F3 * EdgesNum):
        u, v = RandomEdges[i]
        G1.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G1)) / (NodesNum + 0.0)
    print F3, nD
    LRA.append(nD)
    
    while i < int(F4 * EdgesNum):
        u, v = RandomEdges[i]
        G1.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G1)) / (NodesNum + 0.0)
    print F4, nD
    LRA.append(nD)
    G1.clear()
    RandomEdges = []

    # Following is Initial Edge Degree Attack (IDA)
    print '########## Edge IDA ##########'
    G2 = copy.deepcopy(G)
    NodeDegrees = nx.degree(G2)
    EdgeDegrees = {}
    for u, v in G2.edges_iter():  # Calculate the edge degrees
        EdgeDegrees[(u, v)] = NodeDegrees[u] * NodeDegrees[v]
    # Sort the edges decrendingly according to edge degree    
    SortedEdges = sorted(EdgeDegrees, key=EdgeDegrees.get, reverse=True)
    i = 0
    while i < int(F1 * EdgesNum):
        u, v = SortedEdges[i]
        G2.remove_edge(u, v)
        i += 1   
    nD = len(SC.control_nodes(G2)) / (NodesNum + 0.0)
    print F1, nD
    LID.append(nD)

    while i < int(F2 * EdgesNum):
        u, v = SortedEdges[i]
        G2.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G2)) / (NodesNum + 0.0)
    print F2, nD
    LID.append(nD)

    while i < int(F3 * EdgesNum):
        u, v = SortedEdges[i]
        G2.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G2)) / (NodesNum + 0.0)
    print F3, nD
    LID.append(nD)

    while i < int(F4 * EdgesNum):
        u, v = SortedEdges[i]
        G2.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G2)) / (NodesNum + 0.0)
    print F4, nD
    LID.append(nD)
    G2.clear()
    NodeDegrees = {}
    EdgeDegrees = {}
    SortedEdges = []

    # Following is Recalculated Edge Degree Attack (RDA)
    print '########## Edge RDA ##########'
    G3 = copy.deepcopy(G)
    i = 0
    while i < int(F1 * EdgesNum):
        # Find the edge with max edge degree at present 
        MaxU = -1; MaxV = -1; MaxDegree = -1;
        NodeDegrees = nx.degree(G3)
        for (u, v) in G3.edges_iter():
            CurDegree = NodeDegrees[u] * NodeDegrees[v]
            if CurDegree > MaxDegree:
                MaxDegree = CurDegree
                MaxU = u
                MaxV = v
        G3.remove_edge(MaxU, MaxV)
        i += 1
    nD = len(SC.control_nodes(G3)) / (NodesNum + 0.0)
    print F1, nD
    LRD.append(nD)

    while i < int(F2 * EdgesNum):
        # Find the edge with max edge degree at present 
        MaxU = -1; MaxV = -1; MaxDegree = -1;
        NodeDegrees = nx.degree(G3)
        for (u, v) in G3.edges_iter():
            CurDegree = NodeDegrees[u] * NodeDegrees[v]
            if CurDegree > MaxDegree:
                MaxDegree = CurDegree
                MaxU = u
                MaxV = v
        G3.remove_edge(MaxU, MaxV)
        i += 1
    nD = len(SC.control_nodes(G3)) / (NodesNum + 0.0)
    print F2, nD
    LRD.append(nD)

    while i < int(F3 * EdgesNum):
        # Find the edge with max edge degree at present 
        MaxU = -1; MaxV = -1; MaxDegree = -1;
        NodeDegrees = nx.degree(G3)
        for (u, v) in G3.edges_iter():
            CurDegree = NodeDegrees[u] * NodeDegrees[v]
            if CurDegree > MaxDegree:
                MaxDegree = CurDegree
                MaxU = u
                MaxV = v
        G3.remove_edge(MaxU, MaxV)
        i += 1
    nD = len(SC.control_nodes(G3)) / (NodesNum + 0.0)
    print F3, nD
    LRD.append(nD)

    while i < int(F4 * EdgesNum):
        # Find the edge with max edge degree at present 
        MaxU = -1; MaxV = -1; MaxDegree = -1;
        NodeDegrees = nx.degree(G3)
        for (u, v) in G3.edges_iter():
            CurDegree = NodeDegrees[u] * NodeDegrees[v]
            if CurDegree > MaxDegree:
                MaxDegree = CurDegree
                MaxU = u
                MaxV = v
        G3.remove_edge(MaxU, MaxV)
        i += 1
    nD = len(SC.control_nodes(G3)) / (NodesNum + 0.0)
    print F4, nD
    LRD.append(nD)
    G3.clear()
        
    # Folloing is Initial Edge Betweenness Attack (IBA)
    print '########## Edge IBA ##########'
    G4 = copy.deepcopy(G)
    EdgeBetweenness = nx.edge_betweenness_centrality(G4)
    SortedBetEdges = sorted(EdgeBetweenness,
                            key=EdgeBetweenness.get, reverse=True)
    i = 0
    while i < int(F1 * EdgesNum):
        u, v = SortedBetEdges[i]
        G4.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G4)) / (NodesNum + 0.0)
    print F1, nD
    LIB.append(nD)

    while i < int(F2 * EdgesNum):
        u, v = SortedBetEdges[i]
        G4.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G4)) / (NodesNum + 0.0)
    print F2, nD
    LIB.append(nD)

    while i < int(F3 * EdgesNum):
        u, v = SortedBetEdges[i]
        G4.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G4)) / (NodesNum + 0.0)
    print F3, nD
    LIB.append(nD)

    while i < int(F4 * EdgesNum):
        u, v = SortedBetEdges[i]
        G4.remove_edge(u, v)
        i += 1
    nD = len(SC.control_nodes(G4)) / (NodesNum + 0.0)
    print F4, nD
    LIB.append(nD)
    G4.clear()
    EdgeBetweenness = {}
    SortedBetEdges = []

    # Following is Recalculated Edge Betweenness Attack (RBA)
    print '########## Edge RBA ##########'
    G5 = copy.deepcopy(G)
    i = 0
    while i < int(F1 * EdgesNum):
        EdgeBets = nx.edge_betweenness_centrality(G5)
        # Find the edge with Max edge betweenness
        uMax = -1; vMax = -1; betMax = -1.0;
        for ((u, v), bet) in EdgeBets.iteritems():
            if bet > betMax:
                betMax = bet
                uMax = u
                vMax = v
        G5.remove_edge(uMax, vMax)
        i += 1
    nD = len(SC.control_nodes(G5)) / (NodesNum + 0.0)
    print F1, nD
    LRB.append(nD)

    while i < int(F2 * EdgesNum):
        EdgeBets = nx.edge_betweenness_centrality(G5)
        # Find the edge with Max edge betweenness
        uMax = -1; vMax = -1; betMax = -1.0;
        for ((u, v), bet) in EdgeBets.iteritems():
            if bet > betMax:
                betMax = bet
                uMax = u
                vMax = v
        G5.remove_edge(uMax, vMax)
        i += 1
    nD = len(SC.control_nodes(G5)) / (NodesNum + 0.0)
    print F2, nD
    LRB.append(nD)

    while i < int(F3 * EdgesNum):
        EdgeBets = nx.edge_betweenness_centrality(G5)
        # Find the edge with Max edge betweenness
        uMax = -1; vMax = -1; betMax = -1.0;
        for ((u, v), bet) in EdgeBets.iteritems():
            if bet > betMax:
                betMax = bet
                uMax = u
                vMax = v
        G5.remove_edge(uMax, vMax)
        i += 1
    nD = len(SC.control_nodes(G5)) / (NodesNum + 0.0)
    print F3, nD
    LRB.append(nD)

    while i < int(F4 * EdgesNum):
        EdgeBets = nx.edge_betweenness_centrality(G5)
        # Find the edge with Max edge betweenness
        uMax = -1; vMax = -1; betMax = -1.0;
        for ((u, v), bet) in EdgeBets.iteritems():
            if bet > betMax:
                betMax = bet
                uMax = u
                vMax = v
        G5.remove_edge(uMax, vMax)
        i += 1
    nD = len(SC.control_nodes(G5)) / (NodesNum + 0.0)
    print F4, nD
    LRB.append(nD)
    G5.clear()

    print 'RA: ', LRA[0], LRA[1], LRA[2], LRA[3]
    print 'ID: ', LID[0], LID[1], LID[2], LID[3]
    print 'RD: ', LRD[0], LRD[1], LRD[2], LRD[3]
    print 'IB: ', LIB[0], LIB[1], LIB[2], LIB[3]
    print 'RB: ', LRB[0], LRB[1], LRB[2], LRB[3]



if __name__ == "__main__":
    #EdgeAttackBA()
    #EdgeAttackUSAir()
    # Edge Attack Erdos971 Network
    # for random attack, we set the random seed to from 1 to 100 for the 
    # independent 100 runs. For other deliberate attacks, as the attack order
    # is fixed, we reset the seed of random to the initial state, i.e. seed(None)
    #EdgeAttackErdosNetwork()

    # Regulatory
    #G = ReadPajek('./dataset/Regulatory/TRN-Yeast-1.net')
    #G = ReadPajek('./dataset/Regulatory/TRN-Yeast-2.net')
    #G = ReadPajek('./dataset/Regulatory/TRN-EC-2.net')
    #G = ReadPajek('./dataset/Regulatory/Ownership.net')

    # World Wide Web (WWW)
    G = ReadPajek('./dataset/WWW/PoliticalBlogs.net')

    print 'Edge Attack From Temp Files ... '
    print 'WWW --- PoliticalBlogs'
    NodesNum = G.number_of_nodes()
    EdgesNum = G.number_of_edges()
    DriverNodes = SC.control_nodes(G)
    nD = len(DriverNodes) / (NodesNum + 0.0)
    print 'Nodes Num: ', NodesNum
    print 'Edges Num: ', EdgesNum
    print 'nD = ', nD
    EdgeAttack(G)