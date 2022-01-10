class Solution:
    
    def BinSearch(self, arr, l, r, target):
        if l > r:
            return -1
        m = (l+r) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m-1
        else:
            l = m+1
        return self.BinSearch(arr, l, r, target)
        
    
    def search(self, nums: List[int], target: int) -> int:
        
        l = len(nums)
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        #### Find the offset of the rotated array
        offset = 0
        # Find offset only if it is rotated
        if nums[0] > nums[-1] :
            
            s, e = 0, len(nums)-1
            while s <= e:
                m = (s+e) // 2
                # print(s, e, m)
                if nums[m] == target:
                    return m
                else:
                    if nums[m] <= nums[-1] :  # = is important & nums[-1] is important
                        e = m-1
                    elif nums[m] >= nums[0] : # = is important & nums[0] is important
                        s = m+1
                # print(s, e, m)
            offset = e
            
        # print(offset)
        if nums[0] <= target <= nums[offset] :
            return self.BinSearch(nums, 0, offset , target)
        else:
            return self.BinSearch(nums, offset+1, len(nums)-1, target)
        
############# Time Complexity: O(log(n)) #############
## 1. Bin Search in entire array for offset ---> O(log(n))
## 2. Bin Search in 0:offset --->O(log(offset))
## 3. Bin Search in offset:n-1 ---> O(log(n-offset))

############# Space Complexity: O(1) #############
## 1. No extra space
        
        
