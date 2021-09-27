class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0 and n & (n-1) == 0)
        # return( n > 0 and sum([int(i) for i in bin(n).replace("0b", '').replace("-", "")]) == 1 )
        