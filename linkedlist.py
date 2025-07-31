class Node:
    def __init__(self,value):
        self.value = value
        self.Next = None

class LinkedList:
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length = +1
            return True 
        