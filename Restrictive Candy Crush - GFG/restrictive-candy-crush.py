#User function Template for python3

class Solution:
    def Reduced_String(self, k, s):
        # Your code goes here
        # return the reduced string
        
        
        if k == 1:
            return ""
            
        from collections import deque
        q, rcQ = deque(), deque()
        
        for i in s:
            if len(q) == 0 or q[-1] != i:
                q.append(i)
                rcQ.append(1)
            
            else:
                q.append(i)
                rcQ.append(rcQ[-1]+1)
                
                if rcQ[-1] == k:
                    while len(q) and q[-1] == i:
                        q.pop()
                        rcQ.pop()
                        
        return (''.join(list(q)))
    # def Reduced_String(self, k, s):
    #     # Your code goes here
    #     # return the reduced string
        
    #     from collections import deque
    #     q = deque()
        
    #     runningCount = 0
    #     for i in s:
    #         if len(q) == 0:
    #             runningCount += 1
    #             q.append(i)
                
            
    #         else:
    #             if q[-1] == i:
    #                 runningCount += 1
                
    #                 if runningCount == k:
    #                     while runningCount-1 > 0:
    #                         q.pop()
    #                         runningCount -= 1
    #                     runningCount = 1
    #                 else:
    #                     q.append(i)
    #             else:
    #                 q.append(i)
    #                 runningCount = 1
            
        
    #     return (''.join(list(q)))
                        
                    
                    
                    
            
         


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        k=int(input())
        s=input().strip()
        obj = Solution()
        print(obj.Reduced_String(k,s))

# } Driver Code Ends