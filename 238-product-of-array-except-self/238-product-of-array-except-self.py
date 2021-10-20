class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0 :
                numZeros += 1
            else:
                product *= nums[i]
            
        
        if numZeros > 1:
            return([0] * len(nums))
        elif numZeros == 1:
            return ([0 if nums[i] != 0 else product for i in range(len(nums))])
        else:
            return([product // i for i in nums])
        