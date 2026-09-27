class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets={
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack=[]
        for char in s :
            if char in matching_brackets:
                if stack and stack[-1]==matching_brackets[char]:
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(char)
        return True if not stack else False            

           




            
        