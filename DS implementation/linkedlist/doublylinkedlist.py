# References: https://www.educative.io/edpresso/how-to-create-a-doubly-linked-list-in-python

# Creating a node class
class Node:
  def __init__(self, data):
    self.data = data #adding an element to the node
    self.next = None # Initally this node will not be linked with any other node
    self.prev = None # It will not be linked in either direction

class DoublyLinkedList:
    def __init__(self):
        self.head = None # Initally there are no elements in the list
        self.tail = None

    def push_front(self, new_data): # Adding an element before the first element
        new_node = Node(new_data) # creating a new node with the desired value
        new_node.next = self.head # newly created node's next pointer will refer to the old head

        if self.head != None: # Checks whether list is empty or not
            self.head.prev = new_node # old head's previous pointer will refer to newly created node
            self.head = new_node # new node becomes the new head
            new_node.prev = None
        
        else: # If the list is empty, make new node both head and tail
            self.head = new_node
            self.tail = new_node
            new_node.prev = None # There's only one element so both pointers refer to null

    def push_back(self, new_data): # Adding an element after the last element
        new_node = Node(new_data)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node 
            self.tail = new_node

    def peek_front(self): # returns first element
        if self.head == None: # checks whether list is empty or not
            print("List is empty")
        else:
            return self.head.data

    def peek_back(self): # returns last element
        if self.tail == None: # checks whether list is empty or not
            print("List is empty")
        else:
            return self.tail.data
    
    def pop_front(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            return temp.data
        else:
            print("List is empty")
    
    def pop_back(self): # removes and returns the last element
        if self.tail == None:
            print("List is empty")
        else:
            temp = self.tail
            temp.prev.next = None # removes next pointer referring to old tail
            self.tail = temp.prev # make second to last element the new tail
            temp.prev = None # remove previous pointer referring to new tail
            return temp.data

# TODO: Check these once, 
    def insert_after(self, temp_node, new_data): # Inserting a new node after a given node
        if temp_node == None:
            print("Given node is empty")
        if temp_node != None:
            new_node = Node(new_data)
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node
            if new_node.next != None:
                new_node.next.prev = new_node
            
            if temp_node == self.tail: # checks whether new node is being added to the last element
                self.tail = new_node # makes new node the new tail
        

  
    def insert_before(self, temp_node, new_data): # Inserting a new node before a given node
        if temp_node == None:
            print("Given node is empty")
        if temp_node != None:
            new_node = Node(new_data)
            new_node.prev = temp_node.prev
            temp_node.prev = new_node
            new_node.next = temp_node
            if new_node.prev != None:
                new_node.prev.next = new_node
            
            if temp_node == self.head: # checks whether new node is being added before the first element
                self.head = new_node # makes new node the new head

            
