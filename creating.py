class Node:
    def __init(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

def append(self,value): 
    newnode = Node(value)
    if self.head is  None:
        self.head = newnode
        self.tail = newnode
        self.length = +1 


def pop(self,value):
    if length == 0:
        return None
    temp = self.head
    pre = self.head
    while(temp.next):
        pre = temp
        temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length = -1 
    if length == 0:
        self.head = None
        self.tail = None
