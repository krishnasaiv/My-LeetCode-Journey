    

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        nRows, nCols = len(grid), len(grid[0])
        p = 0
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    #### UP
                    if i == 0 or grid[i-1][j] == 0:
                        p += 1
                    #### Down
                    if i == nRows-1 or grid[i+1][j] == 0:
                        p += 1
                    #### Left
                    if j == 0 or grid[i][j-1] == 0:
                        p += 1    
                    #### Right
                    if j == nCols-1 or grid[i][j+1] == 0:
                        p += 1

        return(p)

############# Time Complexity: O(m * n) #############
## 1. Iterate through each cell of the grid & check all the 4 directions ---> O(n)

############# Space Complexity: O(1) #############
## 1. No Extra Space required (at any size of the grid) ---> O(1)