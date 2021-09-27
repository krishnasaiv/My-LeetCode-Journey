class Solution:
    def rob(self, nums: List[int]) -> int:
########################### T(n), S(1) ###########################
        if len(nums) == 1:
            return(nums[0])
        
        n1, n2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            n1, n2 = n2, max(nums[i] + n1,  n2)
        
        return(n2)
############# Time Complexity: O(n) #############
## 1. Iterate through the list ---> O(n)

############# Space Complexity: O(1) #############
## 1. Constant Space ---> O(1)


########################### T(n), S(n) ###########################
# if len(nums) == 1:
#             return(nums[0])
#         runningMaxRoabbale = [0] * len(nums)
#         runningMaxRoabbale[0] = nums[0]
#         runningMaxRoabbale[1] = max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             runningMaxRoabbale[i] = max(nums[i] + runningMaxRoabbale[i-2],  runningMaxRoabbale[i-1])

#         return(runningMaxRoabbale[-1])
############# Time Complexity: O(n) #############
## 1. Iterate through the list ---> O(n)

############# Space Complexity: O(n) #############
## 1. List of size 



           
