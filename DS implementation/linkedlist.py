#Create a linked list in python. Python doesn't ship with builtin linked list like java.
# Here's creating one.

class Node:
    # constructor
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self, nodes = None):  
        self.head = None
        if nodes:
            node = Node(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while (node):
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # insertion method for the linked list at end
    def insert(self, data):

        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    #add node to beginning of list
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # add node after a specific element
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.next.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            if curr.next == None:
                self.head = curr
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
    #traverse a linked list
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

# Linked List with a single node
LL = LinkedList()
LL.head = Node(3)
LL.insert(4)
LL.insert(7)
LL.add_before(7, Node(8))
print(LL)
LL.reverse()
print(LL)