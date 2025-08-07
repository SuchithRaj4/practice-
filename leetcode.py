class solution:
    def pop (self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = None
            self.tail = None 
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length -=1
            return true
    
class suvhith:
    def hascycle(self,head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            return False