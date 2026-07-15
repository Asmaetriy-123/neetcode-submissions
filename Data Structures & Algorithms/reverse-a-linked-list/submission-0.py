# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        if not head:
         return head
        current=head
        while current:
            stack.append(current.val)
            current=current.next
        head=ListNode(stack.pop())
        tail=head
        
        while stack:
            node=ListNode(stack.pop())
            tail.next=node
            tail=node
        return head
            
    


        




        
        