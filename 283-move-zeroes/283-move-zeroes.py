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
            
    
#############     Strategy         #############
## 2 pointer iteration
## One iterator points to the position in array & the other to the position of placing the next number

############# Time Complexity: O(n) #############
## 1. Iterate once ---> O(n)

############# Space Complexity: O(1) #############
## 1. No extra Space ---> O(1)
                
        