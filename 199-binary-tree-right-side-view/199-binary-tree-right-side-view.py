# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



def rightView (node, curLevel, maxLevel):
    if node is None: 
        return([])
    
    res = []
    if maxLevel[0] < curLevel:
        res += [node.val]
        maxLevel[0] = curLevel
        
    return (res + rightView (node.right, curLevel+1, maxLevel) + rightView (node.left, curLevel+1, maxLevel) )

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        curLevel = 0
        maxLevel = [-1]
        
        return( rightView (root, curLevel, maxLevel) )
        
        
