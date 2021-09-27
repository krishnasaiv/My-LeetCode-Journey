# import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ######################################################################################
        ####            Solution 1
        ######################################################################################
        
        #### Delete the punctuation & whitespaces
        #### If there are m punc & whitspace chars to search for & delete in a given string
        #### It takes O(n * m) time but here m is constant 
        #### so it takes O(n) to search for & delete the m chars
        # s = ''.join([i.lower() for i in s if i not in string.punctuation + string.whitespace])
        # s = ''.join([i.lower() for i in s if i.isalnum()])
        
        # l = 0
        # r = len(s) -1

#         while l <= r :
#             if s[l] != s[r]:
#                 return False
#             l += 1
#             r -= 1
        
#         return True
        ######################################################################################
        ####            Solution 2
        ######################################################################################        
#         s_cleaned = ''
        
#         for i in s:
#             if i.isalnum():
#                 s_cleaned += i.lower()
        
#         return s_cleaned == s_cleaned[::-1]
        ######################################################################################
        ####            Solution 3
        ######################################################################################
        
#         l = 0
#         r = len(s) - 1
        
#         while l < r:
#             if not s[l].isalnum():
#                 l += 1
#             elif not s[r].isalnum():
#                 r -= 1
#             elif s[l].lower() != s[r].lower():
#                 return False
#             else:           
#                 l += 1
#                 r -= 1
#         return True

        ######################################################################################
        ####            Solution 4
        ######################################################################################
        
        import re
        s = re.sub(r'[\W_]', '', s).lower()
        
        l, r  = 0, len(s) -1
        while l <= r :
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
