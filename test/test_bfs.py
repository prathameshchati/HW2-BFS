# write tests for bfs
from logging import warning
from types import NoneType
import warnings
from warnings import WarningMessage
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
    # set filename and start
    fn="data/tiny_network.adjlist"
    start="Luke Gilbert"

    # use networkx bfs function to check that our manually written bfs function is working properly
    nx_g=nx.read_adjlist(fn, create_using=nx.DiGraph, delimiter=";")
    nx_edges=nx.bfs_edges(nx_g, start)
    nx_bfs=[start] + [v for u, v in nx_edges]

    # create instance of our graph and run our bfs function
    g=Graph(fn)
    our_bfs=g.bfs("Luke Gilbert")

    # check that we return the same number of nodes and that traversal is correct for our bfs function given a starting node and no end node 
    assert len(our_bfs)==len(nx_bfs)
    assert our_bfs==nx_bfs

    # pass

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
    ################################################################### FOR SMALL GRAPH ###################################################################

    # set filename and start node
    fn="data/tiny_network.adjlist"
    start="Luke Gilbert"

    # read in small graph
    nx_g=nx.read_adjlist(fn, create_using=nx.DiGraph, delimiter=";")

    # make sure graph is fully connected
    nx_cc=[len(c) for c in sorted(nx.strongly_connected_components(nx_g), key=len, reverse=True)]
    assert len(nx_cc)==1

    # create instance of our graph and run our bfs function - check that no warning is raised
    g=Graph(fn)
    with warnings.catch_warnings() as record:
        g.bfs("Luke Gilbert")
    assert type(record)==NoneType

    ################################################################### FOR LARGE GRAPH ###################################################################

    # set filename, start and end node (both in connected and unconnected region)
    fn="data/citation_network.adjlist"
    start="Luke Gilbert"

    # unconnected end found using the smallest subgraph for a set of disjoint connected components: unconnected_end=min(nx.strongly_connected_components(nx_g), key=len)
    unconnected_end='34858697'

    # connected end found using same process as above but with a random node drawn from the largest connected component: connected_end=max(nx.strongly_connected_components(nx_g), key=len)
    connected_end='Mark Ansel'

    # # use networkx bfs function to check that our manually written bfs function is working properly - also compute shortest path - this is done for the large network
    nx_g=nx.read_adjlist(fn, create_using=nx.DiGraph, delimiter=";")

    # make sure that there exists unconnected regions to test 
    nx_cc=[len(c) for c in sorted(nx.strongly_connected_components(nx_g), key=len, reverse=True)]
    assert len(nx_cc)>1

    # run bfs and dijkstra using networkx
    nx_edges=nx.bfs_edges(nx_g, start)
    nx_bfs=[start] + [v for u, v in nx_edges]
    nx_sp=nx.single_source_dijkstra(nx_g, start, connected_end)

    # # create instance of our graph and run our bfs function
    g=Graph(fn)

    # check if warning is raised for unconnected graph when running bfs with no end
    with pytest.warns(UserWarning):
        our_bfs=g.bfs("Luke Gilbert")

    # check that we return the same number of nodes and that traversal is correct for our bfs function given a starting node and no end node 
    assert len(our_bfs)==len(nx_bfs)
    assert our_bfs==nx_bfs

    # check that we get the shortest path with our connected end when running bfs (compared to networkx shortest path function), we are checking if the shortest path is returned for a known connected end
    with pytest.warns(UserWarning):
        our_bfs=g.bfs("Luke Gilbert", connected_end)
    assert len(our_bfs)==len(nx_sp[1])
    assert our_bfs==nx_sp[1]

    # check that if we run with an unconnected end node we get None, we should test this with networkx by raising an exception with the unconnected end
    with pytest.warns(UserWarning):
        our_bfs=g.bfs("Luke Gilbert", unconnected_end)
    assert our_bfs==None

    # check that network raises exception
    with pytest.raises(nx.exception.NetworkXNoPath):
        nx_sp=nx.single_source_dijkstra(nx_g, start, unconnected_end)

    # pass


def test_bfs_edge_cases():

    # test with blank graph - should be stopped at initialization
    with pytest.raises(ValueError) as out:  
         g=Graph("data/empty_graph.adjlist")
    assert out.type==ValueError

    # test with a start node that does not exist in the tiny network
    non_existant_node="Prathamesh Chati" # hopefully someday
    g=Graph("data/tiny_network.adjlist")
    with pytest.raises(KeyError) as out:  
        g.bfs(non_existant_node, 'Luke Gilbert')
    assert out.type==KeyError

    # test with an end node that does not exist in the tiny network
    with pytest.raises(KeyError) as out:  
        g.bfs('Luke Gilbert', non_existant_node)
    assert out.type==KeyError

    # test if start and end are same node
    with pytest.raises(KeyError) as out:  
        g.bfs('Luke Gilbert', 'Luke Gilbert')
    assert out.type==KeyError

    # test single node graph - warning should be raised on initialization and running bfs should simply return the single node
    with pytest.warns(UserWarning):
        g=Graph("data/single_node_graph.adjlist")
    out_bfs=g.bfs("A")
    assert list(out_bfs)==["A"]

    # pass