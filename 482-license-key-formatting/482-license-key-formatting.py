class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]

        return( "-".join( [ s[i:i+k] for i in range(0, len(s), k) ] )[::-1] )
    
            
############# Time Complexity: O(n+k) #############
## 1. Reverse String & Filter out only Alpha Numeric Characters ---> O(n)
## 2. Join substrings of size 'k' ---> O(k) 

############# Space Complexity: O(n) #############
## 1. Space to store the result & intermediate variables ---> O(n)