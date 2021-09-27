class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            
            while  nums[num-1] != num:
                nums[num-1], num = num, nums[num-1]
        
        misssing_numers = list()
        for i in range(len(nums)):
            if nums[i] != i+1:
                misssing_numers.append(i+1)
        
        return(misssing_numers)
    
############# Time Complexity: O(n) #############
## 1. Swap once for each index ---> O(n)
## 2. Iterate to find the missing element ---> O(n)

############# Space Complexity: O(1) #############
## 1. No extra space apart from the 'misssing_numers' ---> O(1)
        