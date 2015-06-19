import networkx as nx
import matplotlib.pyplot as plt
from networkx.utils import powerlaw_sequence
import operator
import random
import csv
import copy
import subprocess, os
import time

def average_closeness_centrality(G):
    closeness_dict = nx.closeness_centrality(G)
    lst = closeness_dict.values()
    n = G.number_of_nodes()
    return sum(lst) / (n + 0.0)

def average_betweenness_centrality(G):
    betweenness_dict = nx.betweenness_centrality(G)
    lst = betweenness_dict.values()
    n = G.number_of_nodes()
    return sum(lst) / (n + 0.0)

def average_eigenvector_centrality(G):
    eigenvector_dict = nx.eigenvector_centrality(G, max_iter=1000)
    lst = eigenvector_dict.values()
    n = G.number_of_nodes()
    return sum(lst) / (n + 0.0)