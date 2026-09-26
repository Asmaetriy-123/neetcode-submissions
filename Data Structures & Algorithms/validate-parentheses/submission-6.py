class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict={
            "{":"}",
            "[":"]",
            "(":")"
        }

        opening_brackets_stack=[]
        for char in s :
            if char in bracket_dict:
                #if it's an opening bracket we will append it to the stack
                opening_brackets_stack.append(char)
            elif opening_brackets_stack:
                    #making sure first that the stack is not empty
                    #then we check if the closing bracket in the string doesn't match the 
                    #latest opening bracket popped from the stack
                    #if that's the case the string is not valid
                    if bracket_dict[opening_brackets_stack.pop()]!=char:
                        return False
            else:
                #if the opening_brackets_stack is empty but there's a closing 
                # character in the "s"
                return False            
        if not opening_brackets_stack:
            #if openning brackets and closing brackets match and 
            #there are no opening brackets left when we exited the loop
            #then the string is valid
            return True 
        else:
            #if we went through the entire string but there are still
            #characters left in the stack then that means the string is not valid
            return False                  






            
        