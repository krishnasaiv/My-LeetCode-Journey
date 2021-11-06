# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        rangeSum = 0
        
        from collections import deque
        q = deque()
        
        q.append(root)
        
        while len(q):
            
            n = q[-1]
            if low <= n.val <= high: rangeSum +=  n.val
            q.pop()
            
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
            
        
        return(rangeSum)
            
            
            
        
            
        