class Node():
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value
    
class Linked_list_node(Node):
    def __init__(self, value, next=None):
        super().__init__(value)
        self.next = next

class BST_node(Node):
    def __init__(self, value):
        super.__init__(value)
        self.left = None
        self.right = None

class Graph_node(Node):
    pass

class Heap_node(Node):
    pass

class RBT_node(Node):
    pass