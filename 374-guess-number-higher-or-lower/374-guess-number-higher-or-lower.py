# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l, r = 1, n

        while True:
            num = (l+r) // 2
            res = guess(num)
            
            if res == 0:
                return(num)
            elif res == 1:
                l = num + 1
            else:
                r = num -1
                
        
        
        