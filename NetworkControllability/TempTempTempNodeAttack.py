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

def NodeAttack(G):
    NodesNum = G.number_of_nodes()
    
    # Following is Random Attack
    print '***********Node Random Attack**********'
    G1 = copy.deepcopy(G)
    shuffleNodes = copy.deepcopy(G1.nodes())
    random.shuffle(shuffleNodes)
    i = 0
    while i < int(0.05 * NodesNum):
        node = shuffleNodes[i]
        G1.remove_node(node)
        i += 1
    print '5% ', len(SC.control_nodes(G1)) / (NodesNum + 0.0)

    while i < int(0.10 * NodesNum):
        node = shuffleNodes[i]
        G1.remove_node(node)
        i += 1
    print '10% ', len(SC.control_nodes(G1)) / (NodesNum + 0.0)

    while i < int(0.15 * NodesNum):
        node = shuffleNodes[i]
        G1.remove_node(node)
        i += 1
    print '15% ', len(SC.control_nodes(G1)) / (NodesNum + 0.0)

    while i < int(0.20 * NodesNum):
        node = shuffleNodes[i]
        G1.remove_node(node)
        i += 1
    print '20% ', len(SC.control_nodes(G1)) / (NodesNum + 0.0)
    shuffleNodes = []
    G1.clear()

    # Following is ID Attack
    print '***********Node ID Attack**********'
    G2 = copy.deepcopy(G)
    AllDegrees = G2.degree()
    SortedDegrees = sorted(AllDegrees, key=AllDegrees.get, reverse=True)
    i = 0
    while i < int(0.05 * NodesNum):
        node = SortedDegrees[i]
        G2.remove_node(node)
        i += 1
    print '5% ', len(SC.control_nodes(G2)) / (NodesNum + 0.0)

    while i < int(0.10 * NodesNum):
        node = SortedDegrees[i]
        G2.remove_node(node)
        i += 1
    print '10% ', len(SC.control_nodes(G2)) / (NodesNum + 0.0)

    while i < int(0.15 * NodesNum):
        node = SortedDegrees[i]
        G2.remove_node(node)
        i += 1
    print '15% ', len(SC.control_nodes(G2)) / (NodesNum + 0.0)

    while i < int(0.20 * NodesNum):
        node = SortedDegrees[i]
        G2.remove_node(node)
        i += 1
    print '20% ', len(SC.control_nodes(G2)) / (NodesNum + 0.0)
    AllDegrees.clear()
    SortedDegrees = []
    G2.clear()

    # Following is RD attack
    print '**********Node RD Attack**********'
    G3 = copy.deepcopy(G)
    i = 0
    while i < int(0.05 * NodesNum):
        MaxDegree = max(G3.degree().values())       # Find Current Max Degree
        for node in G3.nodes():                     # Delete One node that has Max Degree
            if G3.degree(node) == MaxDegree:
                G3.remove_node(node)
                break
        i += 1
    print '5% ', len(SC.control_nodes(G3)) / (NodesNum + 0.0)

    while i < int(0.1 * NodesNum):
        MaxDegree = max(G3.degree().values())       # Find Current Max Degree
        for node in G3.nodes():                     # Delete One node that has Max Degree
            if G3.degree(node) == MaxDegree:
                G3.remove_node(node)
                break
        i += 1
    print '10% ', len(SC.control_nodes(G3)) / (NodesNum + 0.0)

    while i < int(0.15 * NodesNum):
        MaxDegree = max(G3.degree().values())       # Find Current Max Degree
        for node in G3.nodes():                     # Delete One node that has Max Degree
            if G3.degree(node) == MaxDegree:
                G3.remove_node(node)
                break
        i += 1
    print '15% ', len(SC.control_nodes(G3)) / (NodesNum + 0.0)

    while i < int(0.20 * NodesNum):
        MaxDegree = max(G3.degree().values())       # Find Current Max Degree
        for node in G3.nodes():                     # Delete One node that has Max Degree
            if G3.degree(node) == MaxDegree:
                G3.remove_node(node)
                break
        i += 1
    print '20% ', len(SC.control_nodes(G3)) / (NodesNum + 0.0)
    G3.clear()

    # Following is IB Attack
    print '**********Node IB Attack**********'
    G4 = copy.deepcopy(G)
    AllBetweenness = nx.betweenness_centrality(G4, k=2000)
    SortedBetweenness = sorted(AllBetweenness, key=AllBetweenness.get, reverse=True)
    i = 0
    while i < int(0.05 * NodesNum):
        G4.remove_node(SortedBetweenness[i])
        i += 1
    print '5% ', len(SC.control_nodes(G4)) / (NodesNum + 0.0)
    while i < int(0.10 * NodesNum):
        G4.remove_node(SortedBetweenness[i])
        i += 1
    print '10% ', len(SC.control_nodes(G4)) / (NodesNum + 0.0)
    while i < int(0.15 * NodesNum):
        G4.remove_node(SortedBetweenness[i])
        i += 1
    print '15% ', len(SC.control_nodes(G4)) / (NodesNum + 0.0)
    while i < int(0.20 * NodesNum):
        G4.remove_node(SortedBetweenness[i])
        i += 1
    print '20% ', len(SC.control_nodes(G4)) / (NodesNum + 0.0)
    G4.clear()
    AllBetweenness.clear()
    SortedBetweenness = []

    #Following is RB Attack
    print '**********Node RB Attack**********'
    G5 = copy.deepcopy(G)
    i = 0
    while i < int(0.05 * NodesNum):
        CurrentBetweenness = nx.betweenness_centrality(G5, k=2000)
        MaxBetweenness = max(CurrentBetweenness.values())
        for node in G5.nodes():
            if CurrentBetweenness[node] == MaxBetweenness:
                G5.remove_node(node)
                break
        i += 1
    print '5% ', len(SC.control_nodes(G5)) / (NodesNum + 0.0)
    while i < int(0.10 * NodesNum):
        CurrentBetweenness = nx.betweenness_centrality(G5, k=2000)
        MaxBetweenness = max(CurrentBetweenness.values())
        for node in G5.nodes():
            if CurrentBetweenness[node] == MaxBetweenness:
                G5.remove_node(node)
                break
        i += 1
    print '10% ', len(SC.control_nodes(G5)) / (NodesNum + 0.0)
    while i < int(0.15 * NodesNum):
        CurrentBetweenness = nx.betweenness_centrality(G5, k=2000)
        MaxBetweenness = max(CurrentBetweenness.values())
        for node in G5.nodes():
            if CurrentBetweenness[node] == MaxBetweenness:
                G5.remove_node(node)
                break
        i += 1
    print '15% ', len(SC.control_nodes(G5)) / (NodesNum + 0.0)
    while i < int(0.20 * NodesNum):
        CurrentBetweenness = nx.betweenness_centrality(G5, k=2000)
        MaxBetweenness = max(CurrentBetweenness.values())
        for node in G5.nodes():
            if CurrentBetweenness[node] == MaxBetweenness:
                G5.remove_node(node)
                break
        i += 1
    print '20% ', len(SC.control_nodes(G5)) / (NodesNum + 0.0)
    G5.clear()




