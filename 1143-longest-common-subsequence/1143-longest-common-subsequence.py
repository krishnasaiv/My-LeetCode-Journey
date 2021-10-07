class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ################################################
        ################# Iterative (Tabulation)
        ################################################
        l1, l2 = len(text1), len(text2)
        
#         dp =[ [0 for i in range(l2+1)] for j in range(l1+1)]
#         # print(dp)
        
#         for i in range(1, l1+1):
#             for j in range(1, l2+1):
                
#                 # print( (i, j), (text1[i-1], text2[j-1]), dp)
#                 if text1[i-1] == text2[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         return(dp[i][j])
    
    
    
        ################################################
        ################# Space Optimized Iterative (Tabulation)
        ################################################
        l1, l2 = len(text1), len(text2)
            
        dp_prev = [0 for i in range(l2+1)]
        
        for i in range(1, l1+1):
            dp_cur = [0 for i in range(l2+1)]
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    dp_cur[j] = 1 + dp_prev[j-1]
                else:
                    dp_cur[j] = max(dp_prev[j], dp_cur[j-1])

            dp_prev = dp_cur
                
        return(dp_prev[j])
                    
        
        
        
        
        