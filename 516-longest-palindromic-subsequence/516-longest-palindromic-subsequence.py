class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ##############################################################
        ###### Longest Common SubSequence with the reversed string
        ##############################################################
        
        t = s[::-1]
        
        l1, l2 = len(s), len(t)
        
        dp_prev = [0] * (l2+1)
        
        for i in range(1, l1+1):
            dp_cur = [0] * (l1+1)
            for j in range(1, l2+1):
                
                if s[i-1] == t[j-1]:
                    dp_cur[j] = 1 + dp_prev[j-1]
                else:
                    dp_cur[j] = max(dp_cur[j-1], dp_prev[j])
                
            dp_prev = dp_cur
        
        
        return(dp_cur[-1])
            
        