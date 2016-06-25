import strutral_controllability as SC
import networkx as nx
import copy
import random

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
    # ElectronicCircuits
    #G = ReadPajek('./dataset/ElectronicCircuits/s208st.net')
    #G = ReadPajek('./dataset/ElectronicCircuits/s420st.net')
    #G = ReadPajek('./dataset/ElectronicCircuits/s838st.net')

    # Food Web
    #G = ReadPajek('./dataset/FoodWeb/Ythan.net')
    #G = ReadPajek('./dataset/FoodWeb/LittleRock.net')
    #G = ReadPajek('./dataset/FoodWeb/Grassland.net')
    #G = ReadPajek('./dataset/FoodWeb/Seagrass.net')

    # Metabolic
    #G = ReadPajek('./dataset/Metabolic/EColi.net')
    #G = ReadPajek('./dataset/Metabolic/SCerevisiae.net')
    #G = ReadPajek('./dataset/Metabolic/CElegans.net')


    # Regulatory
    #G = ReadPajek('./dataset/Regulatory/TRN-Yeast-1.net')
    #G = ReadPajek('./dataset/Regulatory/TRN-Yeast-2.net')
    #G = ReadPajek('./dataset/Regulatory/TRN-EC-2.net')
    #G = ReadPajek('./dataset/Regulatory/Ownership.net')

    # Neuronal
    #G = ReadPajek('./dataset/Neuronal/CElegans.net')

    # Internet
    #G = ReadPajek('./dataset/Internet/P2P_1.net')
    #G = ReadPajek('./dataset/Internet/P2P_2.net')
    #G = ReadPajek('./dataset/Internet/P2P_3.net')

    # Organizational
    #G = ReadPajek('./dataset/IntraOrganizational/Consulting.net')
    #G = ReadPajek('./dataset/IntraOrganizational/Manufacturing.net')
    #G = ReadPajek('./dataset/IntraOrganizational/University.net')

    # Trust
    G = ReadPajek('./dataset/Trust/CollegeStudent.net')
    print 'Edge Attack ... '
    print 'Trust College Student'
    NodesNum = G.number_of_nodes()
    EdgesNum = G.number_of_edges()
    DriverNodes = SC.control_nodes(G)
    nD = len(DriverNodes) / (NodesNum + 0.0)
    print 'Nodes Num: ', NodesNum
    print 'Edges Num: ', EdgesNum
    print 'nD = ', nD
    EdgeAttack(G)
    G = ReadPajek('./dataset/Trust/PrisonInmate.net')
    print 'Edge Attack ... '
    print 'Trust Prison Inmate'
    NodesNum = G.number_of_nodes()
    EdgesNum = G.number_of_edges()
    DriverNodes = SC.control_nodes(G)
    nD = len(DriverNodes) / (NodesNum + 0.0)
    print 'Nodes Num: ', NodesNum
    print 'Edges Num: ', EdgesNum
    print 'nD = ', nD
    EdgeAttack(G)
    #G = ReadPajek('./dataset/Trust/Slashdot.net')
    G = ReadPajek('./dataset/Trust/WikiVote.net')
    print 'Edge Attack ... '
    print 'Trust WikiVote'
    NodesNum = G.number_of_nodes()
    EdgesNum = G.number_of_edges()
    DriverNodes = SC.control_nodes(G)
    nD = len(DriverNodes) / (NodesNum + 0.0)
    print 'Nodes Num: ', NodesNum
    print 'Edges Num: ', EdgesNum
    print 'nD = ', nD
    EdgeAttack(G)
    #G = ReadPajek('./dataset/Trust/Epinions.net')

    # World Wide Web (WWW)
    #G = ReadPajek('./dataset/WWW/PoliticalBlogs.net')
    


    