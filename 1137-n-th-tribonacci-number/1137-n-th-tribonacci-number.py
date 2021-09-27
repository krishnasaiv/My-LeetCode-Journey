class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return(n)
        if n == 2:
            return(1)
        
        f1, f2, f3 = 0, 1, 1
        
        for i in range(3, n+1):
            f1, f2, f3 = f2, f3, f1+f2+f3
        
        return(f3)