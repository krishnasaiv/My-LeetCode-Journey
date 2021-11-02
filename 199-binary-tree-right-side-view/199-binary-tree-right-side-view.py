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

#################################################
## 1. Approach 1: Recursive PreOrder Traversal with maxLevel & curLevel  ---> T:O(n) ; S:O(maxDepth) 
## 2. Approach 2: Level Order traversal ---> T:O(n) ; S:O(maxNodesInaLevel)

        
############# Time Complexity: O(n) #############
## 1.

############# Space Complexity: O(maxDepth) #############
## 1.