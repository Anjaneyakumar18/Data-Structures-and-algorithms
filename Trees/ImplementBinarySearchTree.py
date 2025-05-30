
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,val):
        def _insert(node,val):
            if not node:
                return Node(val)
            if val<node.val:
                node.left=_insert(node.left,val)
            else:
                node.right=_insert(node.right,val)
            return node
        self.root=_insert(self.root,val)

    def search(self,val):
        def _search(node,val):
            if not node:
                return False
            if node.val==val:
                return True
            if val<node.val:
                return _search(node.left,val)
            else:
                return _search(node.right,val)
        return _search(self.root,val)

    def inorder(self):
        res=[]
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            res.append(node.val)
            _inorder(node.right)
        _inorder(self.root)
        return res

# Test cases
bst=BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(20)

print(bst.inorder())       # [2, 5, 7, 10, 12, 15, 20]
print(bst.search(7))       # True
print(bst.search(14))      # False
print(bst.search(10))      # True
