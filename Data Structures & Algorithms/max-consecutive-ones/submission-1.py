class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        seen={}
        list_items=[]
        count=0
        for num in nums:
            if num==1:
                count+=1
                seen[1]=count
                
            elif num!=1 and 1 in seen :
               list_items.append(seen[1])
               count=0
            else:
               list_items.append(0) 
        if 1 in seen :         
          list_items.append(seen[1]) 
        return max(list_items)
        