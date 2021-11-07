class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        numSorted = sorted(list(set(nums)))
        return (self.LCS(nums, numSorted, len(nums), len(numSorted) ))
        
        
    def LCS (self, arr1, arr2, l1, l2):
        if l1 == 0 or l2 == 0:
            return 0
        
        LCS_DP_Prev = [0] * (l2+1)
        
        for i in range(1, l1+1):
            LCS_DP_Cur = [0] * (l2+1)
            for j in range(1, l2+1):
                if arr1[i-1] == arr2[j-1]:
                    LCS_DP_Cur[j] = 1 +  LCS_DP_Prev[j-1]
                else:
                    LCS_DP_Cur[j] = max(  LCS_DP_Prev[j], LCS_DP_Cur[j-1] )
        
            LCS_DP_Prev = LCS_DP_Cur
        
        return (LCS_DP_Cur[-1])