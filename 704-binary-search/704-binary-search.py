class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target or nums[-1] < target:
            return(-1)
        
        l, r = 0, len(nums)-1
        
        while l <= r : 
            m =(l+r)//2
            
            if nums[m] == target:
                return(m)
            
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        return(-1)