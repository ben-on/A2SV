class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)


# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if x==0:
#             return 0
#         def poww(b,p):
#             for i in range(p):
#                 p*=p
#             return p
#         if n>0:
#             return poww(x,n)
#         if n < 0:
#             return 1/poww(x,-n)
#         if n==0 and x!=0:
#             return 1
            