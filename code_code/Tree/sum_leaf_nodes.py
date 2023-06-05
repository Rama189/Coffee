
 # Class for node creation
class Node:
      
     # Constructor
    def __init__(self, data):             
        self.data = data
        self.left = None
        self.right = None

def leafSum(root):
    global total

    if not root:
        return 0
    
    if not root.left and not root.right:
        total = total + root.data

    leafSum(root.left)
    leafSum(root.right)

# Binary tree Formation
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(7)
    root.right.left = Node(6)
    root.right.left.right = Node(8)
# Variable to store the sum of leaf nodes
    total = 0
    leafSum(root)
# Printing the calculated sum
    print(total)