"""
def dijkstra(graph, start, end):
    visited = []
    unvisited = Graph.nodes()
    table = {node: [float('inf'), Null] for node in Graph.nodes()}

#   Node      Shortest dist from start        prev node
#   A               inf                         Null
#   B               inf                         Null
#   C               inf                         Null
#   D               inf                         Null
#   E               inf                         Null

    current = start
    dist(start, start)  #no cycles = 0

    while len(unvisited): #unvisited nodes exist
        unvisited.pop(current)
        for neighbor in current.neighbors():
            if total + dist(current, neighbor) < table[neighbor][0]:  # current shortest distant
                table[neighbor] = [dist(start, neighbor), current]
        visited.append(current)
        if current == end: stop()
        current = min(table[shortest_path_node])
        total = min(table[shortest_path dist])

    path = []
    while True:
        path.insert(0, end)
        if end == start:
            break
        end = table[end][prev]
    return path

"""

from dataclasses import dataclass
class Graph():
    def __init__(self):
        self.nodes = dict()
    
    #neighbors = node:weight
    #nodes = {A:{B:1, C:1, D:3}}
    def add_node(self, value, neighbors=None):
        self.nodes[value] = dict() if neighbors is None else neighbors

    def add_nodes(self, values):
        for value in values:
            self.nodes[value] = dict()
    
    def add_edge(self, u, v, weight=1):
        if u == v:
            return
        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)
        self.nodes[u][v] = weight
        self.nodes[v][u] = weight
        self._clean()
    
    def _clean(self):
        keys = list(self.nodes.keys())
        for node in keys:
            try:
                del self.nodes[node][node]
            except:
                continue

    def get_neighbors(self, node):
        if node in self.nodes:
            return list(self.nodes[node].keys())
        raise KeyError

    def dist(self, u, v):
        if v in self.nodes[u]:
            return self.nodes[u][v]
        raise KeyError

    def __repr__(self):
        return self.nodes.__repr__()


@dataclass
class Table:
    distance : int
    previous : tuple


class Grid2D(Graph):
    def __init__(self, *args):
        super().__init__()
        if len(args) == 2:
            self.grid_dim_factory(args[0], args[1])

        elif len(args) == 1:
            self.grid_matrix_factory(args[0])
    
        else:
            raise

    def grid_matrix_factory(self, matrix):
        # assert, is instance of list
        self.matrix = matrix
        self.length = len(matrix)
        self.width = len(matrix[0])

        for i in range(self.length):
            for j in range(self.width):
                self.nodes[(i, j)] = dict()
                if i > 0:
                    self.add_edge((i, j), (i-1, j), weight=matrix[i-1][j])
                if i < self.length-1:
                        self.add_edge((i, j), (i+1, j), weight=matrix[i-1][j])
                if j > 0:
                    self.add_edge((i, j), (i, j-1), weight=matrix[i][j-1])
                if j < self.width-1:
                    self.add_edge((i, j), (i, j+1), weight=matrix[i][j+1])


    def grid_dim_factory(self, length, width):
        matrix = [[None for _ in range(width)] for _ in range(length)]
        self.grid_matrix_factory(matrix)

    def add_edge(self, u, v, weight=1, symmetric=False):
        if u == v:
            return
        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)

        self.nodes[u][v] = weight
        if symmetric:
            self.nodes[v][u] = weight

    def __repr__(self):
        output = ""
        # output += str(self.matrix[0][0]) + "\n"
        for node in self.nodes.keys():
            for neighbor in self.nodes[node].keys():
                output += str(self.matrix[node[0]][node[1]]) + " --" + str(self.nodes[node][neighbor]) + "-> " + str(self.matrix[neighbor[0]][neighbor[1]])
                output += "\n"
            output += "\n"
        return output

    def __getitem__(self, index):
        return self.matrix.__getitem__(index)

    def get_dist(self, u, v, u_inclusive=True):
        try:
            return self.matrix[u[0]][u[1]] + self.nodes[u][v] if u_inclusive else self.nodes[u][v]

        except (KeyError, IndexError) as e:
            print(f"Error: \n\t{v} is not a neighbor of {u}")
            raise e
    
    def dijkstra(self, start, end):
        visited = []
        unvisited = list(self.nodes.keys())
        table = dict()
        for node in unvisited:
            table[node] = Table(float('inf'), None)
        total = self.matrix[start[0]][start[1]]
        current = start
        while current != end:
            if len(unvisited) == 0:
                return -1
            unvisited.remove(current)
            for neighbor in self.get_neighbors(current):
                if total + self.get_dist(current, neighbor, False) < table[neighbor].distance:
                    table[neighbor].distance = total + self.get_dist(current, neighbor, False)
                    table[neighbor].previous = current
            visited.append(current)

            mn = float('inf')
            for i in unvisited:
                if table[i].distance < mn:
                    mn = table[i].distance
                    current = i
            # current = min(table, key=lambda x: table[x].distance)
            total = table[current].distance
        
        path = []
        while True:
            path.insert(0, current)
            if current == start:
                break
            current = table[current].previous
        
        return total, path

# w = 80
# l = 80
# matrix = [[0 for _ in range(w)] for _ in range(l)]
# with open(".\\p083_matrix.txt", "r") as f:
#     for i, line in enumerate(f):
#         values = line.split(",")
#         for j, value in enumerate(values):
#             matrix[i][j] = int(value)

k = [[2, 5, 7, 8, 2, 9, 9], 
     [3, 1, 5, 1, 0, 5, 6],
     [9, 1, 8, 6, 6, 9, 0],
     [4, 4, 5, 1, 8, 2, 3]]
d = Grid2D(k)

path = d.dijkstra((0, 0), (3, 6))[1]
print(path)
for i in path:
    print(k[i[0]][i[1]])
