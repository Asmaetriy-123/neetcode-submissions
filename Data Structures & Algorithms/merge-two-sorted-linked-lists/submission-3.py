# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode=ListNode(0)
        mergedListPointer=dummyNode
        currentList1=list1
        currentList2=list2
        while currentList1 and currentList2:
            if currentList1.val<=currentList2.val:
                mergedListPointer.next=currentList1
                currentList1=currentList1.next
            else:
                mergedListPointer.next=currentList2
                currentList2=currentList2.next   
            mergedListPointer= mergedListPointer.next    
        if not currentList1:   
             mergedListPointer.next=currentList2
        else:
             mergedListPointer.next=currentList1  
        return dummyNode.next    

        