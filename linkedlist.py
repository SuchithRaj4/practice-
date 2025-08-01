class Node:
    def __init__(self,value):
        self.value = value
        self.Next = None

class LinkedList:
    def get(self,index):
      if index <0 or  index >= self.length:
          return None
      temp = self.head
      for _ in range(index):
          temp = temp.next
          return temp
      
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length = -1
        return True 
    
    def set_values(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert_values(self,index,value):

       if index < 0 or index>  self.length: 
        return False
       if index == 0:
        return self.prepend(value)
        if index == self.length:
           
           return self.append(value)


