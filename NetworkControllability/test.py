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
import math
import UtilityFunctions as UF

#G = nx.Graph()
#G.add_nodes_from([0, 1, 2, 3])
#G.add_edge(0, 1)
#G.add_edge(0, 2)
#G.add_edge(0, 3)
#G.add_edge(1, 2)
#print nx.transitivity(G)


#DG = G.to_directed()
#print DG.edges()

def ReadPajek(filename):
    '''Read pajek file to construct Graph'''
    G = nx.Graph()
    fp = open(filename, 'r')
    line = fp.readline()
    while line:
        if line[0] == '*':
            line = line.strip().split()
            #print "line = ", line
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
            elif label == '*Edges' or label == '*edges':
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

if __name__ == "__main__":
    """
    NOTE: The core effects on controllability on USAir97 is calculated
    by PAJEK software not using NetworkX
    """
    #G = ReadPajek("dataset/TEST_USAir97.net")

    M = ReadPajek("dataset/Erdos971_revised.net")
    G = max(nx.connected_component_subgraphs(M),key=len)

    N = G.number_of_nodes()
    L = G.number_of_edges()
    remove_fraction = 0.20
    N_rm = int(N * remove_fraction)
    nodes = nx.nodes(G)
    print "Before Removing:\n"
    print "N = ", N
    print "L = ", L

    random.shuffle(nodes)

    rm_nodes = nodes[0:N_rm]
    G.remove_nodes_from(rm_nodes)

    print "\n after removing:"
    print "N = ", G.number_of_nodes()
    print "L = ", G.number_of_edges()
    print "<k> = ", float(2 * G.number_of_edges()) / G.number_of_nodes()

    avg_deg = UF.average_degree(G);
    print "<k>: ", avg_deg;
    avg_bet = UF.average_betweenness_centrality(G);
    print "<B>: ", avg_bet;
    #APL = nx.average_shortest_path_length(G)
    #print "APL: ", APL

    N_core = nx.core_number(G)
    core_values = N_core.values()
    leaves = [x for x in core_values if x <= 1]
    print "#leaves:", len(leaves)
    print "#core:", G.number_of_nodes() - len(leaves)
    print "#core/#N:", (G.number_of_nodes() - len(leaves))/float(G.number_of_nodes())

