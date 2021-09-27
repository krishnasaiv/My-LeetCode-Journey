class Solution:
    def hammingWeight(self, n: int) -> int:
 
        numOnes = 0
        
        while n:
            numOnes += n % 2
            n //= 2
            
        return(numOnes)
            
        
        