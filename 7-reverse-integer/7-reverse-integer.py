class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return(0)
        
        
        while x % 10 == 0:
            x //= 10
            
        num =int(str(x)[::-1].replace('-', '')) * (1 if x > 0 else -1)
        if num > 2**31-1 or num < -2**31:
            return(0)
        
        return(num)
        
        