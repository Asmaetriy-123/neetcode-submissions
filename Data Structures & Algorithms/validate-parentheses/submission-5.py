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
                opening_brackets_stack.append(char)
            elif opening_brackets_stack:
                    if bracket_dict[opening_brackets_stack.pop()]!=char:
                        return False
            else:
                #if the opening_brackets_stack is empty but there's a character in the "s"
                return False            
        if not opening_brackets_stack:
            return True 
        else:
            return False                  







        '''for i in range(s) :
            if i==0 and s[i] not in bracket_dict:
                return False
            elif len(s)/2!=0:
                return False

            else:
                if s[i] in bracket_dict.values:
                    if s[i]=="}" and s[i-1]!='{':
                        return False
                    elif s[i]=="]" and s[i-1]!='[':
                        return False
                    elif s[i]==")" and s[i-1]!="(":
                        return False
                        '''
                        



            
        