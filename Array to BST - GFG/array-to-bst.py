class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBSTHelper(self,  nums, l, r):
        if l > r:
            return None
            
        m = (l+r) // 2
        root = Node(nums[m])
        root.left = self.sortedArrayToBSTHelper(nums, l, m-1)
        root.right = self.sortedArrayToBSTHelper(nums, m+1, r)
    
        return root
    
    def preOrderTraversal(self, BSTNode):
        if BSTNode is None:
            return []
        return [BSTNode.data] + self.preOrderTraversal(BSTNode.left) + self.preOrderTraversal(BSTNode.right)
        
    
	def sortedArrayToBST(self, nums):
	    # code here
	    if len(nums) == 0:
	        return None
	        
	    tree =  self.sortedArrayToBSTHelper( nums, 0, len(nums)-1)
	    return self.preOrderTraversal(tree)
	    
	    

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends