from collections import deque
 
# Initializing a queue

 
class Solution:
    def isValid(self, s):
        
        if len(s) % 2 == 1:
            return(False)
        
        
        parentheses = {'{':'}','[':']','(':')', }
        q = deque()
        for char in s:
            if char in parentheses.keys():
                q.append(char)
            else:
                if (not q) or parentheses[q[-1]] != char :
                    return(False)
                else:
                    q.pop()
        if q:
            return(False)
        else:
            return(True)
                
            
        
        