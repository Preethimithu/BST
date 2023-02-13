class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def find_prefix(root, prefix):

    if root is None:
        return []
    elif root.data.startswith(prefix):
        return [root.data] + find_prefix(root.left, prefix) + find_prefix(root.right, prefix)
    elif root.data < prefix:
        return find_prefix(root.right, prefix)
    else:
        return find_prefix(root.left, prefix)

def find_suffix(root, suffix):

    if root is None:
        return []
    elif root.data.endswith(suffix):
        return [root.data] + find_suffix(root.left, suffix) + find_suffix(root.right, suffix)
    elif root.data < suffix:
        return find_suffix(root.right, suffix)
    else:
        return find_suffix(root.left, suffix)

root = Node("dog")
root.left = Node("cat")
root.right = Node("elephant")
root.left.left = Node("crow")
root.left.right = Node("bird")
root.right.right = Node("giraffe")

print("Elements with prefix 'c' in the BST are:", find_prefix(root, "c"))
print("Elements with suffix 'fe' in the BST are:", find_suffix(root, "fe"))
