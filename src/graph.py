class node:
    def __init__(self, value, **attr):
        self.value = value
        for key, val in attr.items():
            self.key = val
    
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value
    
    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)
    
class graph_node(node):
    def __init__(self, value, edges=dict()):
        """
            edges = {graph_node : **edge_properties}
        """
        try:
            assert type(edges) == type(dict())
        except AssertionError:
            print("Must be a dictionairy")
            raise
        super().__init__(value, edges=edges)


class BST_node(node):
    def __init__(self, value, left=None, right=None):
        try:
            assert left < value and value < right
        except AssertionError:
            print("left node must be less than current node which must be lest the right node")

        super().__init__(value, left=left, right=right)


class Graph:
    def __init__(self):
        self.graph = dict()

    def __getitem__(self, key):
        # create temp graph node
        return self.graph.__getitem__(key)

    def __clean__(self):
        for node in self.graph.keys():
            for pot_node in self.graph[node]:
                if pot_node not in self.graph:
                    self.graph[pot_node] = dict()
                self.graph[pot_node][node] = self.graph[node][pot_node]

    def add_node(self, new_node, edges=dict()):
        if new_node in self.graph:
            raise
        self.graph[new_node] = edges
        # self.__clean__()
        for potential_node in edges.keys():
            if potential_node not in self.graph:
                self.graph[potential_node] = dict()
            self.graph[potential_node][new_node] = edges[potential_node]
    
    def add_edge(self, node_a, node_b, **edge_properties):
        if not self.has_node(node_a):
            self.graph[node_a] = dict()
        if not self.has_node(node_b):
            self.graph[node_b] = dict()
        self.graph[node_a][node_b] = edge_properties
        self.graph[node_b][node_a] = edge_properties

    def __repr__(self):
        output = ""
        for key in self.graph.keys():
            output += f"{key} : {self.graph[key]}\n"
        return output
    
    def has_edge(self, node_a, node_b):
        if self.has_node(node_a) and self.has_node(node_b):
            return node_b in self.graph[node_a]
        return False

    def has_node(self, node):
        return node in self.graph

class BST:
    def __init__(self, root=None):
        if root is not None:
            try:
                assert type(root) == type(BST_node())
            except AssertionError:
                print("root must be a BST node")
        pass
    def add_node(self, new_node):
        pass


def add_edge(graph, start, end, **kwargs):
    graph[start][end] = kwargs
    graph[end][start] = kwargs

def add_node(graph, new_node, edges=dict(), **kwargs):
    try:
        assert type(edges) == type(dict())
    except AssertionError:
        print("edges must be a dictionary")
    
    for node in edges.keys():
        pass
        # add_edge(graph, new_node, node, **{edges[node][key]: edges[node][val] for key, val in edges[node].items()})

g = Graph()
g.add_node("a", {"b":{"weight":1, "color": "blue"}, "c":{"weight":2}})
print(g)
g.add_edge("b", "d", weight=1)
print(g)
print(g.has_edge("a", "d"))