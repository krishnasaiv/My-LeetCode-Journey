# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBST(self, root, minVal, maxVal):
        if root is None:
            return True
        
        return (minVal < root.val < maxVal) and \
        self.isBST(root.left, minVal, root.val) and \
        self.isBST(root.right, root.val, maxVal)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isBST(root, float('-inf'), float('inf'))
        
        