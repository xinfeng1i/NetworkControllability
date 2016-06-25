import networkx as nx
import matplotlib.pyplot as plt
from networkx.utils import powerlaw_sequence
import operator
import random
import csv
import copy
import subprocess, os
import time
import math

def average_degree(G):
    degree = nx.degree(G).values()
    return float(sum(degree)) / len(degree)

def average_closeness_centrality(G):
    closeness_dict = nx.closeness_centrality(G)
    lst = closeness_dict.values()
    n = G.number_of_nodes()
    return sum(lst) / (n + 0.0)

def average_betweenness_centrality(G):
    n = G.number_of_nodes()
    betweenness_dict = nx.betweenness_centrality(G, k=None, normalized=True, weight=None)
    lst = betweenness_dict.values()
    return sum(lst) / (n + 0.0)

def average_eigenvector_centrality(G):
    eigenvector_dict = nx.eigenvector_centrality_numpy(G)
    lst = eigenvector_dict.values()
    n = G.number_of_nodes()
    return sum(lst) / (n + 0.0)

def closeness_betweenness_combination_centrality(G):
    avg_B = average_betweenness_centrality(G)
    avg_C = average_closeness_centrality(G)

    if math.fabs(avg_C - 0.0) < 1E-5:
        return (avg_B + 0.0)
    else:
        return (avg_C + 0.0) + ((avg_B + 0.0) / avg_C)