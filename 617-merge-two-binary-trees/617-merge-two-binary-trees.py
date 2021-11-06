# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root1 is None and root2 is None:
#             return None
        
#         if root1 is None or root2 is None:
#             return root1 if root2 is None else root1
        
#         from collections import deque
#         q1, q2 = deque(), deque()
#         q1.append(root1)
#         q2.append(root2)
        
#         while len(q1) + len(q2): 
#             n1, n2 = q1[0], q2[0]
#             q1.pop()
#             q2.pop()
            
#             n1.val += n2.val
            
#             if n1.left is None
            
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans


        