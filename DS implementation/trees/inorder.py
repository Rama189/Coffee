
#implement a binary tree
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = Node(root)
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        
    def _insert(self, root, data):
        if not root:
            return Node(data)
        if root.data > data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root
    
    def preorder(self, root, res):
        
        if not root:
            return ""
        # res = res + "-" + str(root.data)
        # res = res + self.preorder(root.left, res)
        # res = res + self.preorder(root.right, res)

        return str(root.data) + "-" + self.preorder(root.left, res) + self.preorder(root.right, res)

        # return res

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            res = self.preorder(self.root, res="")
            print(res)
    
    

            

tree = BST(1)
# print(root.data)
tree.insert(9)
tree.insert(3)
tree.insert(19)
tree.insert(24)
tree.insert(5)
tree.insert(21)

# root.left = BST(9)
print(tree.root.right.left.right.data)
# print(tree.root.left.data)
tree.print_tree("preorder")