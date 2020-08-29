class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def insert(root, node):
        if root == None:
            root = node
        elif node.value < root.value:
            insert(root.left, node)
        else:
            insert(root.right, node)
    
    @staticmethod
    def inorder(root):
        if root:
            inorder(root.left)
            print(root.value)
            inorder(root.right)

r = Node(100)
r.insert(r,  Node(12))
r.inorder(r)