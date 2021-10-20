class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         from functools import reduce
#         return( reduce(lambda x,y: x^y, nums + [i for i in range(len(nums)+1)]))
        
        return(len(nums) * (len(nums)+1) // 2 - sum(nums))
    