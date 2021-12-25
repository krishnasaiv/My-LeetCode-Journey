class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return(nums[0])
        
        
        maxSubarraySum = runningSubarraySum = nums[0]
        for num in nums[1:]:
            
            runningSubarraySum = max(runningSubarraySum + num, num)
            maxSubarraySum = max(maxSubarraySum, runningSubarraySum)
            
        return(maxSubarraySum)
