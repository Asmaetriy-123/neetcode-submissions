from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q=deque(students)
        sandwiches=deque(sandwiches)
        rejected=0
        while q:
            if q[0]==sandwiches[0]:
                q.popleft()
                sandwiches.popleft()
                rejected=0
            else:
                q.append(q.popleft())  
                rejected+=1
                if len(q)==rejected:
                    break 
        return rejected            

        