import string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ####### Left & Right Pointer ---> S(O(1))
        ####### 1 pass through the string ---> T(O(n))
        ####### Space for list to sstore the characters of the string ---> S(O(n))
        
        s = [i for i in s]
        l, r = 0, len(s)-1
        
        while True:
            while l <= len(s)-1 and  not s[l].isalpha(): #((65 <= ord(s[l]) <= 90) or (97 <= ord(s[l]) <= 122))  :
                l += 1
            while r >= 0 and not s[r].isalpha(): #((65 <= ord(s[r]) <= 90) or (97 <= ord(s[r]) <= 122)) :
                r -= 1
            
            if l >= r:
                break
            
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return("".join(s))
     
        ####### 1 pass through the string to store all the alphabets in a stack ---> T(O(n))
        ####### Space for a stack to store the characters of the string ---> S(O(n))
        ####### 1 more pass through the string to place back alphabets in reverse order ---> T(O(n))
        ####### Space for new string to place the alphabets & other characters ---> S(O(n))
        
#         from collections import deque
#         q = deque()
        
#         for i in s:
#             if i.isalpha(): # (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
#                 q.append(i)
        
#         result = ""
#         for i in s:
#             if i.isalpha(): #(65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
#                 c = q[-1]
#                 q.pop()
#             else:
#                 c = i
            
#             result += c
        
#         return(result)
                
############# Time Complexity: O(n) #############

############# Space Complexity: O(n) #############

        