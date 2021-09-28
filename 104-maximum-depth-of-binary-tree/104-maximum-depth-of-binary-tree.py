# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def Traverse(root, CurDepth, MaxDepth):
    
    if root is None:
        return
    
    md = max(CurDepth, CurDepth if root.left is None else Traverse(root.left, CurDepth+1, MaxDepth))
    md = max(md, CurDepth if root.right is None else Traverse(root.right, CurDepth+1, MaxDepth))
    
    return md


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        return(Traverse(root, 1, 1))
        
        
        
        
        
        