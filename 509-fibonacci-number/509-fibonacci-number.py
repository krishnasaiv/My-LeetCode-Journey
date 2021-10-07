class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return(n)

        f1, f2 = 0, 1
        for i in range(2, n+1):
            f1, f2 = f2, f1+f2

        return(f2)

# f = [0, 1] + [-1] * 29

# class Solution:
#     def fib(self, n: int) -> int:
#         if f[n] < 0:
#             f[n] = self.fib(n-1) + self.fib(n-2)
            
#         return(f[n])