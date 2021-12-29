#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		
		start = end = -1
		
		#### Find the starting index of given element
		l, r = 0, n-1
		while l <= r:
		    m = (l+r) // 2
		    if x < arr[m]:
		        r=m-1
		    elif x > arr[m]:
		        l=m+1
            else:
                if m >= 1 and arr[m-1] == arr[m]:
                    r=m-1
                else:
                    start = m
                    break
                
        #### Find the ending index of given element
		l, r = 0, n-1
		while l <= r:
		    m = (l+r) // 2
		    if x < arr[m]:
		        r=m-1
		    elif x > arr[m]:
		        l=m+1
            else:
                if m <= n-2 and arr[m] == arr[m+1]:
                    l=m+1
                else:
                    end = m
                    break
                
        
        if start + end == -2:
            return 0 
        else:
            return end - start + 1
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends