# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBSTHelper(self, nums, l, r):
        if l > r:
            return None
        
        m = (l+r)//2
        root = TreeNode(nums[m])
        
        root.left = self.sortedArrayToBSTHelper(nums, l, m-1)
        root.right = self.sortedArrayToBSTHelper(nums, m+1, r)
        
        return root
    
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
       
        return self.sortedArrayToBSTHelper(nums, 0, len(nums)-1)