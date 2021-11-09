# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return(self.isMirrorTree(root.left, root.right) )
    
    
    
    
    def isMirrorTree(self, l, r):
        # print("---------------")
        # print(l, r)
        if (not l) and (not r):
            return True
        elif (l and not r) or ( not l and r) or (l.val != r.val):
            return False
        # print(l.val, r.val)
        return( self.isMirrorTree(l.left, r.right) and self.isMirrorTree(l.right, r.left) )
        