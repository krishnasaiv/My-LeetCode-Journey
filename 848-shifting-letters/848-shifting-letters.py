class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        offset = shifts[-1] % 26
        shifts[-1]  = chr((ord(s[-1]) -97 + offset)% 26 + 97)
        for i in range( len(shifts) -2, -1, -1 ):
            offset += shifts[i] 
            offset %= 26
            
            shifts[i]  = chr((ord(s[i]) -97 + offset)% 26 + 97)
    
        return ("".join(shifts))
            
############# Time Complexity: O(n) #############
## 1. Iterate through the array in reverse & add offset to each character 


############# Space Complexity: O(n) #############
## 1. Space for the output