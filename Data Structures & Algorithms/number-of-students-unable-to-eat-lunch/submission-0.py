from collections import deque       
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        sandwiches = deque(sandwiches)
        rejected = 0                      # how many in a row said "no"
        while q:
           if q[0] == sandwiches[0]:
              q.popleft()
              sandwiches.popleft()
              rejected = 0
           else:
             q.append(q.popleft())    # to the back
             rejected += 1
           if rejected == len(q):       # everyone left has refused the top
             break
        return len(q)