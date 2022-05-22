#Create a linked list in python. Python doesn't ship with builtin linked list like java.
# Here's creating one.

class Node:
    # constructor
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

# Creating a single node
first = Node(3)
print(first.data)