class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return(max(nums))
        
        r1, r2 = nums[0], max(nums[:2])
        maxRobbable1 = r2
        for i in range(2, len(nums)-1):
            maxRobbable1 = max(r1 + nums[i], r2)
            r1, r2 = r2, maxRobbable1
        
        
        
        r1, r2 = nums[1], max(nums[1:3])
        maxRobbable2 = r2
        for i in range(3, len(nums)):
            maxRobbable2 = max(r1 + nums[i], r2)
            r1, r2 = r2, maxRobbable2
        
        return max(maxRobbable1, maxRobbable2)

############# Time Complexity: O(n) #############
## 1. Traverse the array 2 times ---> O(n)

############# Space Complexity: O(1) #############
## 1. No Extra Space ---> O(1)

