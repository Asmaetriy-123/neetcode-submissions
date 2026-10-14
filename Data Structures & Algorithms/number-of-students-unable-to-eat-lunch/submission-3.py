class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Step 1: Count total preferences
        # count[0] = number of students who want circular
        # count[1] = number of students who want square
        count = [students.count(0), students.count(1)]
        
        # Step 2: Loop through the sandwiches from top to bottom
        for sandwich in sandwiches:
            # STOPPING CONDITION: If no students left want this type of sandwich,
            # the line stalls completely. 
            if count[sandwich] == 0:
                break
                
            # Otherwise, a matching student takes it and leaves
            count[sandwich] -= 1
            
        # The number of students unable to eat is just the total remaining count
        return count[0] + count[1]
        