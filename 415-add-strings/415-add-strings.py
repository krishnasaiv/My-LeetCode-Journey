class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x, y = (num1, num2) if len(num1) >= len(num2) else (num2, num1)
        result = ""
        carry = 0
        for i in range(-1, -1*len(x)- 1, -1):
            a, b = int(x[i]), int(y[i]) if  i >= -1 * len(y) else 0

            s = a + b + carry
            result = str(s % 10) + result
            carry = s // 10
        
        if carry:
            result = str(carry) + result
        return (result)
            
############# Time Complexity: O(n) #############
## 1. Adding 3 digits, atmost n times ---> O(n)

############# Space Complexity: O(n) #############
## 1. Space for the string 'result' ---> O(n)
        