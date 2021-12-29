class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nRows, nCols = len(matrix), len(matrix[0])
        
        u, d = 0, nRows-1
        while u <= d :                              # this should be <=  because we want to consider the array when u == d
            mRow = (u+d) // 2
            if target < matrix[mRow][0] :
                d = mRow-1
            elif target > matrix[mRow][-1]:
                u = mRow+1
            else:                                   # matrix[mRow][0] <= target <= matrix[mRow][-1]
                
                l, r = 0, nCols-1
                while l <= r:
                    mCol = (l+r) // 2
                    if target < matrix[mRow][mCol] :
                        r = mCol-1
                    elif target > matrix[mRow][mCol]:
                        l = mCol+1
                    else:                           # matrix[mRow][mCol] == target:
                        return True
                return False
            
        return False
        
        