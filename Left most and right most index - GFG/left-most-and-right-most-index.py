#User function Template for python3

class Solution:
    def indexes(self, arr, x):
        # Your code goes here
        
        n = len(arr)
        
        ### Search for the start
        start = -1
        
        l,r = 0, n-1
        while l<=r:
            m = (l+r)//2
            
            if x < arr[m]:
                r = m-1
            elif x > arr[m]:
                l = m+1
            else:
                if m == 0 or arr[m-1] != arr[m]:
                    start = m
                    break
                else:
                    r = m-1
        
        ### Search for the end
        end = -1
        
        l,r = 0, n-1
        while l<=r:
            m = (l+r)//2
            
            if x < arr[m]:
                r = m-1
            elif x > arr[m]:
                l = m+1
            else:
                if m == n-1 or arr[m+1] != arr[m]:
                    end = m
                    break
                else:
                    l = m+1
        
        return [start, end]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends