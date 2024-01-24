from queue import Queue
import networkx as nx
import warnings

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

        # check if graph is empty, if it is, raise an error and stop the initialization
        if len(self.graph.nodes())==0:
            raise ValueError("Empty graph was provided, please make sure that the input graph has at least one node.")

    # simple function to get the nodes of the graph
    def get_nodes(self):
        return list(self.graph.nodes())

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # check if start node exists in graph
        if not self.graph.has_node(start):
            raise KeyError("The starting node provided is not in the graph. Please try another node.") 

        # check if ending node is present in the graph if ending node is not None
        if (end!=None):
            if not self.graph.has_node(end):
                raise KeyError("The ending node provided is not in the graph. Please try another node.")

        # check if graph is connected; first convert to undirected graph, if graph contains unconnected regions, raise a warning but keep running the program
        self.undirected_graph=nx.to_undirected(self.graph)
        # if not (nx.is_connected(self.undirected_graph)):
        if not (nx.is_strongly_connected(self.graph)):
            # print('WARNING')
            # raise Warning("The graph you have provided is not connected. BFS will be run on all the nodes that are within the connected component of the provided starting node.")
            warnings.warn("The graph you have provided is not connected. BFS will be run on all the nodes that are within the connected component of the provided starting node.")

        # scaffold code provided in slides
        Q=Queue()
        visited=[]
        Q.put(start)
        visited.append(start)
        while not Q.empty():
            v=Q.get()

            # SWITCH LINE BELOW TO self.graph.neighbors(v) AND TEST
            N=[n for n in self.graph.successors(v)] # get set of out neighbors since we are given a directed graph 
            for w in N:

                # check if the neighbor node is the end
                if (w==end):
                    distance, shortest_path=nx.single_source_dijkstra(self.graph, start, end) # if w is the end node, then compute the shortest path using the networkx function
                    return shortest_path # list of nodes for the shortest path from start to end

                # if the node has not been visited, add to the visited list and the queue
                if w not in visited:
                    visited.append(w)
                    Q.put(w)
                    
        # if the end node is not specificed, return the BFS traversal list
        if (end==None):
            return visited
        else:
            return None # if the end node is not None, but a path does not exist between start and end, return None

        # return

    # networkx version of bfs to check bfs traversal written above
    def networkx_bfs(self, start):
        return


    def networkx_shortest_path(self, start, end=None):
        return


# TEST SINGLE AND DOUBLE NODE GRAPHS


# TESTING
# g=Graph("data/class_example_graph.adjlist")
# print(g.bfs("A"))
# print(g.bfs("A", "H"))

# g=Graph("data/tiny_network.adjlist")
# g.get_nodes()
# g.bfs('Luke Gilbert')

# g=Graph("data/citation_network.adjlist")
# g.bfs('Luke Gilbert')

# g=Graph("data/class_example_graph_no_path_case.adjlist")
# print(g.bfs("A"))
# print(g.bfs("A", "I"))

# g=Graph("data/empty_graph.adjlist")


# g.bfs("")