class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return(n)
        n1, n2 = 1, 2
        
        for i in range(3, n+1):
            num = n1 + n2
            n1, n2 = n2, num
            
        return(n2)
        
        
############# Time Complexity: O(n) #############
## 1. Iterate from 3 to n ---> O(n)

############# Space Complexity: O(1) #############
## 1.No extra space ---> O(1)
        
        
       
        
        
        
        
        