class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1 :  return
        
        ind = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[ind] = nums[i]
                ind += 1
        for i in range(ind, len(nums)):
            nums[i] = 0
        
                
        