class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return([[1]])
        if numRows == 2:
            return ([[1], [1,1]])
        
        PT = [[1], [1,1]]
        
        for i in range(3, numRows+1):
            PT.append([1] * i)
            
            for j in range(1, i-1):
                # print(i, j)
                PT[i-1][j] = PT[i-2][j-1] + PT[i-2][j]
            
        
        return(PT)
        