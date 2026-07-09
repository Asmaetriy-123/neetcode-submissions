class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        nums_length=len(nums)
        k=0
        j=0
        for i in range(2*nums_length):
            if j<nums_length:
                ans.append(nums[i])
                j+=1
               
            else:
              
              
               ans.append(nums[k])
               k+=1
        return ans
