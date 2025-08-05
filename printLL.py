class Node:
    def __init__(self,value):
        self.value = value
        self.next = none


class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

def append(self,value): 
    new_node = Node(value)
    if self.head is None:
        self.head = newnode
        self.tail = newnode 
    else:
        self.tail.next = newnode 
        self.tail = newnode
        self.length += 1 

def pop(self,value):
    if self.length == 0:
        return None
    
    temp =  self.head
    pre = self.head
    while(temp.next):
        pre = temp
        temp = temp.next


def pop(self,value):
    if self.length == 0:
        return None 
    temp = self.tail
    self.tail = self.prev.next
    self.tail.next = None
    temp.prev.next = None
    self.length = -1
    return True

def prepend (self,value):
    if self.length == 0:
        return None
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    else:
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node
    self.length = -1
    return True
    

        
