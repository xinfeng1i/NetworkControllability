#coding=utf-8
"""
exact controllability measure, driver nodes
"""
#   Copyright (C) 2015 by
#   Xin-Feng Li <silfer.lee@gmail.com>
#   All rights reserved
#   BSD license

import networkx as nx
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import scipy as sp
import sympy

__author__ = """Xin-Feng Li (silfer.lee@gmail.com)"""

def get_number_of_driver_nodes(G):
    """Return the driver nodes number and driver nodes of a (directed or undirected) graph G

    Basic Idea:
    Given a graph G, it have been proved that the number of driver nodes (N_D) is determined
    by the maximum geometric multiplicity of the adjacency matrix A. i.e.
        N_D = max{N - rank(\lambda_i I_N - A)} where \lambda_i is the eigenvalue of A 
    For undirected network, the above equation can be reduced to 
        N_D = max {\delta (\lambda_i)} the maximum algebraic multiplicity of \lambda_i

    Parameters:
    -----------
    G:  directed or undirected network

    Returns:
    --------
    ND:              the number of driver nodes
    ND_lambda:       the eigenvalue corresponding to maximum geometric multiplicity

    Note:
    ----
    IF you only want get THE NUMBER of DRIVER NODES, but DONOT CARE which are driver nodes
    Please consider this algorithm.

    References:
    -----------
    Yuan Z, Zhao C, Di Z, et al. Exact controllability of complex networks[J].
    Nature communications, 2013, 4.

    """

    N = G.number_of_nodes()
    A = (nx.adjacency_matrix(G)).todense()  # get adjacency matrix A of G
    all_eigs = LA.eigvals(A)           # get eigenvalues of A
    # get distince eigevalues of A, the precision is 1e-5, 
    # which means any two eigenvalues less than 1e-5 will be considered as identical
    # L = np.unique(np.round(all_eigs,decimals=5))
    L = list(set(np.round(all_eigs,8)))
    #L = list(set(all_eigs))

    ND = -1
    ND_lambda = 0.0
    IN = np.eye(N)
    for my_lambda in L:
        # get geometric multiplicity for each lambda of A
        miu_lambda = N - LA.matrix_rank(my_lambda * IN - A, tol=1E-6)
        if miu_lambda > ND:
            ND = miu_lambda
            ND_lambda = my_lambda

    return (ND, ND_lambda)

def get_number_of_drivers_fast_rank(G):
    """ Return the number of driver nodes using fast rank algorithm,
        this algorithm can ONLY apply to large sparse networks
    """
    N = G.number_of_nodes()
    A = (nx.adjacency_matrix(G)).todense()
    myRank = np.linalg.matrix_rank(A, 1E-6);
    return N - myRank;

def get_driver_nodes(G):
    """Return the driver nodes number and driver nodes of a (directed or undirected) graph G

    Basic Idea:
    Given a graph G, it have been proved that the number of driver nodes (N_D) is determined
    by the maximum geometric multiplicity of the adjacency matrix A. i.e.
        N_D = max{N - rank(\lambda_i I_N - A)} where \lambda_i is the eigenvalue of A 
    For undirected network, the above equation can be reduced to 
        N_D = max {\delta (\lambda_i)} the maximum algebraic multiplicity of \lambda_i

    Parameters:
    -----------
    G:  directed or undirected network

    Returns:
    --------
    ND:              the number of driver nodes
    driverNodes:     the list of driver nodes

    Note:
    -----
    IF you only want get THE NUMBER of DRIVER NODES, but DONOT CARE which are driver nodes
    Please consider the other function get_number_of_driver_nodes(G), it is much more efficient.

    References:
    -----------
    Yuan Z, Zhao C, Di Z, et al. Exact controllability of complex networks[J].
    Nature communications, 2013, 4.

    """
    N = G.number_of_nodes()
    A = (nx.adjacency_matrix(G)).todense()          # get adjacency matrix A of G
    all_eigs = LA.eigvals(A)                        # get eigenvalues of A
    # which means any two eigenvalues less than 1e-8 will be considered as identical
    L = list(set(np.round(all_eigs,8)))

    ND = -1
    ND_lambda = 0.0
    IN = np.eye(N)
    for my_lambda in L:
        # get geometric multiplicity for each lambda of A
        miu_lambda = N - LA.matrix_rank(my_lambda * IN - A, tol=1E-8)
        if miu_lambda > ND:
            ND = miu_lambda
            ND_lambda = my_lambda
        
    middle_matrix = A - ND_lambda * np.eye(N)   # get the middle matrix A - \lambda * I_N
    middle_matrix = np.round(middle_matrix, 8);
    (reduced_matrix, pivot_array) = sympy.Matrix(middle_matrix).rref()  # rref get the reduced row echelon form
    all_nodes = G.nodes() 
    pivot_nodes = [all_nodes[i] for i in pivot_array]
    driver_nodes = [x for x in G.nodes() if x not in pivot_nodes]

    return (ND, driver_nodes)


