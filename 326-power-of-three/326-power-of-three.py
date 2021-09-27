class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n:
            if n == 1:
                return True 
            if n % 3 > 0 :
                return False
            n = n // 3
        return True

## For all numbers <= 0, we return False. This is because the question clearly mentions if the given number 'n' can be represented as 3^x for any integer & there is no integer x when raised to the power of threee that will give a non natural number( <= 0 ) 