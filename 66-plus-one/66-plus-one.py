
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits [-1] += 1
            return(digits)
        else:
            # newdigits = [0] + digits
            num2 = 1
            for i in range(len(digits)-1, -1, -1):
                num1 = digits[i]
                digits[i] = (num1 + num2) % 10
                num2 = (num1+num2) // 10
            
            if num2 == 0:
                return(digits)
            else:
                return([1]+digits)
            
        
        