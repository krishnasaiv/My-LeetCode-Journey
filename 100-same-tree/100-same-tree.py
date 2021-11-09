# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
################################################################################################
#### Recursion
################################################################################################    
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


################################################################################################
#### Recursion: InOrder & PreOrder Traversal 
################################################################################################ 

### This will only work if all the elements are distinct or 
### This will work if we add nulls for leaves with missing sibling leaves ( [1, 1], [1, null, 1])

#     def preOrderTraversal(self, root, arr):
#         if not root:
#             arr.append(None)
#             return
#         arr.append(root.val)
#         self.preOrderTraversal(root.left, arr)
#         self.preOrderTraversal(root.right, arr)
        
#     def inOrderTraversal(self, root, arr):
#         if not root:
#             arr.append(None)
#             return
#         self.inOrderTraversal(root.left, arr)
#         arr.append(root.val)
#         self.inOrderTraversal(root.right, arr)
        
        
    
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         pre1, pre2, in1, in2 = list(), list(), list(), list()
        
#         self.preOrderTraversal(p, pre1)
#         self.inOrderTraversal(p, in1)
        
#         self.preOrderTraversal(q, pre2)
#         self.inOrderTraversal(q, in2)
       
#         return ((pre1 == pre2) and (in1 == in2))
    

############# Space Complexity: O(8n) = O(n) #############
## 1. Storage for PreOrder ---> O(2n) * 2 ## because of the added nulls. ( if tree is like chain, we will add nullls for each missing sibling, so 2n)
## 2. Storage for InOrder ---> O(2n) * 2  ## because of the added nulls. ( if tree is like chain, we will add nullls for each missing sibling, so 2n)

############# Time Complexity: O(12n) = O(n) #############
## 1. PreOrder ---> O(2n) * 2
## 2. InOrder ---> O(2n) * 2
## 3. Compare lists ---> O(2n) * 2