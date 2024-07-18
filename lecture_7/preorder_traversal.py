# прямий обхід бінарного дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Прямий обхід:") # Прямий обхід: 1 2 4 5 3
preorder_traversal(root)
