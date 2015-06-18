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

G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3])
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(0, 3)
G.add_edge(1, 2)
print nx.transitivity(G)