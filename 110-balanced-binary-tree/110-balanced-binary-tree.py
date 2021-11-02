# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def CheckHeightAndBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return(True, -1)
        
        l = self.CheckHeightAndBalanced(root.left)
        r = self.CheckHeightAndBalanced(root.right)
        lh, rh = l[1]+1, r[1]+1
        
        return (abs(lh-rh)<= 1 and l[0] and r[0], max(lh, rh))
        
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return(self.CheckHeightAndBalanced(root)[0])