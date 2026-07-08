class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            k=i+1
            if k<len(arr):
               arr[i]=max(arr[k:len(arr)])
        arr[i]=-1
        return arr

