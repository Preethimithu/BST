class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def find_min(root):

    if root is None:
        return float("inf")
    elif root.left is None:
        return root.data
    else:
        return find_min(root.left)

def find_max(root):

    if root is None:
        return float("-inf")
    elif root.right is None:
        return root.data
    else:
        return find_max(root.right)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(7)

print("Minimum element in the BST is:", find_min(root))
print("Maximum element in the BST is:", find_max(root))

"""
In this code, float("inf") is used to represent positive infinity and 
float("-inf") is used to represent negative infinity.
"""