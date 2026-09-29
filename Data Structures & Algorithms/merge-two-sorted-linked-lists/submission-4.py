# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        curr1=list1
        curr2=list2
        curr3=list3
       # count_list1=count_list2=0
        """while list1!=None:
            list1=list1.next
            count_list1+=1
        while list2!=None:
            list2=list2.next
            count_list2+=1
        min_length=min(count_list1,count_list2)"""
        ##now we're done with knowing which list has the least number of nodes 

      #  if count_list1<count_list2:
        while curr1!=None and curr2!=None:
            if curr1.val<=curr2.val:
                curr3.next=curr1
                curr3=curr3.next
                curr1=curr1.next
            
            else:
                curr3.next=curr2
                curr3=curr3.next
                curr2=curr2.next 
        if curr1==None and curr2!=None:
            while curr2!=None:
                    curr3.next=curr2
                    curr3=curr3.next
                    curr2=curr2.next   
        else:
            while curr1!=None:
                    curr3.next=curr1
                    curr3=curr3.next
                    curr1=curr1.next   
        return list3.next         


        





        