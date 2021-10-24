class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        for i in range(9):
            freq = {str(a+1):False for a in range(9)}
            
            for j in range(9):
                if board[i][j] != '.' and freq[board[i][j]]:
                    # print((i,j), freq)
                    return(False)
                freq[board[i][j]] = True
        
        
        for j in range(9):
            freq = {str(a+1):False for a in range(9)}
            
            for i in range(9):
                if board[i][j] != '.' and freq[board[i][j]]:
                    # print((i,j), freq)
                    return(False)
                freq[board[i][j]] = True
        
        
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                freq = {str(a+1):False for a in range(9)}
                
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        # print((r,c), (i,j))
                        if board[i][j] != '.' and freq[board[i][j]]:
                            # print((r,c), (i,j), freq)
                            return(False)
                            
                        freq[board[i][j]] = True
        return(True)
                        