if __name__ == "__main__":
    # test case from Nature Comm. Fig1 a.
    # Expected results: miu_lambda = 2, lambda = 1.00
    # driver nodes = (2, 5) index start from 0
    G = nx.MultiGraph()
    nodes = [0, 1, 2, 3, 4, 5]
    G.add_nodes_from(nodes)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 3)
    G.add_edge(0, 4)
    G.add_edge(0, 5)
    G.add_edge(4, 5)
    G.add_edge(1, 1)
    G.add_edge(2, 2)  
    (ND, my_lambda) = get_number_of_driver_nodes(G)
    print 'N = ', G.number_of_nodes();
    print 'ND = ', ND
    print 'my lambda = ', my_lambda
    (ND, pivot) = get_driver_nodes(G)
    print "ND:", ND
    print "driver nodes:", pivot
    
    # test from Nature paper, Figure1 c
    # Expected Result: 1
    # driver nodes = (0) index start from 0
    # Matched Edges: (1, 2) (2, 3) (3, 4)
    G2 = nx.DiGraph()
    G2.add_nodes_from([0,1,2,3])
    G2.add_edge(1-1,2-1)
    G2.add_edge(2-1,3-1)
    G2.add_edge(3-1,4-1)
    (ND, my_lambda) = get_number_of_driver_nodes(G2)
    print '-'*20
    print 'N = ', G2.number_of_nodes();
    print "ND:", ND;
    print "lambda:", my_lambda
    (ND, pivot) = get_driver_nodes(G2)
    print "ND:", ND
    print "driver nodes:", pivot


    # test from Nature paper, Figure1 f
    # Expected Result 1: (1, 2, 3)
    # Matched Edges 1: (1, 4)
    # Expected Result 2: (1, 3, 4)
    # Matched Edges 2: (1, 2)
    # Expected Result 3: (1, 2, 4)
    # Matched Edges 3: (1, 3)
    G3 = nx.DiGraph()
    G3.add_nodes_from([0,1,2,3])
    G3.add_edge(1-1,2-1)
    G3.add_edge(1-1,3-1)
    G3.add_edge(1-1,4-1)
    (ND, my_lambda) = get_number_of_driver_nodes(G3)
    print '-'*20
    print 'N = ', G3.number_of_nodes();
    print "ND:", ND;
    print "lambda:", my_lambda
    (ND, pivot) = get_driver_nodes(G3)
    print "ND:", ND
    print "driver nodes:", pivot


    # test from Nature paper, Figure1 i
    # Expected Results 1: (1, 2, 3, 4)
    # Matched Edges 1: (1, 5) (2, 6)
    # Expected Results 2: (1, 3, 4, 5)
    # Matched Edges 2: (1, 2) (2, 6)
    # Expected Results 3: (1, 2, 4, 5)
    # Matched Edges 3: (1, 3) (2, 6)
    # Expected Results 4: (1, 2, 3, 5)
    # Matched Edges 4: (1, 4) (2, 6)
    G4 = nx.DiGraph()
    G4.add_nodes_from([0,1,2,3,4,5])
    G4.add_edge(1-1,2-1)
    G4.add_edge(1-1,3-1)
    G4.add_edge(1-1,4-1)
    G4.add_edge(1-1,5-1)
    G4.add_edge(1-1,6-1)
    G4.add_edge(2-1,6-1)
    (ND, my_lambda) = get_number_of_driver_nodes(G4)
    print '-'*20
    print 'N = ', G4.number_of_nodes();
    print "ND:", ND;
    print "lambda:", my_lambda
    (ND, pivot) = get_driver_nodes(G4)
    print "ND:", ND
    print "driver nodes:", pivot

    # test compelte graph
    # Expeced Results: (1,2,3)
    G5 = nx.DiGraph()
    G5.add_nodes_from([0, 1, 2, 3])
    G5.add_edge(1-1, 2-1)
    G5.add_edge(1-1, 3-1)
    G5.add_edge(1-1, 4-1)
    G5.add_edge(2-1, 1-1)
    G5.add_edge(2-1, 3-1)
    G5.add_edge(2-1, 4-1)
    G5.add_edge(3-1, 1-1)
    G5.add_edge(3-1, 2-1)
    G5.add_edge(3-1, 4-1)
    G5.add_edge(4-1, 1-1)
    G5.add_edge(4-1, 2-1)
    G5.add_edge(4-1, 3-1)
    (ND, my_lambda) = get_number_of_driver_nodes(G5)
    print '-'*20
    print 'N = ', G5.number_of_nodes();
    print "ND:", ND;
    print "lambda:", my_lambda
    (ND, pivot) = get_driver_nodes(G5)
    print "ND:", ND
    print "driver nodes:", pivot

    # test case from Nature Comm. Fig1 b.
    # Expected results: miu_lambda = 4, lambda = 0
    # driver nodes = (0, 2, 3, 5) index start from 0
    G6 = nx.DiGraph();
    G6.add_nodes_from([0, 1, 2, 3, 4, 5])
    G6.add_edge(0, 1)
    G6.add_edge(0, 2)
    G6.add_edge(0, 3)
    G6.add_edge(0, 4)
    G6.add_edge(0, 5)
    G6.add_edge(5, 4)
    (ND, my_lambda) = get_number_of_driver_nodes(G6)
    print '-'*20
    print 'N = ', G6.number_of_nodes();
    print "ND:", ND;
    print "lambda:", my_lambda
    (ND, pivot) = get_driver_nodes(G6)
    print "ND:", ND
    print "driver nodes:", pivot

    # test case from Nature Comm. Fig1.c
    # expected ND = 3 ND_lambda = -1.00
    # driver nodes = (1, 4, 5)
    G7 = nx.Graph()
    G7.add_nodes_from([0, 1, 2, 3, 4, 5])
    edge_1 = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
    edge_2 = [(1, 2), (1, 3), (1, 4), (1, 5)]
    edge_3 = [(2, 4), (2, 5)]
    edge_4 = [(3, 4), (3, 5)]
    edge_5 = [(4, 5)]
    G7.add_edges_from(edge_1)
    G7.add_edges_from(edge_2)
    G7.add_edges_from(edge_3)
    G7.add_edges_from(edge_4)
    G7.add_edges_from(edge_5)
    (ND, my_lambda) = get_number_of_driver_nodes(G7)
    print '-'*20
    print 'N = ', G7.number_of_nodes();
    print "ND:", ND;
    print "lambda:", my_lambda
    (ND, pivot) = get_driver_nodes(G7)
    print "ND:", ND
    print "driver nodes:", pivot

    G8 = nx.Graph()
    G8.add_nodes_from([0, 1, 3, 5]) 
    G8.add_edge(0, 1)
    G8.add_edge(0, 3)
    G8.add_edge(0, 5)
    (ND, my_lambda) = get_number_of_driver_nodes(G8)
    print '-'*20
    print 'N = ', G8.number_of_nodes();
    print "ND:", ND;
    print "lambda:", my_lambda
    (ND, pivot) = get_driver_nodes(G8)
    print "ND:", ND
    print "driver nodes:", pivot