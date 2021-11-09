# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    
    def checkbalancedAndReturnHeight(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return(True, 0)
        
        leftIsBalanced, leftHeight = self.checkbalancedAndReturnHeight(root.left)
        rightIsBalanced, rightHeight = self.checkbalancedAndReturnHeight(root.right)
        
        return (abs(leftHeight-rightHeight)<= 1 and leftIsBalanced and rightIsBalanced, 1 + max(leftHeight, rightHeight)) ## Add 1 to increase height of parent by 1
    
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ### Access the Bollean Flag only
        return( self.checkbalancedAndReturnHeight(root)[0] )
       
    
    