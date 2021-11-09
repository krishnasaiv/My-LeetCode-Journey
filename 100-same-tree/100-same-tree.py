# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if (not p) and (not q):
            return True
        if (p and not q) or (not p and q) or (p.val != q.val):
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
############# Time Complexity: O(n) #############
## 1. Traverse each node of the tree

############# Space Complexity: O(n) #############
## 1. Stack space for recusrsion which is max height of the tree


############# Comments #############
##      Here if the tree is not balanced & like a chain( we will find it in the first step itself). 
##      So, the more unbalanced the quicker it takes to decide symmetry
##      We could say the worst case takes place when the tree is balanced
##      Can we say the time & space complexities are O(log(n))