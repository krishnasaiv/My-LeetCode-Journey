# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### This function will never have None as value for parameter node because of 
    ###     1. if condition in 'minDepth'(line 21)
    ###     2. last two if conditions in treverseForMindepth (lines 16-17)
    
    def treverseForMindepth(self, node, curDepth, minimumdepth):
        
        if (not node.left) and (not node.right):
            minimumdepth[0] = min(minimumdepth[0], curDepth)
            
        if node.left: self.treverseForMindepth(node.left, 1+curDepth, minimumdepth)
        if node.right: self.treverseForMindepth(node.right, 1+curDepth, minimumdepth)
        
        
    
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return(0)

        minimumdepth = [float('inf')]
        self.treverseForMindepth(root, 1, minimumdepth)
        return(minimumdepth[0])
        
        
        