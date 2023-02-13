class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    if value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)

def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

value = 80
if search(root, value):
    print(f"{value} is found in the BST.")
else:
    print(f"{value} is not found in the BST.")
