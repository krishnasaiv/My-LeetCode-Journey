class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        reachable = [False]*len(nums)
        reachable[0] = True
        
        
        for i in range(1, len(nums)):
            lookBack = 1
            
            while i-lookBack >= 0:
                if nums[i-lookBack] >= lookBack and reachable[i-lookBack] :
                    reachable[i] = True
                    break
                
                lookBack += 1
            
        return(reachable[-1])
        
            