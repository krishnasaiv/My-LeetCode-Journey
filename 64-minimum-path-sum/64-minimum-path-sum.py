class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        ### TRICK: We only need to maintain the dp cost values of the previous row & do not need any previous rows' costs 
        
        ## Populate the costs for the first row
        dp_PrevRow = grid[0]
        for j in range(1, n):
            dp_PrevRow[j] +=  dp_PrevRow[j-1]
        
        ## Iterate from the second row
        for i in range(1, m):
            dp_CurRow = [0] * (n)
            for j in range(n):
                dp_CurRow[j] = (dp_PrevRow[j] if j==0 else min(dp_CurRow[j-1], dp_PrevRow[j]) ) + grid[i][j]
            
            dp_PrevRow = dp_CurRow
            
        
            
        return dp_PrevRow[-1]
                
            
                
############# Time Complexity: O(m * n) #############
## 1. Traverse each element of the matrix ---> O(m*n)

############# Space Complexity: O(n) #############
## 1. Maintain a DP array for prev row ---> O(n)
                
        
        