if __name__ == "__main__":
    # Test on USAir97 and Erdos971
    # G_USAir = nx.read_pajek("dataset/USAir97.net") # USAir97
    #G_Erdos = nx.read_pajek("dataset/Erdos971_revised.net") # Erdos971
    #G1 = max(nx.connected_component_subgraphs(G_Erdos),key=len)
    #G = nx.DiGraph()
    #G.add_nodes_from(G1.nodes())
    #for u, v in G1.edges():
    #    r = random.randint(0, 1)
    #    if r == 0:
    #        G.add_edge(u, v)
    #    else:
    #        G.add_edge(v, u)
    #    G1.remove_edge(u, v)

    # ElectronicCircuits
    #G = ReadPajek('./dataset/ElectronicCircuits/s208st.net')
    #G = ReadPajek('./dataset/ElectronicCircuits/s420st.net')
    #G = ReadPajek('./dataset/ElectronicCircuits/s838st.net')

    # Food Web
    #G = ReadPajek('./dataset/FoodWeb/Ythan.net')
    #G = ReadPajek('./dataset/FoodWeb/LittleRock.net')
    #G = ReadPajek('./dataset/FoodWeb/Grassland.net')

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
    #G = ReadPajek('./dataset/Trust/CollegeStudent.net')
    #G = ReadPajek('./dataset/Trust/PrisonInmate.net')
    #G = ReadPajek('./dataset/Trust/Slashdot.net')
    #G = ReadPajek('./dataset/Trust/WikiVote.net')
    #G = ReadPajek('./dataset/Trust/Epinions.net')

    # World Wide Web (WWW)
    #G = ReadPajek('./dataset/WWW/PoliticalBlogs.net')

    # Citation
    #G = ReadPajek('./dataset/Citation/ArXivHepPh.net')
    G = ReadPajek('./dataset/Citation/ArXivHepTh.net')

    print 'Node Attack from Temp Temp Temp Node Attack...'
    print 'Node Attack ArXivHepTh.net'
    NodesNum = G.number_of_nodes()
    EdgesNum = G.number_of_edges()
    DriverNodes = SC.control_nodes(G)
    nD = len(DriverNodes) / (NodesNum + 0.0)
    print 'Nodes Num: ', NodesNum
    print 'Edges Num: ', EdgesNum
    print 'nD = ', nD
    NodeAttack(G)
