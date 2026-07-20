class Solution:
    def isValid(self, s: str) -> bool:
        matching_parentheses={
        "{":"}",
        "(":")",
        "[":"]"
       }
        stack=[]
        for ch in s:
            if ch in matching_parentheses.keys():
                stack.append(ch)
            elif ch in matching_parentheses.values():
                if not stack or ch!=matching_parentheses[stack.pop()]:
                    return False
        return not stack
                

        