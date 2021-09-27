class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1 :
            return(s)
        
        l, r = 0, len(s)-1
        s = [i for i in s]
        vowels = 'aeiouAEIOU'
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l] += s[r]
                s[r] = s[l][0]
                s[l] = s[l][1]
                # s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l] not in vowels:
                    l += 1

                if s[r] not in vowels:
                    r -= 1
        return(''.join(s))
    
    
    ### You could use a stack for the vowels, put vowels in stack as you go through the sting & also store the indces of vowels.
    ### loop back on the string indices & place the top elements from stack
    
    
    