# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def PreOrderTraverse(root, CurDepth, MaxDepth):
    
    if root is None:
        return
    
    ml = CurDepth if root.left is None else PreOrderTraverse(root.left, CurDepth+1, MaxDepth)
    mr = CurDepth if root.right is None else PreOrderTraverse(root.right, CurDepth+1, MaxDepth)
    
    return(max(ml, mr))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        return(PreOrderTraverse(root, 1, 1))
        
        
        
        
        
        