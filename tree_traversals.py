class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def Inorder(self, root):
        if root:
            self.Inorder(root.left)
            print(root.val)
            self.Inorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.Inorder(root)


