class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def profit(i,bol):
            if i>=len(prices):
                return 0
            if (i,bol) in dp:
                return dp[(i,bol)]
            cooldown=profit(i+1,bol)
            if bol:
                buy=profit(i+1,False)-prices[i]
                dp[(i,bol)]=max(cooldown,buy)
            else:
                sell=profit(i+2,True)+prices[i]
                dp[(i,bol)]=max(cooldown,sell)
            return dp[(i,bol)]
        return profit(0,True)
            