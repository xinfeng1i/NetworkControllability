"""
structral controllability measure, driver nodes
"""
#   Copyright (C) 2014 by
#   Xin-Feng Li <silfer.lee@gmail.com>
#   All rights reserved
#   BSD license

import networkx as nx
import matplotlib.pyplot as plt

__author__ = """Xin-Feng Li (silfer.lee@gmail.com)"""

def get_driver_nodes(DG):
    '''Return the driver nodes number and driver nodes from a DiGraph DG

    Basic Idea:
    Given a graph DG, create a new undirected bipartite graph, BG
    suppose DG has n nodes, the the BG has 2*n nodes, the first n nodes [0, n)
    form the left parts of BG, the [n, 2*n) nodes form the right part of BG,
    for each edge form DG, say, 1-->3, add edges in BG 1---(3+n)
    then call the maximum matching algorithm find the matched nodes
    All the unmatched nodes are the driver nodes we are looking for

    Parameters
    ----------
    DG: networkx.DiGraph, directed graph, node number start from 0

    Returns
    -------
    driver node num:    the number of driver nodes
    driver nodes:       the driver nodes we are looking for

    Notes:
    -------
    The index of nodes in DG must start from 0, 1, 2, 3...

    References:
    -----------
    [1] Yang-Yu Liu, Jean-Jacques Slotine, Albert L. Barabasi. Controllability
        of complex networks. Nature, 2011.
    '''
    assert(nx.is_directed(DG))

    nodeNum = DG.number_of_nodes()
    edgeNum = DG.number_of_edges()

    # convert to a bipartite graph
    G = nx.Graph()
    left_nodes  = ['a'+str(node) for node in G.nodes()]
    right_nodes = ['b'+str(node) for node in G.nodes()]       
    G.add_nodes_from(left_nodes)
    G.add_nodes_from(right_nodes)
    for edge in DG.edges():
        da = 'a' + str(edge[0])
        db = 'b' + str(edge[1])
        G.add_edge(da, db)

    assert(nx.is_bipartite(G))
    # maximum matching algorithm
    matched_edges = nx.maximal_matching(G)

    # find all the matched and unmatched nodes
    matched_nodes = [int(edge[0][1:]) if edge[0][0] == 'b' else int(edge[1][1:]) for edge in matched_edges]
    unmatched_nodes = [node for node in DG.nodes() if node not in matched_nodes]
    unmatched_nodes_num = len(unmatched_nodes)

    # perfect matching
    if unmatched_nodes_num == 0:
        print '>>> Perfect Match Found ! <<<'
        unmatched_nodes_num = 1
        unmatched_nodes = [0]
        
    return (unmatched_nodes_num, unmatched_nodes)

# test this function
if __name__ == "__main__":
    DG = nx.DiGraph()
    DG_edges = [(0,2), (0,3), (0,4), (0,5), (1,4), (1,5)]
    DG.add_edges_from(DG_edges)
    n, nodes = get_driver_nodes(DG)
    print "\n"
    print "node num:", n
    print "nodes:", nodes

    # test from Nature paper, Figure1 c
    # Expected Result: 1
    # Matched Edges: (1, 2) (2, 3) (3, 4)
    G2 = nx.DiGraph()
    G2.add_nodes_from([0,1,2,3])
    G2.add_edge(1-1,2-1)
    G2.add_edge(2-1,3-1)
    G2.add_edge(3-1,4-1)
    n, nodes = get_driver_nodes(G2)
    print "\n"
    print "G2 nodes:", G2.nodes();
    print "node num:", n
    print "nodes:", nodes

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
    n, nodes = get_driver_nodes(G3)
    print "\n"
    print "G3 nodes:", G3.nodes();
    print "node num:", n
    print "nodes:", nodes

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
    n, nodes = get_driver_nodes(G4)
    print "\n"
    print "G4 nodes:", G4.nodes();
    print "node num:", n
    print "nodes:", nodes

    # test compelte graph
    # Expeced Results: (0) OR (1) OR (2) OR (3)
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
    n, nodes = get_driver_nodes(G5)
    print "\n"
    print "G5 nodes:", G5.nodes();
    print "node num:", n
    print "nodes:", nodes