# from typing import List
class Graph:
    def __init__(self, graph_dict=None):
        if not graph_dict:
            self.graph = {}
        else:
            self.graph = graph_dict

    # accept key value pair, tuple, list, or vertex and args
    def add_vertex (self, vertex, ls):
        if vertex not in self.graph:
            self.graph[vertex] = ls

    # def add_vertex(self, vertex, *edges):
    #     if vertex not in self.graph:
    #         self.graph[vertex] = [*edges]
    
    def gen_edges(self):
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                # for directed graph, order is significant
                edges.append((node, neighbor))
        return edges
 
    def edges(self):
        return self.gen_edges()


    def vertices(self):
        return [node for node in self.graph]


    def get_isolated(self):
        isolated = []
        for node in self.graph:
            if not graph[node]:
                isolated += node
        return isolated
    
    def degree(self, vertex):
        return len(self.graph[vertex])
    
    
    def neighbors(self, vertex):
        return self.graph[vertex]
    
    
    def __repr__(self):
        output = "Graph: \n"
        for node in self.graph:
            output += str(node) + "-> "
            for neighbor in self.graph[node]:
                output += str(neighbor) + ", "
            output += "\n"
        return output


if __name__ == "__main__":
    g = Graph()
    g.add_vertex('a', ['b', 'c'])
    g.add_vertex('b', ['a', 'c'])
    print(g)
    print(g.degree('a'))
    print(g.neighbors('b'))
    print(g.vertices())
    print(g.edges())
 