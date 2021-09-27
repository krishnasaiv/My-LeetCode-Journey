# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        if n == 1:
            if isBadVersion(1):
                return(1)
        
        l, r = 1, n
        while l <= r:
            m = (l+r) // 2
            
            cur, prev = isBadVersion(m), isBadVersion(m-1)
            if cur and (not prev):
                return(m)
            elif cur and prev:
                r = m - 1
            else:
                l = m + 1
                
            
        