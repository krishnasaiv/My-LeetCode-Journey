class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        e, o = 0, 1
        
        while True:
            while e < len(nums) and nums[e]%2 == 0 :
                e += 2
            
            while o < len(nums) and nums[o]%2 == 1 :
                o += 2
            # print(e, o)
            
            if e > len(nums) or o > len(nums):
                break
            nums[e], nums[o] = nums[o], nums[e]
            
            e += 2
            o += 2
            
        return(nums)
        