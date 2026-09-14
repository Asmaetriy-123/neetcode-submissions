class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            if 1 not in nums :
                return 0
            
            count=max_value=0
            for num in nums:
                if num==1:
                    count+=1
                    
                else:
                    max_value=max(max_value,count)
                    count=0  

            return max(max_value,count)    

        