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

    def finding_middle_(self):
        slow = self.head
        fast = self.head
        while fast is None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            return True
    def fib(n):
        fib_list = [0,1]
        for index in range(2, n+1):
            next_fiblist = fib_list[index -1] + fiblist[index -2 ]
            next_fiblist.append(next_fiblist)
            return n 
        
class doublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = -1
        return True
    
class append:
    def __init__(self,value):
        new_node = Node(value)
        if self.head is not None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node[]

class doubleLinkedList:
    def __init__(self,value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = -1
        return True
    
class pop(self,value):
    if self.length == 0:
        return None
    temp = self.tail
    self.tail = self.tail.prev
    self.tail.next = None
    temp.prev = None
    self.length = -1
    return None 