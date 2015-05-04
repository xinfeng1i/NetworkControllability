import networkx as nx

G = nx.DiGraph()
G.add_nodes_from([0, 1, 2, 3, 4])
G.add_edge(0, 1);
G.add_edge(0, 4);
G.add_edge(0, 2);
G.add_edge(1, 2);
G.add_edge(1, 4);
G.add_edge(2, 3);
G.add_edge(4, 3);

nodes = G.nodes();
edges = G.edges();
mydict = nx.edge_betweenness_centrality(G, False);

print "nodes:", nodes;
print "edges:", edges;
print "loads:\n"
for key, value in mydict:
    print key, value, mydict[(key, value)]*1.15

# remove edge(2, 3)
G.remove_edge(2, 3);
nodes = G.nodes();
edges = G.edges();
mydict = nx.edge_betweenness_centrality(G, False);

print "nodes:", nodes;
print "edges:", edges;
print "loads:\n"
for key, value in mydict:
    print key, value, mydict[(key, value)]

# remove (0, 4) (1, 4) (4, 3)
G.remove_edge(0, 4);
G.remove_edge(1, 4);
G.remove_edge(4, 3);
nodes = G.nodes();
edges = G.edges();
mydict = nx.edge_betweenness_centrality(G, False);

print "nodes:", nodes;
print "edges:", edges;
print "loads:\n"
for key, value in mydict:
    print key, value, mydict[(key, value)]

nodesnodes = G;
print nodesnodes;


