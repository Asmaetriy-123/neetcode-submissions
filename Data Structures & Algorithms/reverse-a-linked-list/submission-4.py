# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:      # base case: empty or single node
           return head

        newHead = self.reverseList(head.next)   # reverse everything after head
        head.next.next = head              # make the next node point back at me
        head.next = None                   # I become the new tail

        return newHead                     # front of the reversed list, passed up
       

        
        