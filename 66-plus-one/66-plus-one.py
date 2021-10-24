
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits [-1] += 1
            return(digits)
        else:
            # newdigits = [0] + digits
            carry = 1
            for i in range(len(digits)-1, -1, -1):
                num = digits[i]
                digits[i] = (num + carry) % 10
                carry = (num+carry) // 10
            
            if carry == 0:
                return(digits)
            else:
                return([1]+digits)
            
        
        