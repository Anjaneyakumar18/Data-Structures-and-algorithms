class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Treenode(val)
            return
        self.insert_rec(val, self.root)

    def insert_rec(self, val, root):
        if not root:
            return Treenode(val)  # return a new node to be assigned as child
        
        # Use recursion to find the correct position to insert the new value
        if val < root.val:
            root.left = self.insert_rec(val, root.left)
        else:
            root.right = self.insert_rec(val, root.right)
        
        return root  # return the root after modification

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)
    
        

# Create a Tree and insert values
tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(8)
tree.insert(20)


# Perform inorder traversal
tree.inorder(tree.root)
print('level')
