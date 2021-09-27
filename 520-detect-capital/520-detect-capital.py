class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        return(word.isupper() or word.islower() or word.istitle())

############# Time Complexity: O(n) #############
## 1. iterate through the word --> O(n)

############# Space Complexity: O(1) #############
## 1. No Extra Space
