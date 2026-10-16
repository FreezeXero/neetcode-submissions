class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = [] #Stack 
        x = 0

        for char in operations:
            if char == "+":
                x = record[-1] +  record[-2]
                record.append(x)
            
            elif char == "D": 
                x =  record[-1]
                record.append(x * 2)
            
            elif char == "C": 
                record.pop()
            
            else:
                record.append(int(char))
        
        return sum(record)


        