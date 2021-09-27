# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

########### Constant Space solution


prev = minVal = float('inf')

def InOrderTraversal(root):
    if root is None:
        return
    global prev, minVal
    
    InOrderTraversal(root.left)
    # print("----------------------------")
    # print(prev, minVal)
    minVal = min(minVal, abs(root.val-prev))
    prev = root.val
    # print(root.val)
    # print(prev, minVal)
    InOrderTraversal(root.right)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global prev, minVal
        prev = minVal = float('inf')
        InOrderTraversal(root)
        return(minVal)
    
############# Time Complexity: O(n) #############
## 1. Traverse through each node of the BST once ---> O(n)
## 2. Traverse through the InOrder traversal & find the min of diffrence between consequrive nodes ---> O(n)

############# Space Complexity: O(1) #############
## 1. Space for recursing through the tree ---> O(n) | Total recursive calls on stack would be the max depth of the tree. The worst case max-depth would be O(n) because they did not mention that the BST is balanced.  ( This is not an extra space so, space complexity is still O(1))



########### Linear Space solution
# def InOrderTraversal(root, l):
#     if root is None:
#         return
    
#     InOrderTraversal(root.left, l)
#     l.append(root.val)
#     InOrderTraversal(root.right, l)
    
    

# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#         inOrder_BST = list()
        
#         InOrderTraversal(root, inOrder_BST)
#         minVal = float('inf')
        
#         for i in range(1, len(inOrder_BST)):
#             minVal = min(minVal, abs(inOrder_BST[i] - inOrder_BST[i-1]))
        
#         return(minVal)


############# Time Complexity: O(n) #############
## 1. Traverse through each node of the BST once ---> O(n)
## 2. Traverse through the InOrder traversal & find the min of diffrence between consequrive nodes ---> O(n)

############# Space Complexity: O(n) #############
## 1. Space for recursing through the tree ---> O(n) | Total recursive calls on stack would be the max depth of the tree. The worst case max-depth would be O(n) because they did not mention that the BST is balanced.
## 2. Space to store the result of InOrder travelsal ---> O(n)