class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        def myfib(nn):
            if nn==1 or nn==0:
                return nn
            if nn in dp:
                return dp[nn]
            else:
                a = myfib(nn-1)+myfib(nn-2)
                dp[nn] = a
                return a
        return myfib(n)