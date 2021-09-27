class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return(nums)
        currentRangeStart = currentRangeEnd = nums[0]
        ranges = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                currentRangeEnd = nums[i]
            else:
                ranges.append(str(currentRangeStart) if currentRangeStart == currentRangeEnd else f"{currentRangeStart}->{currentRangeEnd}")
                currentRangeStart = currentRangeEnd = nums[i]
        ranges.append(str(currentRangeStart) if currentRangeStart == currentRangeEnd else f"{currentRangeStart}->{currentRangeEnd}")
        return(ranges)
            
            
            