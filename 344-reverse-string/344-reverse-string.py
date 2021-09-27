class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
            
        
############# Time Complexity: O(n) #############
## 1. Iterate from both ends until the midlle ---> O(n)

############# Space Complexity: O(1) #############
## 1. No extra Space ---> O(n)
        