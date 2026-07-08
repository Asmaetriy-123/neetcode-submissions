class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        differentElements=[]
        

        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]="##"
               # print(f"this is {nums[i]}")
               # print(f"this is nums {nums}")
                
            elif nums[i]!=val:
                k+=1 
                differentElements.append(nums[i])
               # print(f"this is the distinct value array {differentElements}")
        for j in range(len(nums)):
            if j<len(differentElements):
              nums[j]=differentElements[j]
            else:
                nums[j]="#" 
        #print(f" the nums array is now {nums}")
        return k        


