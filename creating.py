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

def preped(self,value):
    new_node = Node(value)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
        self.length = +1
        return True

def pop_first(self):
    if self.length == 0:
        return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length = -1
    return True 

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp 
            temp = after



    