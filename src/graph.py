# from typing import List
import random
from src.utils import *

#FIXME: consistent naming (vertex and node), return values should be all list or set

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

class Graph:
    def __init__(self, graph_dict=None, is_directed=False, has_loops=False):
        self.is_directed = is_directed
        self.has_loops = has_loops

        if not graph_dict:
            self.graph = {}
        else:
            #FIXME: single element neighbor is not iterable
            self.graph = {k:set(v) for k, v in graph_dict.items()}
            self._clean()
    
    def __repr__(self):
        output = "Graph: \n"
        for node in self.graph:
            output += str(node) + "-> "
            for neighbor in self.graph[node]:
                output += str(neighbor) + ", "
            output += "\n"
        return output
            
    def _clean(self):
        for node in self.graph:
            # make sure that if one node has a path to another, 
            # the corresponding node also has that path
            if not self.is_directed: # if it not a directed graph
                for v in self.graph[node]:
                    self.graph[v].add(node)
            
            # if a graph is not enabled to have loops it must not
            # have an edge to itself
            if not self.has_loops and node in self.graph[node]:
                self.graph[node].remove(node)
    
    def add_vertex(self, vertex, ls=set()):
        if vertex not in self.graph:
            self.graph[vertex] = ls
        self._clean()

    # incase a vertex is given just call the neighbors function
    def vertices(self, vertex=None):
        if not vertex:
            return [node for node in self.graph]
        return self.neighbors(vertex)
    

    def gen_edges(self):
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                # for directed graph, order is significant
                edges.append((node, neighbor))
        return edges
 
    def edges(self, vertex=None):
        if not vertex:
            return self.gen_edges()
            # use tuple instead of set in case of directed graph
        return [(vertex, neighbor) for neighbor in self.graph[vertex]]


    def get_isolated(self):
        isolated = set()
        for node in self.graph:
            if not self.graph[node]:
                isolated.add(node)
        return isolated
    
    #TODO: if no vertex is passed, generate the degrees for all nodes
    def degree(self, vertex):
        return len(self.graph[vertex])
        
    def neighbors(self, vertex):
        return self.graph[vertex]

def random_graph(alphabet=alphabet, min_degree=0, max_degree=round(len(alphabet)*0.75)):
    d = {}
    for i in alphabet:
        d.update({i : [random.choice(exclude(alphabet, i)) for _ in range(random.randint(min_degree, max_degree))]})
    g = Graph(d)
    return g

if __name__ == "__main__":
    g = random_graph()
    print(g)
 