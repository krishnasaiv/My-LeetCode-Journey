class Solution:
    def squareSum(self, num):
        s = 0
        while num:
            s += (num%10)**2
            num //= 10
        return s
    
    
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        
        while True:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))
            
            if fast == 1:
                return True
            
            if slow == fast:
                return False
            
            
        
        
        