# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def InOrderTraversal(root, l):
    if root is None:
        return
    
    InOrderTraversal(root.left, l)
    l.append(root.val)
    InOrderTraversal(root.right, l)
    
    

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inOrder_BST = list()
        
        InOrderTraversal(root, inOrder_BST)
        minVal = float('inf')
        
        for i in range(1, len(inOrder_BST)):
            minVal = min(minVal, inOrder_BST[i] - inOrder_BST[i-1])
        
        return(minVal)
        