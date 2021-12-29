class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x <= 1 :
            return x
        
        l, r = 2, x-1
        while l <= r:
            m = (l+r)//2
            sq = m*m
            if x < sq:
                r=m-1
            elif x > sq:
                l=m+1
            else:
                return m
        
        return l-1      ## square of everything before l is always lesser than the target
                        ## square of everything after r is always greater than the target
                
        