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
        if nums[0] > nums[-1] :
        
            # l, r = 0, len(nums)-2
            # m = (l+r) // 2
            # print(l, m, r)
            # while l <= r:
            #     if nums[m] > nums[m+1]:
            #         break
            #     else:
            #         if nums[m] < nums[r+1]:
            #             r = m-1
            #         elif nums[m] > nums[l]:
            #             l = m+1
            #     m = (l+r) // 2
            # offset = m
            
            s, e = 0, len(nums)-1
            while s <= e:
                m = (s+e) // 2
                # print(s, e, m)
                if nums[m] == target:
                    return m
                else:
                    if nums[m] <= nums[-1] :
                        e = m-1
                    elif nums[m] >= nums[0]:
                        s = m+1
                # print(s, e, m)
            offset = e
            
        print(offset)
        if nums[0] <= target <= nums[offset] :
            return self.BinSearch(nums, 0, offset , target)
        else:
            return self.BinSearch(nums, offset+1, len(nums)-1, target)
        
            
        
        
