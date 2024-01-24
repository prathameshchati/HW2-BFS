# write tests for bfs
import pytest
from search.graph import Graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """


    pass

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass



# g=graph.Graph("data/class_example_graph.adjlist")
# nx_g=nx.read_adjlist("data/class_example_graph.adjlist", create_using=nx.DiGraph, delimiter=";")

# nx_g.edges()



# dij=Dijkstra(leafy_g, 0)
# dij.run()
# dij.path(7)

# node_map

# root = "A"
# edges = nx.bfs_edges(nx_g, root)
# nodes = [root] + [v for u, v in edges]
# nodes


# print(g.bfs("A"))
# print(g.bfs("A", "H"))
