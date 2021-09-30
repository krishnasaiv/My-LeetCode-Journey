class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return(nums[0])
        
        
        maxSubarraySum = runningSubarraySum = float('-inf')
        for i in range(len(nums)):
            
            runningSubarraySum = max(runningSubarraySum+nums[i], nums[i])
            maxSubarraySum = max(maxSubarraySum, runningSubarraySum)
            # print(nums[i], runningSubarraySum, maxSubarraySum)
        
        return(maxSubarraySum)
    
#         maxSubarraySum = runningSubarraySum = float('-inf')
#         for i in range(len(nums)):
            
#             if nums[i] < 0:
#                 maxSubarraySum = max(maxSubarraySum, runningSubarraySum)
#                 runningSubarraySum = nums[i]
#             else:
#                 if runningSubarraySum < 0:
#                     maxSubarraySum = max(maxSubarraySum, runningSubarraySum)
#                     runningSubarraySum = nums[i]
#                 else:
#                     runningSubarraySum += nums[i]
        
#         return(maxSubarraySum)
            
        