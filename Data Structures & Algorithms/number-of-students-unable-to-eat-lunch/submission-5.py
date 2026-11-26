class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students=deque(students)
        sandwiches = deque(sandwiches)
        while sandwiches and sandwiches[0] in students:
            if sandwiches[0]==students[0]:
                sandwiches.popleft()
                students.popleft()
            else:
                students.append(students.popleft())    
                
              
        return len(sandwiches)        
        

        