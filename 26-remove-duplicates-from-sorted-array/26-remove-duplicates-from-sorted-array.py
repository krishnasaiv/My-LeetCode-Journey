class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) < 2: return(len(nums))
        
        l = 0
        r = 1
        
        while True:
            while nums[l] == nums[r]:
                r += 1
                if r >= len(nums):
                    return(l+1)
            l += 1
            nums[l] = nums[r]
        
        
        return(l+1)