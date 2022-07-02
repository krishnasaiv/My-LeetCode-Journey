from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ##### find xor of all elements
        xor = 0
        for i in nums:
            xor ^= i
            
        ##### find right most set bit
        x,n = xor,0
        while not(x & 1):
            x = x >> 1
            n += 1
        r = pow(2, n)
        
        
        #### find the two elements
        r1 = r2 = 0
        for i in nums:
            if i & r:
                r1 ^= i
            else:
                r2 ^= i
                
        return [r1, r2]
        
        
        