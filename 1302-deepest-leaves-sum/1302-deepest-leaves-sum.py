# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque   
        nodes = deque()
        nodes.append(root)
        
        while len(nodes):
            
            cnt = len(nodes)
            levelSum = 0
            for i in range(cnt):
                
                n = nodes[0]
                nodes.popleft()
                
                levelSum += n.val
                if n.left: nodes.append(n.left)
                if n.right: nodes.append(n.right)
            
        return(levelSum)
                
        
        
