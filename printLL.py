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
    
    temp = self.head
    pre = self.head

    while (temp.next):
        pre = temp 
        temp = temp.next 
        self.tail = pre
        self.tail.next = None

