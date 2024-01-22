from queue import Queue
import networkx as nx

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

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # scaffold code provided in slides
        Q=Queue()
        visited=[]
        Q.put(start)
        visited.append(start)
        while Q.not_empty():
            v=Q.get()
            N=[n for n in self.graph.successors(v)] # get set of out neighbors since we are given a directed graph 
            for w in N:

                # check if the neighbor node is the end
                if (w==end):
                    distance, shortest_path=nx.single_source_dijkstra(self.graph, start, end) # if w is the end node, then compute the shortest path using the networkx function
                    return shortest_path # list of nodes for the shortest path from start to end

                if w not in visited:
                    visited.append(w)
                    Q.put(w)
                    
        # if the end node is not specificed, return the BFS traversal list
        if (end==None):
            return visited
        else:
            return None # if the end node is not None, but a path does not exist between start and end, return None

        # return




