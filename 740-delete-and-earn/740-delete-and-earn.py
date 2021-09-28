class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter, defaultdict 
        d = defaultdict(lambda : 0, Counter(nums))
        
        
        
        m1, m2 = d[1], max(d[1], d[2]*2)
        for i in range(3, max(d.keys())+1):
            m1, m2 = m2, max(m1 + d[i]*i,  m2)
        
        return(m2)
        
        