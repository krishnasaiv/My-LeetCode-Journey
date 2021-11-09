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
        if (not l) and (not r):
            return True
        elif (l and not r) or ( not l and r) or (l.val != r.val):
            return False
        return( self.isMirrorTree(l.left, r.right) and self.isMirrorTree(l.right, r.left) )

############# Time Complexity: O(n) #############
## 1. Traverse each node of the tree

############# Space Complexity: O(n) #############
## 1. Stack space for recusrsion which is max height of the tree


############# Comments #############
##      Here if the tree is not balanced & like a chain( we will find it in the first step itself). 
##      So, the more unbalanced the quicker it takes to decide symmetry
##      We could say the worst case takes place when the tree is balanced
##      Can we say the time & space complexities are O(log(n))
