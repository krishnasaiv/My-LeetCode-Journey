class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]
        
        start = -1
        #### Find the starting position of the target
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if target < nums[m] :
                r = m-1
            elif target > nums[m] :
                l = m+1
            else:
                if m-1 >= 0 and nums[m-1] == nums[m]:
                    r = m-1
                else:
                    start = m
                    break
       
        end = -1
        #### Find the ending position of the target
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if target < nums[m] :
                r = m-1
            elif target > nums[m] :
                l = m+1
            else:
                if m+1 <= len(nums)-1 and nums[m] == nums[m+1]:
                    l = m+1
                else:
                    end = m
                    break
        return [start, end]        
        
        
        