class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in range (len(operations)):
            if operations[i].lstrip("-").isdigit():
                stack.append(int(operations[i]))
            elif operations[i]=="+" and len(stack)>=2:
                stack.append(stack[-1]+stack[-2])
            elif operations[i]=="D" and stack:
                stack.append(stack[-1]*2)
            elif operations[i]=="C" and stack:
    
                stack.pop()  
        return sum (stack)               


        