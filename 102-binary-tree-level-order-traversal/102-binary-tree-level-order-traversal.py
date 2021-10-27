# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return([])
        
        q = deque()
        q.append([root])
        
        curLevel = 0
        
        while True:
            
            q.append(list())
            nextLevel = curLevel+1
            
            for i in range(len(q[curLevel])):
                
                if q[curLevel][i].left: q[nextLevel].append(q[curLevel][i].left)
                if q[curLevel][i].right: q[nextLevel].append(q[curLevel][i].right)
                    
                q[curLevel][i] = q[curLevel][i].val
                
                
            if len(q[nextLevel]) == 0:
                q.pop()
                break
            
            curLevel += 1
            
            
        return(q)
                        
            
        
        