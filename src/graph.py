# from typing import List
import random
# from src.utils import *

#FIXME: consistent naming (vertex and node), return values should be all list or set



class Graph:
    def __init__(self, is_directed=False, has_loops=False):
        self.is_directed = is_directed
        self.has_loops = has_loops
        self.vertices = {}
        self._clean()
    
    def __repr__(self):
        output = "Graph: \n"
        for node in self.vertices:
            output += f"{node.value} -> "
            output += f"{str([i[0] for i in node.edges])[1:-1]}\n"
        return output
            
    def _clean(self):
        for node in self.vertices:
            # make sure that if one node has a path to another, 
            # the corresponding node also has that path
            if not self.is_directed: # if it not a directed graph
                for v in node.edges:
                    v.add_neighbor(node, node.edges[v])
            
            # if a graph is not enabled to have loops it must not
            # have an edge to itself
            if not self.has_loops and node in node.edges:
                node.edges.pop(node)
    
    def add_vertex(self, value, neighbors={}):
        node = Node(value)
        for n, w in neighbors.items():
            node.add_neighbor(n, w)
        self.vertices[node] = 0 # zerod dictionary

        
    def add_edge(self, start, end, weight=1):
        if start in self.vertices and end in self.vertices:
            start.add_neighbor(end, weight)
            self._clean()
        elif start in {v.value for v in self.vertices} and end in {v.value for v in self.vertices}:
            



    # def add_vertex(self, vertex, ls=set()):
    #     if vertex not in self.graph:
    #         self.graph[vertex] = ls
    #     self._clean()

    # # incase a vertex is given just call the neighbors function
    # def vertices(self, vertex=None):
    #     if not vertex:
    #         return [node for node in self.graph]
    #     return self.neighbors(vertex)
    
    # #TODO: Implement
    # def add_edge(self, vertex1, vertex2):
    #     pass

    # def all_edges(self):
    #     edges = []
    #     for node in self.graph:
    #         for neighbor in self.graph[node]:
    #             # for directed graph, order is significant
    #             edges.append((node, neighbor))
    #     return edges
 
    # def edges(self, vertex=None):
    #     if not vertex:
    #         return self.all_edges()
    #         # use tuple instead of set in case of directed graph
    #     return [(vertex, neighbor) for neighbor in self.graph[vertex]]


    # def get_isolated(self):
    #     isolated = set()
    #     for node in self.graph:
    #         if not self.graph[node]:
    #             isolated.add(node)
    #     return isolated
    
    # #TODO: Implement
    # def set_directed(self):
    #     pass


    # #TODO: if no vertex is passed, generate the degrees for all nodes
    # def degree(self, vertex):
    #     return len(self.graph[vertex])
        
    # def neighbors(self, vertex):
    #     return self.graph[vertex]



class Node:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_neighbor(self, neighbor, weight=1):
        if neighbor not in self.edges:
            self.edges[neighbor] = weight
    
    def __eq__(self, other):
        pass



if __name__ == "__main__":
    g = Graph()
    g.add_vertex(12)
    g.add_vertex(3)
    print(g)
    g.add_edge(12, 3)
    print(g)
    pass