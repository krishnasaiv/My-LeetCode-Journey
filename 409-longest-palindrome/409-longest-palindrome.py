from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        
        num = 0
        hasOddFreqChars = False
        for k in c:
            num += c[k]
            if c[k] % 2:
                num -= 1
                hasOddFreqChars = True
        
        return(num + int(hasOddFreqChars))
                
############# Time Complexity: O() #############
## 1. Iterate through the array once to build the Counter dictionary ---> O(n)
## 2. Iterate through the keys of the Counter dictionary ---> O(n)


############# Space Complexity: O() #############
## 1. Store each distinct character as a key in the dictionary. In worst case, there are no repeating keys. ---> O(n)