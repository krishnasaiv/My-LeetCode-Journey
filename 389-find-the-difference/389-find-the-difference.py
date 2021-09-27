from functools import reduce
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        a = ord(t[0])
        for b in (t+s)[1:]:
            a ^= ord(b)
        return(chr(a))
        
        # return(chr(  reduce( lambda a,b:a^ord(b), (t+s)[1:], ord(t[0]) ) ))
        
        # return(chr(reduce(lambda a,b:a^b, [ord(i) for i in s+t])))
        
    
    
############# Time Complexity: O(m+n) #############
## 1. Convert each ASCII character into ASCII Number ---> O(m+n)
## 2. Apply logical XOR between each consequtive ASCII number ---> O(m+n)

############# Space Complexity: O(1) #############
## 1. Only using 2 variables a, b
