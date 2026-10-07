
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None

class MyLinkedList:

    def __init__(self):
        self.head=Node(-1)
        self.tail=Node(-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0

       
    def get(self, index: int) -> int:
        curr=self.head.next
        count=0
        while curr!=None:
            if count==index:
                return curr.val
            curr=curr.next
            count+=1
        return -1    
        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        temp=self.head.next
        self.head.next=new_node
        new_node.prev=self.head
        new_node.next=temp
        temp.prev=new_node
        self.size+=1
       
        

    def addAtTail(self, val: int) -> None:
       
        new_node=Node(val)
        temp=self.tail.prev
        self.tail.prev=new_node
        new_node.next=self.tail
        new_node.prev=temp
        temp.next=new_node
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
           self.addAtHead(val)
           return
        curr=self.head.next
        count=0
        new_node=Node(val)

        if index==self.size:
            self.addAtTail(val)
            return
        elif index>self.size:
            return    
        
        while curr!=None :
            if count==index:
                temp=curr
                curr.prev.next=new_node
                new_node.prev=curr.prev
                new_node.next=temp
                temp.prev=new_node
                self.size+=1
                break
            curr=curr.next
            count+=1
            
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
          return
        curr=self.head
        count=0
        if index<=self.size:
          while curr!=None :
            if count==index:
                temp=curr
                curr.prev.next=curr.next
                curr.next.prev=curr.prev
                self.size-=1
                break
            curr=curr.next
            count+=1
        else:
            self.size-=1
            return    


    



        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)