#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        
        if k < Arr[0]:
            return 0
        if k > Arr[-1]:
            return N
        
        l, r = 0, N-1
        
        while l <= r:
            m = (l+r) // 2
            
            if k == Arr[m]:
                return m
            elif k <= Arr[m]:
                r = m-1
            else:
                l = m+1
        
        return l

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends