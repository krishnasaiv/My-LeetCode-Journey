class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        from collections import Counter
        c = Counter(nums)
        
        return( max(c.values()) > 1 )
        