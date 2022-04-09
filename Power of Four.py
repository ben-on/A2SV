class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power3(a):
            if a==1:
                return True
            elif a==0:
                return False
            elif a%4==0:
                return power3(a/4)
            else :
                return False
        return power3(n)
#         while 1:
#             if n==1:
#                 return True
#             elif n==0:
#                 return False
#             elif n%3==0:
#                 n=n/3
#             else :
#                 return False
                
         