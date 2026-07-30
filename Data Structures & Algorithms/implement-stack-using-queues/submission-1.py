from collections import deque
class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
         self.q.append(x)                 # add new element at the back
         for _ in range(len(self.q) - 1): # rotate all the OLDER ones...
            self.q.append(self.q.popleft())  # ...take from front, put at back
        # now x is at the front
    def pop(self) -> int:
        
        return self.q.popleft() 
        

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
       return not self.q    
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()