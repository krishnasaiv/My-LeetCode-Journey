class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k==0 or len(nums) == 1:
            return
        
        l, r = 0, len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l += 1
            r -= 1
        
        l, r = 0, k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l += 1
            r -= 1
            
        l, r = k, len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l += 1
            r -= 1
        return
    
    
############# Time Complexity: O(n) #############
## 1. Reverse entire array -->  O(n)
## 2. reverse k elements ---> O(k)
## 3. Reverse n-k elements ---> O(n-k)

############# Space Complexity: O(1) #############
## 1. No extra space ---> O(1)


############# Other Methods
## 1. Shift each element k%len(nums) times --> T: Omega(n * k%len(nums)); Worst case T: O(n**2); S: O(1)
## 2. Iterate trhough array, move each element to it's position after shift & move the element at the position to it's respective position & so on. But we need to store which elements are already moved/ which elements are already in right place. T: O(n); S:O(n)
