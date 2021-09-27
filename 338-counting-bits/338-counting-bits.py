class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n<=1:
            return([i for i in range(n+1)])
        
        import math
        ans = [0]*(n+1)
        ans[1] = 1
        
        for i in range(2, n+1):
            nearestLower2Power = 2**int(math.floor(math.log2(i)))
            ans[i] = ans[i - nearestLower2Power] + 1 
        
        return(ans)
        
        