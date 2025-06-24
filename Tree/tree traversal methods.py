class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.key, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=' ')

# Build the tree
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

print("Preorder: ")
preorder(root)
print("\nInorder: ")
inorder(root)
print("\nPostorder: ")
postorder(root)
