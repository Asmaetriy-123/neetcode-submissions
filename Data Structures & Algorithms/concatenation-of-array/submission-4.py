class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        new_length=len(nums)*2
        j=0
        for i in range(new_length):
            if i==len(nums):
                j=0
            ans.append(nums[j])
            j+=1
        return ans    

        