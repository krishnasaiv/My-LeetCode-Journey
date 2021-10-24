class Solution:
    def twoSum(self, nums, target):
        visited = dict()
        
        for i,val in enumerate(nums):
            
            if (target-val) in visited:
                return ([visited[target-val], i])
            
            visited[val] = i
                