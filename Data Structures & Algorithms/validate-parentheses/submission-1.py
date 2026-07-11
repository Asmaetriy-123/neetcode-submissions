class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets={
            "{":"}",
            "[":"]",
            "(":")"
        }
        stack=[]
        for i in range(len(s)):
            if s[i]in matching_brackets:
                stack.append(s[i])
            elif len(stack)==0 or s[i]!=matching_brackets[stack.pop()]:
                return False
        return not stack    
            

        