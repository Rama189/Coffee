# Python program to find maximumpath sum between two leaves
# of a binary tree

INT_MIN = -2**32

# A binary tree node


class Node:
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Utility function to find maximum sum between any
# two leaves. This function calculates two values:
# 1) Maximum path sum between two leaves which are stored
# in res
# 2) The maximum root to leaf path sum which is returned
# If one side of root is empty, then it returns INT_MIN


def maxPathSumUtil(root, res):
    if not root:
        return 0
    
    l_v = maxPathSumUtil(root.left, res)
    r_v = maxPathSumUtil(root.right, res) 

    temp = root.data + max(l_v, r_v)
    # ans = max(temp, root.data  + l_v, r_v)
    res[0] = max(res[0], root.data  + l_v + r_v)
    return temp

def maxPathSum(root):
	res = [INT_MIN]
	maxPathSumUtil(root, res)
	return res[0]


# Driver program to test above function
root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)

print ("Max pathSum of the given binary tree is", maxPathSum(root))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
