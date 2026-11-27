class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=Counter(students)
        res=len(students)
        for s in sandwiches:
            if count[s]>0:
                count[s]-=1
                res-=1
            else:
                return res
        return res            
                


