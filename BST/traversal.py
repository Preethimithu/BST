# In-order traversal
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

in_order_traversal(root)
print("\n")

# Pre-order traversal

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def pre_order_traversal(root):
    if root:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

pre_order_traversal(root)
print("\n")

# Post-order traversal
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

post_order_traversal(root)
