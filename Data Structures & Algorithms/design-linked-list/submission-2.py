
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:
     
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.size=0

    def get(self, index: int) -> int:
        curr=self.head
        count=0
        while curr:
            if count==index:
                return curr.val
            else:
                curr=curr.next
                count+=1 
        return -1           

        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        self.size+=1
        if self.head is None:
           self.head = new_node
           self.tail = new_node
           return
        
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node


    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        self.size+=1
        if self.tail is None:
            self.tail=new_node
            self.head=new_node
            return
        new_node.prev=self.tail    
        self.tail.next=new_node
        self.tail=new_node

        

    def addAtIndex(self, index: int, val: int) -> None:
        curr=self.head
        count=0
        new_node=Node(val)
        if index>self.size:
            return
        
        if index==0:
            self.addAtHead(val)
            return
        if index==self.size:
            self.addAtTail(val)
            return
       
        while curr:
            
            if count==index:
                curr.prev.next=new_node
                new_node.prev=curr.prev
                new_node.next=curr
                curr.prev=new_node
                break
            else:
                curr=curr.next
                count+=1  
        self.size+=1          

    def deleteAtIndex(self, index: int) -> None:
        curr=self.head
        count=0
        if index not in range(self.size):
            return
        while curr:
            if count==index:
                if curr.prev:
                   curr.prev.next = curr.next   # your line, unchanged
                else:
                   self.head = curr.next        # head case

                if curr.next:
                   curr.next.prev = curr.prev   # your line, unchanged
                else:
                   self.tail = curr.prev        # tail case
                break   
                '''
                curr.prev.next=curr.next
                curr.next.prev=curr.prev
                break'''
            else:
                curr=curr.next
                count+=1    
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)