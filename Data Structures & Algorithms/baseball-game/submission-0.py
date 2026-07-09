class Solution:
    def calPoints(self, operations: List[str]) -> int:
       # top=len(operations)-1
        top=-1
        record=[]
        newVal=0
        for i in range(len(operations)):
            if operations[i] not in ['C', 'D', '+']:
                top+=1
                record.append(int(operations[i]))
               
            elif operations[i]=='D':
               
                newVal= record[top]*2
                record.append(newVal)
                top+=1
                
            elif operations[i]=='+':
                
                newVal= record[top]+record[top-1]
                record.append(newVal)
                top+=1
               
            elif operations[i]=='C'and len(record)>=1:
                del record[top]
                top-=1
        return sum(record)




        