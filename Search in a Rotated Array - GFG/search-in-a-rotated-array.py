#User function Template for python3

class Solution:
    
    def BinSearch(self, A, l, r, key):
        # if l > r:
        #     return -1
        # m = (l+r) // 2
        # if A[m] == key:
        #     return m
        # elif key < A[m]:
        #     return self.BinSearch(A, l, m-1, key)
        # else:
        #     return self.BinSearch(A, l+1, m, key)
            
        if l > r:
            return -1
        m = (l+r) // 2
        if A[m] == key:
            return m
        elif A[m] > key:
            r = m-1
        else:
            l = m+1
        return self.BinSearch(A, l, r, key)
        
        
    def search(self, A : list, l : int, h : int, key : int):
        # Complete this function
        
        if len(A) == 1:
            return 0 if A[0] == key else -1
        
        s, e = l, h
        while s <= e:
            m = (s+e) // 2
            
            if A[m] == key:
                return m
                
            else:
                if A[m] <= A[-1] :
                    e = m-1
                elif A[m] >= A[0]:
                    s = m+1
        
        # print(s, e, m)
        # return ( l, e, h)
        return max(self.BinSearch(A, l, e, key), self.BinSearch(A, e+1, h, key))
         
        
        
                    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends