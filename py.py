def prepend(self,value):
    new_node = Node(value)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length +=1
        return True
    
def popfirst(self,value):
    if self.length == 0:
        return None
    temp = self.head
    if self.length == 1:
        self.head = None
        self.tail = None
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -=1
        return temp
    



    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp
    

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length ==  1:
            self.head = none
            self.tail = none
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -=1
    
        return temp
    

    def get(self,index):
        if index <0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            return temp 