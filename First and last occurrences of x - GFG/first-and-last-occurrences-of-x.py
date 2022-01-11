#User function Template for python3


def find(arr,n,x):
    # code here
    
    
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
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends