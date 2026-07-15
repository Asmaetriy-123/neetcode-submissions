# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)      # fake starting node
        tail = dummy

        # Phase 1: while BOTH lists have nodes, compare and take the smaller
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next    # only move the pointer we took from
            else:
                tail.next = list2
                list2 = list2.next    # only move the pointer we took from
            tail = tail.next          # tail always moves forward

        # Phase 2: attach the leftovers (one list is empty, the other may not be)
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # skip the dummy — the real list starts after it
        return dummy.next 
    
        


