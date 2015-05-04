import networkx as nx
import matplotlib.pyplot as plt

#x = [1, 2, 3]
#y = [4, 5, 6]

#ER = nx.random_graphs.erdos_renyi_graph(20, 0.5, None, False)
#BA = nx.random_graphs.barabasi_albert_graph(20, 2)
#nx.draw(BA, node_size = 200, node_color = 'r', node_shape = 'o', alpha = 0.8, with_labels=True, font_color='b')
#plt.title("BA Networks", fontsize = 20)
#plt.show()


def get_driver_nodes():
    pass

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
G4.add_edge(0,1)
G4.add_edge(0,2)
G4.add_edge(0,3)
G4.add_edge(0,4)
G4.add_edge(0,5)
G4.add_edge(1,5)
#nx.draw(G4, with_labels = True)
#plt.show()
print G4.nodes()

left_nodes  = ['a'+str(node) for node in G4.nodes()]
right_nodes = ['b'+str(node) for node in G4.nodes()]
print left_nodes
print right_nodes
a = 'hello'
print a[0] == 'h' 

ans = [int(eachnode[1:]) for eachnode in left_nodes]
print ans
#n, nodes = get_driver_nodes(G4)
#print "\n"
#print "G4 nodes:", G4.nodes();
#print "node num:", n
#print "nodes:", nodes