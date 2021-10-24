class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) <= 1: return(len(nums))
        
#         l = 0
#         r = 1
        
#         while True:
#             while nums[l] == nums[r]:
#                 r += 1
#                 if r >= len(nums):
#                     return(l+1)
#             l += 1
#             nums[l] = nums[r]

        
        lnth = 0
        for i in range(1, len(nums)):
            
            if nums[i] > nums[lnth]:
                lnth += 1
                nums[lnth] = nums[i]
        
        return(lnth+1)
    
#############     Strategy         #############
## 2 pointer iteration
## One iterator points to the position in array & the other to the position of placing the next number

############# Time Complexity: O(n) #############
## 1. Iterate once ---> O(n)

############# Space Complexity: O(1) #############
## 1. No extra Space ---> O(1)
                