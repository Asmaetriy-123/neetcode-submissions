class MinStack:

    def __init__(self):
        self.MinStack=[]
        self.min_values=[]
        

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        if not self.min_values:
            self.min_values.append(val)
        else:
            if val <=self.min_values[-1]:
                self.min_values.append(val)

                
        

    def pop(self) -> None:
        if self.MinStack[-1]==self.min_values[-1]:
            self.min_values.pop()
        self.MinStack.pop()
        
        

    def top(self) -> int:
        return self.MinStack[-1]
        

    def getMin(self) -> int:
        return self.min_values[-1]
        
